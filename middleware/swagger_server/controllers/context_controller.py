import connexion
from swagger_server.models.context import Context
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from zeep import helpers, Client
import json
from swagger_server.oxap.soap_service_util import get_context_path, initiate_client, get_credentials_object, create_service
from swagger_server.oxap.service_types import ContextService
import sys
from swagger_server.models.base_model_ import Model
from swagger_server.oxap.oxap_account import OXAPAccount
from swagger_server.oxap.endpoint_interface import EndpointInterface


def create_context(accountId, endpointId, contextObject):
    """
    Create a new context
    Creates a new context within the given endpoint
    :param accountId: Id of the OXAP account
    :type accountId: int
    :param endpointId: Id of the OXAP endpoint for this OXAP account
    :type endpointId: int
    :param contextObject: Context object that needs to be created within the given endpoint
    :type contextObject: dict | bytes

    :rtype: Context
    """
    if connexion.request.is_json:
        contextObject = Context.from_dict(connexion.request.get_json())

    oxapAccount = OXAPAccount(accountId)
    endpointInterface = oxapAccount.getEndpointInterface(endpointId)

    client = initiate_client(endpointInterface, ContextService)
    service = create_service(client, endpointInterface, ContextService)
    credentials = get_credentials_object(client, endpointInterface.getEndpointType())

    soapContext = client.get_type('ns4:ResellerContext')
    soapAdminUser = client.get_type('ns5:User')
    soapSchemaSelectStrategy = client.get_type('ns5:SchemaSelectStrategy')

    soapContextInstance = soapContext()
    for key in contextObject.attribute_map:
        if hasattr(contextObject, key) \
            and not isinstance(getattr(contextObject, key), (Model)) \
            and getattr(contextObject, key) is not None:
            setattr(soapContextInstance, contextObject.attribute_map[key], getattr(contextObject, key))

    soapAdminUserInstance = soapAdminUser()
    for key in contextObject.user.attribute_map:
        if hasattr(contextObject.user, key) \
            and not isinstance(getattr(contextObject.user, key), (Model)) \
            and getattr(contextObject.user, key) is not None:
            setattr(soapAdminUserInstance, contextObject.user.attribute_map[key], getattr(contextObject.user, key))

    try:
        soapResponse = service.create(
            ctx=soapContextInstance,
            admin_user=soapAdminUserInstance,
            auth=credentials(
                endpointInterface.getLogin(),
                endpointInterface.getPassword()),
            schema_select_strategy=None
                )

        return json.loads(json.dumps(helpers.serialize_object(soapResponse)))
    except Exception as e:
        return str(e), 405


def delete_context(contextId, accountId, endpointId):
    """
    Delete a context
    Delete a context within an endpoint
    :param contextId: Id of the context object that needs to be deleted within the given endpoint
    :type contextId: int
    :param accountId: Id of the OXAP account
    :type accountId: int
    :param endpointId: Id of the OXAP endpoint for this OXAP account
    :type endpointId: int

    :rtype: None
    """
    oxapAccount = OXAPAccount(accountId)
    endpointInterface = oxapAccount.getEndpointInterface(endpointId)

    client = initiate_client(endpointInterface, ContextService)
    service = create_service(client, endpointInterface, ContextService)
    credentials = get_credentials_object(client, endpointInterface.getEndpointType())

    soapContext = client.get_type('ns4:ResellerContext')

    try:
        soapResponse = service.delete(
            ctx=soapContext(id=contextId),
            auth=credentials(
                endpointInterface.getLogin(),
                endpointInterface.getPassword())
                )

        # replace with log, don't return
        return json.loads(json.dumps(helpers.serialize_object(soapResponse)))
    except Exception as e:
        return str(e), 405


def list_all_contexts(accountId, endpointId):
    """
    List all contexts
    List all contexts in given context
    :param accountId: Id of the OXAP account
    :type accountId: int
    :param endpointId: Id of the OXAP endpoint for this OXAP account
    :type endpointId: int

    :rtype: List[Context]
    """
    oxapAccount = OXAPAccount(accountId)
    endpointInterface = oxapAccount.getEndpointInterface(endpointId)

    client = initiate_client(endpointInterface, ContextService)
    service = create_service(client, endpointInterface, ContextService)
    credentials = get_credentials_object(client, endpointInterface.getEndpointType())

    try:
        soapResponse = service.listAll(credentials(
            endpointInterface.getLogin(),
            endpointInterface.getPassword()))

        return json.loads(json.dumps(helpers.serialize_object(soapResponse)))
    except Exception as e:
        return str(e), 405
