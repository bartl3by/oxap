#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from swagger_server.oxap.soap_types import SOAPStandard, SOAPReseller
from swagger_server.oxap.endpoint_interface_types import AppsuiteSOAP


class EndpointInterface(object):

    def __init__(self, oxap_account_id, endpoint_id, endpoint_interface_id, name, description, location, ssl_verify, login, password, ignore_binding, reseller, type: str):
        self.oxap_account_id = oxap_account_id
        self.endpoint_id = endpoint_id
        self.endpoint_interface_id = endpoint_interface_id
        self.name = name
        self.description = description
        self.location = location
        self.ssl_verify = ssl_verify
        self.login = login
        self.password = password
        self.ignore_binding = ignore_binding
        self.reseller = reseller
        self.type = type

        self.soap_type = None
        self._setSOAPType()

    def getOXAPAccountId(self) -> str:
        return self.oxap_account_id

    def getEndpointId(self) -> str:
        return self.endpoint_id

    def getEndpointInterfaceId(self) -> str:
        return self.endpoint_interface_id

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getLocation(self) -> str:
        return self.location

    def getSSLVerify(self) -> bool:
        return self.ssl_verify

    def getLogin(self) -> str:
        return self.login

    def getPassword(self) -> str:
        return self.password

    def getIgnoreBinding(self) -> bool:
        return self.ignore_binding

    def getReseller(self) -> bool:
        return self.reseller

    def getType(self) -> str:
        return self.type

    def getSOAPType(self) -> int:
        return self.soap_type

    def _setSOAPType(self):
        if self.type == AppsuiteSOAP() and self.reseller == False:
            self.soap_type = SOAPStandard
        elif self.type == AppsuiteSOAP() and self.reseller == True:
            self.soap_type = SOAPReseller
