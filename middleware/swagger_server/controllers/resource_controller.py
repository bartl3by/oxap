import connexion
from swagger_server.models.resource import Resource
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def change_resource(resourceId, resourceObject):
    """
    Change a resource
    Change resource within the given context
    :param resourceId: Id of the resource object that needs to be updated within the given context
    :type resourceId: int
    :param resourceObject: Resource object that needs to be updated within the given context
    :type resourceObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = Resource.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_resource(resourceObject):
    """
    Create a new resource
    Creates a new resource within the given context
    :param resourceObject: Resource object that needs to be created within the given context
    :type resourceObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = Resource.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_resource(resourceId):
    """
    Delete a resource
    Delete a resource within the given context
    :param resourceId: Id of the resource object that needs to be deleted within the given context
    :type resourceId: int

    :rtype: None
    """
    return 'do some magic!'


def find_resource_by_pattern(pattern):
    """
    Find resource by pattern
    Find resource by pattern within the given context
    :param pattern: Pattern of the resource object to find within the given context
    :type pattern: str

    :rtype: Resource
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


def list_all_resources():
    """
    List all resources
    List all resources in given context

    :rtype: List[Resource]
    """
    return 'do some magic!'
