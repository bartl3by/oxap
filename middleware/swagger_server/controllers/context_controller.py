import connexion
from swagger_server.models.context import Context
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def list_all_contexts():
    """
    List all contexts
    List all contexts in given context

    :rtype: List[Context]
    """
    return 'do some magic!'
