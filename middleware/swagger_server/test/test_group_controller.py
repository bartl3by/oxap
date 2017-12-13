# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.group import Group
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGroupController(BaseTestCase):
    """ GroupController integration test stubs """

    def test_list_all_groups(self):
        """
        Test case for list_all_groups

        List all groups
        """
        response = self.client.open('/v2/group',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
