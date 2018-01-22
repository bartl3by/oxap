#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import datetime
import uuid

import connexion
import json
from pymemcache.client.base import Client
import tornado
from tornado.options import options
from swagger_server.models.session import Session
from swagger_server.oxap.exceptions.session_exceptions import ClientSessionIdMissingException,\
    NoSuchSessionException, SessionExpiredException


cookie_name = 'Oxapsessionid'


def __verify_client_cookie(*outer_args, **outer_kwargs):
    def decorator(fn):
        def decorated(*args, **kwargs):
            if connexion.request.cookies is None \
                    or cookie_name not in connexion.request.cookies \
                    or connexion.request.cookies[cookie_name] is None:
                raise ClientSessionIdMissingException('Missing session id in request')
            return fn(*args, **kwargs)
        return decorated
    return decorator


def __get_method_scope(method: str) -> str:
    if hasattr(tornado.options, "session_method_scopes") and method in getattr(tornado.options, "session_method_scopes"):
        return getattr(tornado.options, "session_method_scopes")[method]

    return None


def __refresh_session(memcache: Client, session: Session) -> Session:
    if memcache.check_key(connexion.request.cookies[cookie_name]):
        session.expiration_date = (datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=options.session_timeout)).strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        memcache.set(session.id, json.dumps(session.to_dict()),
                     options.session_timeout, options.cache_session_memcache_noreply)
        return session
    else:
        raise NoSuchSessionException('Session id is unknown or expired')


def __get_memcache_client() -> Client:
    return Client((options.cache_session_memcache_host, options.cache_session_memcache_port))


def __session_expired(session: Session) -> bool:
    return datetime.datetime.strptime(session.expiration_date, "%a, %d-%b-%Y %H:%M:%S GMT") < datetime.datetime.utcnow()


def __generate_session_id() -> str:
    return str(uuid.uuid4())


def create_session(account_id: str, endpoint_id: str, role: str, username: str, password: str) -> Session:
    memcache = __get_memcache_client()
    session = Session(__generate_session_id(),
                      cookie_name,
                      datetime.datetime.utcnow().strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
                      (datetime.datetime.utcnow() + datetime.timedelta(seconds=options.session_timeout)).strftime(
                          "%a, %d-%b-%Y %H:%M:%S GMT"),
                      account_id,
                      endpoint_id,
                      role)

    memcache.add(session.id, json.dumps(session.to_dict()),
                 options.session_timeout, options.cache_session_memcache_noreply)
    memcache.close()

    return session


@__verify_client_cookie()
def get_session_information(refresh: bool) -> Session:
    memcache = __get_memcache_client()

    if not memcache.check_key(connexion.request.cookies[cookie_name]):
        memcache.close()
        raise NoSuchSessionException('Session id is unknown or expired')

    session = Session.from_dict(json.loads(memcache.get(connexion.request.cookies[cookie_name])))
    if __session_expired(session):
        memcache.delete(connexion.request.cookies[cookie_name],
                        options.cache_session_memcache_noreply)
        memcache.close()
        raise SessionExpiredException('Session id is unknown or expired')
    else:
        if refresh:
            session = __refresh_session(memcache, session)
        memcache.close()
        return session


@__verify_client_cookie()
def delete_session():
    memcache = __get_memcache_client()

    cache_value = memcache.get(connexion.request.cookies[cookie_name])
    if cache_value is not None:
        memcache.delete(connexion.request.cookies[cookie_name],
                        options.cache_session_memcache_noreply)
        memcache.close()
        return
    else:
        memcache.close()
        raise NoSuchSessionException('Session id is unknown or expired')


def session_in_scope(method: str, refresh: bool) -> bool:
    if __get_method_scope(method) in (None, ''):
        return True

    session = get_session_information(refresh)
    if session.role == __get_method_scope(method):
        return True

    return False


def method_has_scope(method: str) -> bool:
    return __get_method_scope(method) is not (None, '')


def get_method_scope(method: str) -> str:
    return __get_method_scope(method)


def register_method_scope(method: str, scope: str=None):
    logging.debug('Registering security scope \'' + str(scope) + '\' for method ' + method)

    session_method_scopes = dict()
    if hasattr(tornado.options, "session_method_scopes"):
        session_method_scopes = getattr(tornado.options, "session_method_scopes")

    session_method_scopes[method] = scope

    setattr(tornado.options, "session_method_scopes", session_method_scopes)
