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
from xms_client.api.protection_domains_api import ProtectionDomainsApi  # noqa: E501
from xms_client.rest import ApiException


class TestProtectionDomainsApi(unittest.TestCase):
    """ProtectionDomainsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.protection_domains_api.ProtectionDomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_protection_domain(self):
        """Test case for get_protection_domain

        """
        pass

    def test_list_protection_domains(self):
        """Test case for list_protection_domains

        """
        pass


if __name__ == '__main__':
    unittest.main()