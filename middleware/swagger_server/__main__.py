#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
from .configuration import define_configuration_options
import tornado
from tornado.options import define, options
import os
from tornado.log import enable_pretty_logging
import logging


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/', swagger_json=True, swagger_ui=True)
    app.app.json_encoder = JSONEncoder

    define_configuration_options()
    tornado.options.parse_command_line()
    tornado.options.parse_config_file(options.config_file)

    app.add_api('swagger.yaml', arguments={'title': 'This is the Open-Xchange Admin Panel API. This API is the connector to the middleware that handles provisioning tasks towards Open-Xchange products such as Dovecot or App Suite.'})
    app.run(server='tornado', port=options.server_port)
