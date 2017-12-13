import connexion
from swagger_server.models.endpoint import Endpoint
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_endpoint_by_id(endpointId):
    """
    Find endpoint by ID
    Find endpoint within the given Open-Xchange Admin Panel account
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int

    :rtype: Endpoint
    """
    return 'do some magic!'


def get_oxap_account_endpoints():
    """
    Get all Endpoints
    Get all endpoints of the Open-Xchange Admin Panel account

    :rtype: List[Endpoint]
    """
    return 'do some magic!'
