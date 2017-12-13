# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.publication import Publication
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPublicationController(BaseTestCase):
    """ PublicationController integration test stubs """

    def test_list_all_publications(self):
        """
        Test case for list_all_publications

        List all publications
        """
        response = self.client.open('/v2/publication',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
