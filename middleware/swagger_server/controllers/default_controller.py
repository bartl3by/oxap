import connexion
from swagger_server.models.endpoint import Endpoint
from swagger_server.models.endpoint_interface import EndpointInterface
from swagger_server.models.publication import Publication
from swagger_server.models.resource import Resource
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def change_endpoint(endpointId, endpointObject):
    """
    Change an endpoint
    Change an endpoint within the given Open-Xchange Admin Panel account endpoint
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int
    :param endpointObject: Endpoint object that needs to be updated within the given Open-Xchange Admin Panel account endpoint
    :type endpointObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        endpointObject = EndpointInterface.from_dict(connexion.request.get_json())
    return 'do some magic!'


def change_endpointinterface(endpointId, endpointInterfaceId, resourceObject):
    """
    Change an endpoint interface
    Change an endpoint interface within the given Open-Xchange Admin Panel account endpoint
    :param endpointId: Id of the Open-Xchange Admin Panel Account endpoint object to find within the given account
    :type endpointId: int
    :param endpointInterfaceId: Id of the Open-Xchange Admin Panel account endpoint interface object to find within the given endpoint
    :type endpointInterfaceId: int
    :param resourceObject: Endpoint interface object that needs to be updated within the given Open-Xchange Admin Panel account endpoint
    :type resourceObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = EndpointInterface.from_dict(connexion.request.get_json())
    return 'do some magic!'


def change_resource(resourceId, resourceObject):
    """
    Change a resource
    Change resource within the given context
    :param resourceId: Id of the resource object to find within the given context
    :type resourceId: int
    :param resourceObject: Resource object that needs to be updated within the given context
    :type resourceObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = Resource.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_endpointinterface(endpointInterface):
    """
    Create a new endpoint interface
    Creates a new endpoint interface within the given Open-Xchange Admin Panel account endpoint
    :param endpointInterface: Endpoint Interface object that needs to be created within the given Open-Xchange Admin Panel account endpoint
    :type endpointInterface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        endpointInterface = EndpointInterface.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_resource(resourceId):
    """
    Delete a resource
    Delete a resource within the given context
    :param resourceId: Id of the resource object to find within the given context
    :type resourceId: int

    :rtype: None
    """
    return 'do some magic!'


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


def get_resource_by_id(resourceId):
    """
    Find resource by ID
    Find resource within the given context
    :param resourceId: Id of the resource object to find within the given context
    :type resourceId: int

    :rtype: Resource
    """
    return 'do some magic!'


def list_all_publications():
    """
    List all publications
    List all publications in given context

    :rtype: List[Publication]
    """
    return 'do some magic!'
