#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import connexion
import tornado
from tornado.options import define, options

from swagger_server.oxap.exceptions.session_exceptions import ClientSessionIdMissingException, \
    NoSuchSessionException, SessionExpiredException, SessionException
from swagger_server.oxap.session_manager import method_has_scope, session_in_scope, get_method_scope
from swagger_server.resolver import SessionEnhancedResolver

from swagger_server.oxap.session_manager import cookie_name

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
                and getattr(connexion.request.url_rule, 'endpoint') is not None \
                and method_has_scope(connexion.request.url_rule.endpoint):
            try:
                if not session_in_scope(connexion.request.url_rule.endpoint, True):
                    return 'Requested interface requires role ' + get_method_scope, 403
            except ClientSessionIdMissingException as e:
                return str(e), 401
            except SessionExpiredException as e:
                return str(e), 401, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
            except NoSuchSessionException as e:
                return str(e), 401, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
            except SessionException as e:
                return str(e), 400, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}

    app.run(server='tornado', port=options.server_port)
