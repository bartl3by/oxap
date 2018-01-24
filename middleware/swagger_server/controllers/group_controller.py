#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from zeep import helpers

from swagger_server.oxap import session_manager
from swagger_server.oxap.exceptions.group_exceptions import *
from swagger_server.oxap.soap.base_soap_handler import SOAPHandler
from swagger_server.oxap.types.service_types import GroupService


def list_all_groups(endpoint_id, context_id, Oxapsessionid=None):
    """List all groups

    List all groups in given context

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param context_id: Id of the context object within the given endpoint
    :type context_id: int
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: List[Group]
    """
    session = session_manager.get_session_information()
    soap_handler = SOAPHandler(session.account_id, session.endpoint_id, GroupService)

    try:
        return json.loads(json.dumps(helpers.serialize_object(soap_handler.list_all_groups())))
    except GroupException as e:
        return str(e), 400
