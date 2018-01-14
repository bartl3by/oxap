#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from swagger_server.oxap.endpoint_interface import EndpointInterface


class Endpoint(object):

    def __init__(self, oxap_account_id, endpoint_id, name, description, oxaas, endpoint_interfaces):
        self.oxap_account_id = oxap_account_id
        self.endpoint_id = endpoint_id
        self.name = name
        self.description = description
        self.oxaas = oxaas
        self.endpoint_interfaces = endpoint_interfaces

    def getOXAPAccountId(self) -> str:
        return self.oxap_account_id

    def getEndpointId(self) -> str:
        return self.endpoint_id

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getOXaaS(self) -> bool:
        return self.oxaas

    def getEndpointInterfaces(self) -> List[EndpointInterface]:
        return self.endpoint_interfaces
