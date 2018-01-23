import connexion
import six

from swagger_server.models.user import User
from swagger_server import util


def list_all_users():
    """List all users

    List all users in given context


    :rtype: List[User]
    """
    return 'do some magic!'
