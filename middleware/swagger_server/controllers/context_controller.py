#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging

import connexion
from zeep import helpers

from swagger_server.models.context import Context
from swagger_server.models.context_create import ContextCreate
from swagger_server.oxap import session_manager
from swagger_server.oxap.exceptions.context_exceptions import *
from swagger_server.oxap.soap.context_soap_handler import ContextSOAPHandler
from swagger_server.oxap.types.service_types import ContextService


def change_context(endpoint_id, context_id, data, Oxapsessionid=None):
    """Change a context

    Change a context within an endpoint

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param context_id: Id of the context object within the given endpoint
    :type context_id: int
    :param data: Context information that will be used to update the context within the given endpoint
    :type data: dict | bytes
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: None
    """
    if connexion.request.is_json:
        context_object = Context.from_dict(connexion.request.get_json())

    session = session_manager.get_session_information()
    soap_handler = ContextSOAPHandler(session.account_id, endpoint_id, ContextService)

    try:
        logging.info(
            json.loads(json.dumps(helpers.serialize_object(soap_handler.change_context(context_id, context_object)))))
    except ContextExistsException as e:
        return str(e), 409
    except DatabaseUpdateException as e:
        return str(e), 409
    except DuplicateExtensionException as e:
        return str(e), 409
    except InvalidCredentialsException as e:
        return str(e), 401
    except InvalidDataException as e:
        return str(e), 406
    except NoSuchContextException as e:
        return str(e), 404
    except NoSuchDatabaseException as e:
        return str(e), 404
    except NoSuchFilestoreException as e:
        return str(e), 404
    except NoSuchReasonException as e:
        return str(e), 404
    except RemoteException as e:
        return str(e), 400
    except StorageException as e:
        return str(e), 409
    except ContextException as e:
        return str(e), 400


def create_context(endpoint_id, data, Oxapsessionid=None):
    """Create a new context

    Creates a new context within the given endpoint

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param data: 
    :type data: dict | bytes
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: Context
    """
    if connexion.request.is_json:
        data = ContextCreate.from_dict(connexion.request.get_json())
        context_object = data.context
        user_object = data.user

    session = session_manager.get_session_information()
    soap_handler = ContextSOAPHandler(session.account_id, endpoint_id, ContextService)

    try:
        return json.loads(
            json.dumps(helpers.serialize_object(soap_handler.create_context(context_object, user_object))))
    except ContextExistsException as e:
        return str(e), 409
    except DatabaseUpdateException as e:
        return str(e), 409
    except DuplicateExtensionException as e:
        return str(e), 409
    except InvalidCredentialsException as e:
        return str(e), 401
    except InvalidDataException as e:
        return str(e), 406
    except NoSuchDatabaseException as e:
        return str(e), 404
    except NoSuchFilestoreException as e:
        return str(e), 404
    except NoSuchReasonException as e:
        return str(e), 404
    except RemoteException as e:
        return str(e), 400
    except StorageException as e:
        return str(e), 409
    except ContextException as e:
        return str(e), 400


def delete_context(endpoint_id, context_id, Oxapsessionid=None):
    """Delete a context

    Delete a context within an endpoint

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param context_id: Id of the context object within the given endpoint
    :type context_id: int
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: None
    """
    session = session_manager.get_session_information()
    soap_handler = ContextSOAPHandler(session.account_id, endpoint_id, ContextService)

    try:
        logging.info(json.loads(json.dumps(helpers.serialize_object(soap_handler.delete_context(context_id)))))
    except ContextExistsException as e:
        return str(e), 409
    except DatabaseUpdateException as e:
        return str(e), 409
    except DuplicateExtensionException as e:
        return str(e), 409
    except InvalidCredentialsException as e:
        return str(e), 401
    except InvalidDataException as e:
        return str(e), 406
    except NoSuchContextException as e:
        return str(e), 404
    except NoSuchDatabaseException as e:
        return str(e), 404
    except NoSuchFilestoreException as e:
        return str(e), 404
    except NoSuchReasonException as e:
        return str(e), 404
    except RemoteException as e:
        return str(e), 400
    except StorageException as e:
        return str(e), 409
    except ContextException as e:
        return str(e), 400


def list_all_contexts(endpoint_id, Oxapsessionid=None):
    """List all contexts

    List all contexts in given context

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: List[Context]
    """
    session = session_manager.get_session_information()
    soap_handler = ContextSOAPHandler(session.account_id, endpoint_id, ContextService)

    try:
        return json.loads(json.dumps(helpers.serialize_object(soap_handler.list_all_contexts())))
    except ContextExistsException as e:
        return str(e), 409
    except DatabaseUpdateException as e:
        return str(e), 409
    except DuplicateExtensionException as e:
        return str(e), 409
    except InvalidCredentialsException as e:
        return str(e), 401
    except InvalidDataException as e:
        return str(e), 406
    except RemoteException as e:
        return str(e), 400
    except StorageException as e:
        return str(e), 409
    except ContextException as e:
        return str(e), 400
