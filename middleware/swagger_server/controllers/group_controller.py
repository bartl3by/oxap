import connexion
from swagger_server.models.group import Group
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def list_all_groups():
    """
    List all groups
    List all groups in given context

    :rtype: List[Group]
    """
    return 'do some magic!'
