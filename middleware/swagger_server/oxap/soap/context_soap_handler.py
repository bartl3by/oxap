#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zeep.exceptions import Fault

from swagger_server.models.base_model_ import Model
from swagger_server.models.context import Context
from swagger_server.models.user import User
from swagger_server.oxap.exceptions.context_exceptions import *
from swagger_server.oxap.soap.base_soap_handler import SOAPHandler
from swagger_server.oxap.types.soap_types import SOAPReseller


class ContextSOAPHandler(SOAPHandler):

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
