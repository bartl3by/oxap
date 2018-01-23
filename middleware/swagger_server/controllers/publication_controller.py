import connexion
import six

from swagger_server.models.publication import Publication
from swagger_server import util


def list_all_publications():
    """List all publications

    List all publications in given context


    :rtype: List[Publication]
    """
    return 'do some magic!'
