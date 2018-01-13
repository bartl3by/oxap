import connexion
from swagger_server.models.context import Context
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from zeep import helpers, Client
import json
from swagger_server.oxap.service_types import ContextService
from swagger_server.oxap.soap_handler import SOAPHandler
import logging
import sys


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
    if connexion.request.is_json:
        context_object = Context.from_dict(connexion.request.get_json())

    soap_handler = SOAPHandler(account_id, endpoint_id, ContextService)

    try:
        logging.info(json.loads(json.dumps(helpers.serialize_object(soap_handler.change_context(context_id, context_object)))))
    except Exception as e:
        logging.error(str(e))
        return str(e), 405


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

    soap_handler = SOAPHandler(account_id, endpoint_id, ContextService)

    try:
        return json.loads(json.dumps(helpers.serialize_object(soap_handler.create_context(context_object, user_object))))
    except Exception as e:
        logging.error(str(e))
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
    soap_handler = SOAPHandler(account_id, endpoint_id, ContextService)

    try:
        logging.info(json.loads(json.dumps(helpers.serialize_object(soap_handler.delete_context(context_id)))))
    except Exception as e:
        logging.error(str(e))
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
    soap_handler = SOAPHandler(account_id, endpoint_id, ContextService)

    try:
        return json.loads(json.dumps(helpers.serialize_object(soap_handler.list_all_contexts())))
    except Exception as e:
        logging.error(str(e))
        return str(e), 405
