#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import connexion
from swagger_server.models.data import Data

from swagger_server.oxap import session_manager
from swagger_server.oxap.exceptions.session_exceptions import ClientSessionIdMissingException, \
    NoSuchSessionException, SessionException
from swagger_server.oxap.session_manager import cookie_name


def create_session(data):
    """
    Create an OXAP session
    Create an OXAP session
    :param data: Session Information
    :type data: dict | bytes

    :rtype: Session
    """
    if connexion.request.is_json:
        data = Data.from_dict(connexion.request.get_json())

    session = session_manager.create_session(data.account_id, data.endpoint_id, data.role, data.username, data.password)

    return session, 200, {
        'Set-Cookie': session.session_cookie_path + '=' + session.id + '; expires=' + session.expiration_date + '; path=/'
    }


def delete_session():
    """
    Refresh an OXAP session
    Refresh an OXAP session

    :rtype: None
    """
    try:
        session_manager.delete_session()

        return str(e), 200, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
    except ClientSessionIdMissingException as e:
        return str(e), 401
    except NoSuchSessionException as e:
        return str(e), 401, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
    except SessionException as e:
        return str(e), 400, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}


def get_endpoint_by_id(endpointId):
    """
    Find endpoint by ID
    Find endpoint within the given Open-Xchange Admin Panel account
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int

    :rtype: Endpoint
    """
    return 'do some magic!'


def get_endpoint_interface_by_id(endpointId, endpointInterfaceId):
    """
    Find endpoint interface by ID
    Find endpoint interface within the given Open-Xchange Admin Panel account endpoint
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int
    :param endpointInterfaceId: Id of the Open-Xchange Admin Panel account endpoint interface object to find within the given endpoint
    :type endpointInterfaceId: int

    :rtype: EndpointInterface
    """
    return 'do some magic!'


def get_oxap_account():
    """
    Get Account Information
    Get account information of the Open-Xchange Admin Panel account

    :rtype: None
    """
    return 'do some magic!'


def get_oxap_account_endpoint_interfaces(endpointId):
    """
    Get all interfaces
    Get all interfaces of an Open-Xchange Admin Panel account endpoint
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int

    :rtype: List[EndpointInterface]
    """
    return 'do some magic!'


def get_oxap_account_endpoints():
    """
    Get all Endpoints
    Get all endpoints of the Open-Xchange Admin Panel account

    :rtype: List[Endpoint]
    """
    return 'do some magic!'


def get_session_information():
    """
    Get OXAP session information
    Get OXAP session information

    :rtype: Session
    """
    try:
        session = session_manager.get_session_information(True)

        return session, 200, {
            'Set-Cookie': session.session_cookie_path + '=' + session.id + '; expires=' + session.expiration_date + '; path=/'
        }
    except ClientSessionIdMissingException as e:
        return str(e), 401
    except NoSuchSessionException as e:
        return str(e), 401, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
    except SessionException as e:
        return str(e), 400, {'Set-Cookie': cookie_name + '=deleted; expires=Thu, 01-Jan-1970 00:00:00 GMT'}
