#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from requests import Session
from swagger_server.models.base_model_ import Model
from swagger_server.models.context import Context
from swagger_server.models.user import User
from swagger_server.oxap.types.endpoint_interface_types import AppsuiteSOAP
from swagger_server.oxap.exceptions.context_exceptions import *
from swagger_server.oxap.models.oxap_account import OXAPAccount
from swagger_server.oxap.types.service_types import ContextService
from swagger_server.oxap.types.soap_types import SOAPStandard, SOAPReseller
from tornado.options import options
from zeep import Client
from zeep.cache import SqliteCache
from zeep.exceptions import Fault
from zeep.transports import Transport


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

    def change_context(self, context_id: str, context: Context):
        soap_context = self._get_oxsoap_context_object()

        soap_context_instance = soap_context()
        for key in context.attribute_map:
            if hasattr(context, key) \
                    and not isinstance(getattr(context, key), (Model)) \
                    and getattr(context, key) is not None:
                setattr(soap_context_instance, context.attribute_map[key], getattr(context, key))

        setattr(soap_context_instance, "id", context_id)

        try:
            return self.service.change(
                ctx=soap_context_instance,
                auth=self.credentials(
                    self.endpoint_interface.getLogin(),
                    self.endpoint_interface.getPassword()))
        except Fault as e:
            raise ContextException(e.message, e.detail)

    def create_context(self, context: Context, user: User):
        if self.endpoint_interface.getSOAPType() == SOAPReseller and context.name is None:
            raise Exception(
                "'name' is a required property during context creation on a reseller type SOAP interface")

        soap_context = self._get_oxsoap_context_object()
        soap_admin_user = self._get_oxsoap_user_object()
        soap_schema_select_strategy = self._get_oxsoap_schema_select_strategy_object()

        soap_context_instance = soap_context()
        for key in context.attribute_map:
            if hasattr(context, key) \
                    and not isinstance(getattr(context, key), (Model)) \
                    and getattr(context, key) is not None:
                setattr(soap_context_instance, context.attribute_map[key], getattr(context, key))

        soap_admin_user_instance = soap_admin_user()
        for key in user.attribute_map:
            if hasattr(user, key) \
                    and not isinstance(getattr(user, key), (Model)) \
                    and getattr(user, key) is not None:
                setattr(soap_admin_user_instance, user.attribute_map[key], getattr(user, key))

        soap_schema_select_strategy_instance = soap_schema_select_strategy()

        try:
            return self.service.create(
                ctx=soap_context_instance,
                admin_user=soap_admin_user_instance,
                auth=self.credentials(
                    self.endpoint_interface.getLogin(),
                    self.endpoint_interface.getPassword()),
                schema_select_strategy=soap_schema_select_strategy_instance)
        except Fault as e:
            raise ContextException(e.message, e.detail)

    def delete_context(self, context_id: str):
        soap_context = self._get_oxsoap_context_object()

        try:
            return self.service.delete(
                ctx=soap_context(id=context_id),
                auth=self.credentials(
                    self.endpoint_interface.getLogin(),
                    self.endpoint_interface.getPassword()))
        except Fault as e:
            raise ContextException(e.message, e.detail)

    def list_all_contexts(self):
        try:
            return self.service.listAll(self.credentials(
                self.endpoint_interface.getLogin(),
                self.endpoint_interface.getPassword()))
        except Fault as e:
            raise ContextException(e.message, e.detail)

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
