#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from requests import Session
from tornado.options import options
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

from swagger_server.oxap.models.oxap_account import OXAPAccount
from swagger_server.oxap.types.endpoint_interface_types import AppsuiteSOAP
from swagger_server.oxap.types.service_types import ContextService
from swagger_server.oxap.types.soap_types import SOAPReseller, SOAPStandard


class SOAPHandler(object):

    def __init__(self, oxap_account_id: str, endpoint_id: str, service_type):
        self.oxap_account_id = oxap_account_id
        self.endpoint_id = endpoint_id
        self.service_type = service_type

        self.oxap_account = OXAPAccount(self.oxap_account_id)
        self.endpoint = self.oxap_account.getEndpoint(self.endpoint_id)
        self.endpoint_interface = self.oxap_account.getEndpointInterfaceByType(
            self.endpoint_id, AppsuiteSOAP())

        self.client = self._initiate_oxsoap_client()
        self.service = self._create_oxsoap_service()
        self.credentials = self._get_oxsoap_credentials_object()

    def _create_oxsoap_service(self):
        binding_url = None
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            binding_url = "{http://soap.admin.openexchange.com}"
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            binding_url = "{http://soap.reseller.admin.openexchange.com}"
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

        if self.endpoint_interface.getIgnoreBinding():
            return self.client.create_service(
                binding_url + self._get_service_name() + "SoapBinding",
                self.endpoint_interface.getLocation() + "/" + self._get_service_name())
        else:
            return self.client.service

    def _get_service_name(self) -> str:
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            if self.service_type == ContextService:
                return "OXContextService"
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            if self.service_type == ContextService:
                return "OXResellerContextService"
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

    def _get_oxsoap_credentials_object(self):
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            return self.client.get_type('ns5:Credentials')
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            return self.client.get_type('ns7:Credentials')
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

    def _get_oxsoap_context_object(self):
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            return self.client.get_type('ns4:Context')
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            return self.client.get_type('ns4:ResellerContext')
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

    def _get_oxsoap_schema_select_strategy_object(self):
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            return self.client.get_type('ns4:SchemaSelectStrategy')
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            return self.client.get_type('ns5:SchemaSelectStrategy')
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

    def _get_oxsoap_user_object(self):
        if self.endpoint_interface.getSOAPType() == SOAPStandard:
            return self.client.get_type('ns4:User')
        elif self.endpoint_interface.getSOAPType() == SOAPReseller:
            return self.client.get_type('ns5:User')
        else:
            logging.error("Unknown SOAP type found: " + str(self.endpoint_interface.getSOAPType()))

    def _initiate_oxsoap_client(self):
        session = Session()
        session.verify = self.endpoint_interface.getSSLVerify()
        cache = SqliteCache(path=options.cache_wsdl_store_path, timeout=options.cache_wsdl_timeout)
        transport = Transport(session=session, cache=cache)
        return Client(
            self.endpoint_interface.getLocation() + "/" + self._get_service_name() + "?wsdl",
            transport=transport)
