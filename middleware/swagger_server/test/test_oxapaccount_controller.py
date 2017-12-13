# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestOxapaccountController(BaseTestCase):
    """ OxapaccountController integration test stubs """

    def test_get_oxap_account(self):
        """
        Test case for get_oxap_account

        Get Account Information
        """
        response = self.client.open('/v2/oxap/account',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
