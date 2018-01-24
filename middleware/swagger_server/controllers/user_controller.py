import connexion
import six

from swagger_server.models.user import User
from swagger_server import util


def list_all_users(context_id, Oxapsessionid=None):
    """List all users

    List all users in given context

    :param context_id: Id of the context object within the given endpoint
    :type context_id: int
    :param Oxapsessionid: The session id previously acquired from /oxap/session.
    :type Oxapsessionid: str

    :rtype: List[User]
    """
    return 'do some magic!'
