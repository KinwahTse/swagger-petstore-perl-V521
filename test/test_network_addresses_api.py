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
from xms_client.api.network_addresses_api import NetworkAddressesApi  # noqa: E501
from xms_client.rest import ApiException


class TestNetworkAddressesApi(unittest.TestCase):
    """NetworkAddressesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.network_addresses_api.NetworkAddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_network_address(self):
        """Test case for get_network_address

        """
        pass

    def test_list_network_addresses(self):
        """Test case for list_network_addresses

        """
        pass


if __name__ == '__main__':
    unittest.main()
