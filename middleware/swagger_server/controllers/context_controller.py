import connexion
from swagger_server.models.context import Context
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from zeep import helpers, Client
import json
from swagger_server.oxap.soap_service_util import initiate_oxsoap_client, get_oxsoap_credentials_object, create_oxsoap_service, get_oxsoap_context_object, get_oxsoap_user_object, get_oxsoap_schema_select_strategy_object
from swagger_server.oxap.service_types import ContextService
import sys
from swagger_server.models.base_model_ import Model
from swagger_server.oxap.oxap_account import OXAPAccount
from swagger_server.oxap.endpoint_interface_types import AppsuiteSOAP
from swagger_server.oxap.endpoint_interface import EndpointInterface
import logging


def change_context(context_id: str, account_id: str, endpoint_id: str, payload: dict):
    """
    Change a context
    Change a context within an endpoint
    :param context_id: Id of the context object that needs to be changed within the given endpoint
    :type context_id: int
    :param account_id: Id of the OXAP account
    :type account_id: str
    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param payload: Context information that will be used to update the context within the given endpoint
    :type payload: dict | bytes

    :rtype: None
    """


def create_context(account_id: str, endpoint_id: str, payload: dict):
    """
    Create a new context
    Creates a new context within the given endpoint
    :param account_id: Id of the OXAP account
    :type account_id: str
    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param payload: Context object that needs to be created within the given endpoint
    :type payload: dict | bytes

    :rtype: Context
    """
    if connexion.request.is_json:
        context_object = Context.from_dict(connexion.request.get_json()['context'])
        user_object = User.from_dict(connexion.request.get_json()['user'])

    oxap_account = OXAPAccount(account_id)
    endpoint = oxap_account.getEndpoint(endpoint_id)
    endpoint_interface = oxap_account.getEndpointInterfaceByType(endpoint_id, AppsuiteSOAP())

    client = initiate_oxsoap_client(endpoint_interface, ContextService)
    service = create_oxsoap_service(client, endpoint_interface, ContextService)
    credentials = get_oxsoap_credentials_object(client, endpoint_interface.getSOAPType())
    soap_context = get_oxsoap_context_object(client, endpoint_interface.getSOAPType())
    soap_admin_user = get_oxsoap_user_object(client, endpoint_interface.getSOAPType())
    soap_schema_select_strategy = get_oxsoap_schema_select_strategy_object(client, endpoint_interface.getSOAPType())

    soap_context_instance = soap_context()
    for key in context_object.attribute_map:
        if hasattr(context_object, key) \
            and not isinstance(getattr(context_object, key), (Model)) \
            and getattr(context_object, key) is not None:
            setattr(soap_context_instance, context_object.attribute_map[key], getattr(context_object, key))

    soap_admin_user_instance = soap_admin_user()
    for key in user_object.attribute_map:
        if hasattr(user_object, key) \
            and not isinstance(getattr(user_object, key), (Model)) \
            and getattr(user_object, key) is not None:
            setattr(soap_admin_user_instance, user_object.attribute_map[key], getattr(user_object, key))

    try:
        soap_response = service.create(
            ctx=soap_context_instance,
            admin_user=soap_admin_user_instance,
            auth=credentials(
                endpoint_interface.getLogin(),
                endpoint_interface.getPassword()),
            schema_select_strategy=None)

        return json.loads(json.dumps(helpers.serialize_object(soap_response)))
    except Exception as e:
        return str(e), 405


def delete_context(context_id: str, account_id: str, endpoint_id: str):
    """
    Delete a context
    Delete a context within an endpoint
    :param context_id: Id of the context object that needs to be deleted within the given endpoint
    :type context_id: int
    :param account_id: Id of the OXAP account
    :type account_id: str
    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str

    :rtype: None
    """
    oxap_account = OXAPAccount(account_id)
    endpoint = oxap_account.getEndpoint(endpoint_id)
    endpoint_interface = oxap_account.getEndpointInterfaceByType(endpoint_id, AppsuiteSOAP())

    client = initiate_oxsoap_client(endpoint_interface, ContextService)
    service = create_oxsoap_service(client, endpoint_interface, ContextService)
    credentials = get_oxsoap_credentials_object(client, endpoint_interface.getSOAPType())

    try:
        soap_response = service.delete(
            ctx=soapContext(id=context_id),
            auth=credentials(
                endpoint_interface.getLogin(),
                endpoint_interface.getPassword()))

        logging.info(json.loads(json.dumps(helpers.serialize_object(soap_response))))
    except Exception as e:
        return str(e), 405


def list_all_contexts(account_id: str, endpoint_id: str):
    """
    List all contexts
    List all contexts in given context
    :param account_id: Id of the OXAP account
    :type account_id: str
    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str

    :rtype: List[Context]
    """
    oxap_account = OXAPAccount(account_id)
    endpoint = oxap_account.getEndpoint(endpoint_id)
    endpoint_interface = oxap_account.getEndpointInterfaceByType(endpoint_id, AppsuiteSOAP())

    client = initiate_oxsoap_client(endpoint_interface, ContextService)
    service = create_oxsoap_service(client, endpoint_interface, ContextService)
    credentials = get_oxsoap_credentials_object(client, endpoint_interface.getSOAPType())

    try:
        soap_response = service.listAll(credentials(
            endpoint_interface.getLogin(),
            endpoint_interface.getPassword()))

        return json.loads(json.dumps(helpers.serialize_object(soap_response)))
    except Exception as e:
        return str(e), 405
