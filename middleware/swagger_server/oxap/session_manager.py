#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import logging

import connexion
from pymemcache.client.base import Client
import tornado
from tornado.options import options

from swagger_server.models.session import Session
from swagger_server.oxap.authentication import Authentication
from swagger_server.oxap.exceptions.authentication_exceptions import DuplicateSessionIdException
from swagger_server.oxap.exceptions.session_exceptions import (ClientSessionIdMissingException,
                                                               NoSuchSessionException,
                                                               SessionExpiredException)

header_name = 'Oxapsessionid'


def __verify_session_header(*outer_args, **outer_kwargs):
    def decorator(fn):
        def decorated(*args, **kwargs):
            if connexion.request.headers is None \
                    or header_name not in connexion.request.headers \
                    or connexion.request.headers[header_name] is None:
                raise ClientSessionIdMissingException('Missing session id in request header')
            return fn(*args, **kwargs)
        return decorated
    return decorator


def __get_method_scope(method: str) -> str:
    if hasattr(tornado.options, "session_method_scopes") and \
            method in getattr(tornado.options, "session_method_scopes"):
        return getattr(tornado.options, "session_method_scopes")[method]
    else:
        return None


def __method_has_scope(method: str) -> bool:
    return __get_method_scope(method) not in (None, '')


def __refresh_session(memcache: Client, session: Session) -> Session:
    if memcache.check_key(connexion.request.headers[header_name]):
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


def create_session(account_id: str, endpoint_id: str, role: str, username: str, password: str) -> Session:
    authentication = Authentication(username, password, role, account_id, endpoint_id)
    session = authentication.login()

    memcache = __get_memcache_client()
    cache_value_raw = memcache.get(session.id)
    if cache_value_raw not in (None, ''):
        raise DuplicateSessionIdException('Generated session id already in cache')
    memcache.add(session.id, json.dumps(session.to_dict()),
                 options.session_timeout, options.cache_session_memcache_noreply)
    memcache.close()

    return session


@__verify_session_header()
def get_session_information(refresh: bool=True) -> Session:
    memcache = __get_memcache_client()

    cache_value_raw = memcache.get(connexion.request.headers[header_name])
    if cache_value_raw in (None, ''):
        memcache.close()
        raise NoSuchSessionException('Session id is unknown or expired')

    session = Session.from_dict(json.loads(cache_value_raw))
    if __session_expired(session):
        memcache.delete(connexion.request.headers[header_name],
                        options.cache_session_memcache_noreply)
        memcache.close()
        raise SessionExpiredException('Session id is unknown or expired')
    else:
        if refresh:
            session = __refresh_session(memcache, session)
        memcache.close()
        return session


@__verify_session_header()
def delete_session() -> bool:
    memcache = __get_memcache_client()

    cache_value_raw = memcache.get(connexion.request.headers[header_name])
    if cache_value_raw in (None, ''):
        memcache.close()
        raise NoSuchSessionException('Session id is unknown or expired')

    memcache.delete(connexion.request.headers[header_name],
                    options.cache_session_memcache_noreply)
    memcache.close()

    return True

def session_in_scope(method: str, refresh: bool) -> bool:
    if not __method_has_scope(method):
        return True

    session = get_session_information(refresh)
    if session.role in __get_method_scope(method):
        return True

    return False


def get_method_scope(method: str) -> str:
    return __get_method_scope(method)


def register_method_scope(method: str, scope: str=None):
    logging.debug('Registering security scope \'' + str(scope) + '\' for method ' + method)

    session_method_scopes = dict()
    if hasattr(tornado.options, "session_method_scopes"):
        session_method_scopes = getattr(tornado.options, "session_method_scopes")

    session_method_scopes[method] = scope

    setattr(tornado.options, "session_method_scopes", session_method_scopes)
