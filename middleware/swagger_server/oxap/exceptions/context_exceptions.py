#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree


class ContextException(Exception):

    def __init__(self, message, detail):
        assert message is not None
        assert detail is not None and len(detail) > 0

        Exception.__init__(self, message)
        self.name = etree.QName(detail[0].tag).localname
        self.message = message
        self.namespace = etree.QName(detail[0].tag).namespace
        self.prefix = detail[0].prefix
        self.detail = detail

        try:
            self.__class__ = globals()[self.name]
        except:
            pass

    def __str__(self):
        return self.message

class ContextExistsException(ContextException):
    pass

class DatabaseUpdateException(ContextException):
    pass

class DuplicateExtensionException(ContextException):
    pass

class InvalidCredentialsException(ContextException):
    pass

class InvalidDataException(ContextException):
    pass

class NoSuchContextException(ContextException):
    pass

class NoSuchDatabaseException(ContextException):
    pass

class NoSuchFilestoreException(ContextException):
    pass

class NoSuchReasonException(ContextException):
    pass

class OXContextException(ContextException):
    pass

class RemoteException(ContextException):
    pass

class StorageException(ContextException):
    pass
