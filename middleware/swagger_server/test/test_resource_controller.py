# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.resource import Resource
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestResourceController(BaseTestCase):
    """ ResourceController integration test stubs """

    def test_create_resource(self):
        """
        Test case for create_resource

        Create a new resource
        """
        resourceObject = Resource()
        response = self.client.open('/v2/resource',
                                    method='POST',
                                    data=json.dumps(resourceObject),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_resource_by_pattern(self):
        """
        Test case for find_resource_by_pattern

        Find resource by pattern
        """
        query_string = [('pattern', 'pattern_example')]
        response = self.client.open('/v2/resource/find',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_list_all_resources(self):
        """
        Test case for list_all_resources

        List all resources
        """
        response = self.client.open('/v2/resource',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
