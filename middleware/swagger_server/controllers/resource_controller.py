import connexion
import six

from swagger_server.models.resource import Resource
from swagger_server import util


def change_resource(resource_id, resourceObject, Oxapsessionid=None):
    """Change a resource

    Change resource within the given context

    :param resource_id: Id of the resource object within the given context
    :type resource_id: int
    :param resourceObject: Resource object that needs to be updated within the given context
    :type resourceObject: dict | bytes
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = Resource.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_resource(resourceObject):
    """Create a new resource

    Creates a new resource within the given context

    :param resourceObject: Resource object that needs to be created within the given context
    :type resourceObject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resourceObject = Resource.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_resource(resource_id, Oxapsessionid=None):
    """Delete a resource

    Delete a resource within the given context

    :param resource_id: Id of the resource object within the given context
    :type resource_id: int
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: None
    """
    return 'do some magic!'


def find_resource_by_pattern(endpoint_id, search_pattern):
    """Find resource by pattern

    Find resource by pattern within the given context

    :param endpoint_id: Id of the OXAP endpoint for this OXAP account
    :type endpoint_id: str
    :param search_pattern: Pattern for the search request
    :type search_pattern: str

    :rtype: Resource
    """
    return 'do some magic!'


def get_resource_by_id(resource_id, Oxapsessionid=None):
    """Find resource by ID

    Find resource within the given context

    :param resource_id: Id of the resource object within the given context
    :type resource_id: int
    :param Oxapsessionid: Provide the session id previously acquired from /oxap/session. The session id can either be provided through this header parameter or as cookie (&#39;Oxapsessionid&#39;). If both, header and cookie will be send in a request, the cookie supersedes and will be used to verify the session.
    :type Oxapsessionid: str

    :rtype: Resource
    """
    return 'do some magic!'


def list_all_resources():
    """List all resources

    List all resources in given context


    :rtype: List[Resource]
    """
    return 'do some magic!'
