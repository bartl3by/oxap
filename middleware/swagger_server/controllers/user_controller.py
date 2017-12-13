import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def list_all_users():
    """
    List all users
    List all users in given context

    :rtype: List[User]
    """
    return 'do some magic!'
