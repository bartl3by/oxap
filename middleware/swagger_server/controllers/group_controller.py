import connexion
import six

from swagger_server.models.group import Group
from swagger_server import util


def list_all_groups():
    """List all groups

    List all groups in given context


    :rtype: List[Group]
    """
    return 'do some magic!'
