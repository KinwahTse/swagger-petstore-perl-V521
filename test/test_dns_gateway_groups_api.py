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
from xms_client.api.dns_gateway_groups_api import DnsGatewayGroupsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDnsGatewayGroupsApi(unittest.TestCase):
    """DnsGatewayGroupsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dns_gateway_groups_api.DnsGatewayGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_dns_gateway_to_group(self):
        """Test case for add_dns_gateway_to_group

        """
        pass

    def test_create_dns_gateway_group(self):
        """Test case for create_dns_gateway_group

        """
        pass

    def test_delete_dns_gateway_group(self):
        """Test case for delete_dns_gateway_group

        """
        pass

    def test_get_dns_gateway_group(self):
        """Test case for get_dns_gateway_group

        """
        pass

    def test_list_dns_gateway_groups(self):
        """Test case for list_dns_gateway_groups

        """
        pass

    def test_redeploy_dns_gateway_group(self):
        """Test case for redeploy_dns_gateway_group

        """
        pass

    def test_remove_dns_gateway_from_group(self):
        """Test case for remove_dns_gateway_from_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
