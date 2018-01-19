#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SessionException(Exception):
    pass


class ClientSessionIdMissingException(SessionException):
    pass


class NoSuchSessionException(SessionException):
    pass


class SessionExpiredException(SessionException):
    pass
