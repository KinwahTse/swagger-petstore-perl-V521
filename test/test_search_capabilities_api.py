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
from xms_client.api.search_capabilities_api import SearchCapabilitiesApi  # noqa: E501
from xms_client.rest import ApiException


class TestSearchCapabilitiesApi(unittest.TestCase):
    """SearchCapabilitiesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.search_capabilities_api.SearchCapabilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_capabilites(self):
        """Test case for search_capabilites

        """
        pass


if __name__ == '__main__':
    unittest.main()
