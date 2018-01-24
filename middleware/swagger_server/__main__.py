#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import connexion
import tornado
from tornado.options import define, options

from swagger_server.oxap.exceptions.session_exceptions import ClientSessionIdMissingException, \
    NoSuchSessionException, SessionExpiredException, SessionException
from swagger_server.oxap.session_manager import session_in_scope, get_method_scope
from swagger_server.resolver import SessionEnhancedResolver

from .configuration import define_configuration_options
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/',
                             swagger_json=True, swagger_ui=True)
    app.app.json_encoder = JSONEncoder

    define_configuration_options()
    tornado.options.parse_command_line()
    tornado.options.parse_config_file(options.config_file)

    app.add_api('swagger.yaml',
                arguments={'title': 'This is the Open-Xchange Admin Panel API. This API is the '
                           'connector to the middleware that handles provisioning tasks '
                           'towards Open-Xchange products such as Dovecot or App Suite.'},
                resolver=SessionEnhancedResolver())

    @app.app.before_request
    def before_request():
        if hasattr(connexion.request.url_rule, 'endpoint') \
                and getattr(connexion.request.url_rule, 'endpoint') is not None:
            try:
                if not session_in_scope(connexion.request.url_rule.endpoint, True):
                    return 'Requested interface requires role ' + get_method_scope, 403
            except (ClientSessionIdMissingException,
                    SessionExpiredException,
                    NoSuchSessionException) as e:
                return str(e), 401
            except SessionException as e:
                return str(e), 400

    app.run(server='tornado', port=options.server_port)
