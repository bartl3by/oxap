import connexion
from swagger_server.models.context import Context
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from zeep import helpers, Client
from requests import Session
from zeep.transports import Transport
import json
from tornado.options import options
from ..oxsoap import get_context_path, initiate_client, get_credentials_object


def list_all_contexts():
    """
    List all contexts
    List all contexts in given context

    :rtype: List[Context]
    """

    response = []

    client = initiate_client(options.oxap_account_endpoint_type)
    credentials = get_credentials_object(client, options.oxap_account_endpoint_type)

    soapRequest = client.service.listAll(credentials(
        options.oxap_account_endpoint_soap_login,
        options.oxap_account_endpoint_soap_password))

    for current in soapRequest:
        serialized_dict = helpers.serialize_object(current)
        response.append(json.loads(json.dumps(serialized_dict)))

    return response
