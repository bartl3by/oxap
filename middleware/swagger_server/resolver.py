#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from connexion.apis import flask_utils
from connexion.resolver import Resolver

from swagger_server.oxap.session_manager import register_method_scope


class SessionEnhancedResolver(Resolver):

    def resolve_operation_id(self, operation):
        if 'x-security-scope' in operation.operation:
            security_scope = operation.operation.get('x-security-scope')

            base_path = operation.api.specification['basePath']
            endpoint_name = flask_utils.flaskify_endpoint(Resolver.resolve_operation_id(self, operation),
                                                          operation.randomize_endpoint)

            logging.debug('Registering scope \'' + str(security_scope) +
                          '\' for method ' + base_path + '.' + endpoint_name)
            register_method_scope(base_path + '.' + endpoint_name, security_scope)

        return Resolver.resolve_operation_id(self, operation)
