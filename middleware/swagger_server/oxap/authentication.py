#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import datetime
import uuid

from tornado.options import options

from swagger_server.models.session import Session
from swagger_server.oxap.exceptions.authentication_exceptions import *
from swagger_server.oxap.models.oxap_account import OXAPAccount
from swagger_server.oxap.types.session_types import *


class Authentication(object):

    def __init__(self, username: str, password: str, role: str, account_id: str, endpoint_id: str=None):
        self._username = username
        self._password = password
        self._role = role
        self._account_id = account_id
        self._endpoint_id = endpoint_id

        self._session = None

    def login(self) -> Session:
        if self._role == oxap():
            if not self.__verify_authorization_oxap():
                raise AuthenticationException()
        elif self._role == reseller():
            if not self.__verify_authorization_reseller():
                raise AuthenticationException()
        elif self._role == context():
            if not self.__verify_authorization_context():
                raise AuthenticationException()
        elif self._role == user():
            if not self.__verify_authorization_user():
                raise AuthenticationException()
        else:
            raise UnknownRoleException('Role %s is invalid', self._role)

        self._session = self.__generate_session()

        return self._session

    def __verify_authorization_oxap(self) -> bool:
        oxap_account = OXAPAccount(self._account_id)

        if oxap_account.getUsername() == self._username and oxap_account.getEncryptedPassword() not in (None, ''):
            if oxap_account.getEncryptedPassword().startswith('$pbkdf2-sha1$'):
                from passlib.hash import pbkdf2_sha1 as algorithm
            elif oxap_account.getEncryptedPassword().startswith('$pbkdf2-sha256$'):
                from passlib.hash import pbkdf2_sha256 as algorithm
            elif oxap_account.getEncryptedPassword().startswith('$pbkdf2-sha512$'):
                from passlib.hash import pbkdf2_sha512 as algorithm
            elif oxap_account.getEncryptedPassword().startswith('$bcrypt-sha256$'):
                from passlib.hash import bcrypt_sha256 as algorithm
            else:
                logging.error('Unknown password hashing algorithm found in user password hash: %s',
                              oxap_account.getEncryptedPassword())
                return False

            return algorithm.verify(self._password, oxap_account.getEncryptedPassword())

        return False

    def __verify_authorization_reseller(self) -> bool:
        return False

    def __verify_authorization_context(self) -> bool:
        return False

    def __verify_authorization_user(self) -> bool:
        return False

    def __generate_session(self) -> Session:
        return Session(self.__generate_session_id(),
                       datetime.datetime.utcnow().strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
                       (datetime.datetime.utcnow() + datetime.timedelta(seconds=options.session_timeout)).strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
                       self._account_id,
                       self._endpoint_id,
                       self._role)

    def __generate_session_id(self) -> str:
        return str(uuid.uuid4())
