# coding: utf-8

"""
    XMS API

    XMS is the controller of distributed storage system  # noqa: E501

    OpenAPI spec version: XSCALEROS_5.2.100.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import xms_client
from xms_client.api.clients_api import ClientsApi  # noqa: E501
from xms_client.rest import ApiException


class TestClientsApi(unittest.TestCase):
    """ClientsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.clients_api.ClientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_client(self):
        """Test case for get_client

        """
        pass

    def test_list_clients(self):
        """Test case for list_clients

        """
        pass


if __name__ == '__main__':
    unittest.main()