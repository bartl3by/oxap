#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/', swagger_json=True, swagger_ui=True)
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'This is the Open-Xchange Admin Panel API. This API is the connector to the middleware that handles provisioning tasks towards Open-Xchange products such as Dovecot or App Suite.'})
    app.run(server='tornado', port=8080)
