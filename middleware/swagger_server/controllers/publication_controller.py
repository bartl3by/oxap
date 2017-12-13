import connexion
from swagger_server.models.publication import Publication
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def list_all_publications():
    """
    List all publications
    List all publications in given context

    :rtype: List[Publication]
    """
    return 'do some magic!'
