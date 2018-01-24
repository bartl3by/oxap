#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class AuthenticationException(Exception):
    pass


class UnknownRoleException(AuthenticationException):
    pass


class DuplicateSessionIdException(AuthenticationException):
    pass


class WrongCredentialsException(AuthenticationException):
    pass


class AccountInformationNotFoundException(AuthenticationException):
    pass
