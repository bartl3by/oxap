#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import connexion

from swagger_server.models.endpoint import Endpoint
from swagger_server.models.endpoint_interface import EndpointInterface
from swagger_server.models.session import Session
from swagger_server.models.session_login import SessionLogin
from swagger_server.oxap import session_manager
from swagger_server.oxap.exceptions.authentication_exceptions import *
from swagger_server.oxap.exceptions.session_exceptions import *


def create_session(data):
    """Create an OXAP session

    Create an OXAP session. The endpoint_id parameter is mandatory for &#39;context&#39;, &#39;reseller&#39; and &#39;user&#39; login requests (set via &#39;role&#39;), a login request will fail if this parameter is not specified in case the role is &#39;context&#39;, &#39;reseller&#39; or &#39;user&#39;. OXAP accounts (role &#39;oxap&#39;) do not need to specify this value as a session grants them access to all their endpoints, endpoints will have to be specified during subsequent API requests to OXAP interfaces (like the manage context interface).

    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = SessionLogin.from_dict(connexion.request.get_json())

    try:
        session = session_manager.create_session(data.account_id, data.endpoint_id, data.role, data.username,
                                                 data.password)

        return session, 200
    except UnknownRoleException as e:
        logging.info('Failed login approach from %s with username %s',
                     connexion.request.headers['X-Forwarded-Host'],
                     data.username)
        return None, 400
    except AuthenticationException as e:
        logging.info('Error during authentication: %s', str(e))
        return None, 422


def delete_session(Oxapsessionid=None):
    """Delete an OXAP session

    Delete an OXAP session

    :param Oxapsessionid: The session id previously acquired from /oxap/session.
    :type Oxapsessionid: str

    :rtype: None
    """
    try:
        return (None, 200) if session_manager.delete_session() else (None, 400)
    except (ClientSessionIdMissingException, NoSuchSessionException) as e:
        return str(e), 401
    except SessionException as e:
        return str(e), 400


def get_endpoint_by_id(endpoint_id):
    """Find endpoint by ID

    Find endpoint within the given Open-Xchange Admin Panel account

    :param endpoint_id: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpoint_id: int

    :rtype: Endpoint
    """
    return 'do some magic!'


def get_endpoint_interface_by_id(endpoint_id, endpoint_interface_id):
    """Find endpoint interface by ID

    Find endpoint interface within the given Open-Xchange Admin Panel account endpoint

    :param endpoint_id: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpoint_id: int
    :param endpoint_interface_id: Id of the Open-Xchange Admin Panel account endpoint interface object to find within the given endpoint
    :type endpoint_interface_id: int

    :rtype: EndpointInterface
    """
    return 'do some magic!'


def get_oxap_account():
    """Get Account Information

    Get account information of the Open-Xchange Admin Panel account


    :rtype: None
    """
    return 'do some magic!'


def get_oxap_account_endpoint_interfaces(endpoint_id):
    """Get all interfaces

    Get all interfaces of an Open-Xchange Admin Panel account endpoint

    :param endpoint_id: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpoint_id: int

    :rtype: List[EndpointInterface]
    """
    return 'do some magic!'


def get_oxap_account_endpoints():
    """Get all Endpoints

    Get all endpoints of the Open-Xchange Admin Panel account


    :rtype: List[Endpoint]
    """
    return 'do some magic!'


def get_session_information(Oxapsessionid=None):
    """Refresh and get OXAP session information

    Refresh and get OXAP session information

    :param Oxapsessionid: The session id previously acquired from /oxap/session.
    :type Oxapsessionid: str

    :rtype: Session
    """
    try:
        return session_manager.get_session_information(True), 200
    except (ClientSessionIdMissingException, NoSuchSessionException) as e:
        return str(e), 401
    except SessionException as e:
        return str(e), 400
