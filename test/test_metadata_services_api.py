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
from xms_client.api.metadata_services_api import MetadataServicesApi  # noqa: E501
from xms_client.rest import ApiException


class TestMetadataServicesApi(unittest.TestCase):
    """MetadataServicesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.metadata_services_api.MetadataServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metadata_service(self):
        """Test case for get_metadata_service

        """
        pass

    def test_get_metadata_service_samples(self):
        """Test case for get_metadata_service_samples

        """
        pass

    def test_list_metadata_services(self):
        """Test case for list_metadata_services

        """
        pass


if __name__ == '__main__':
    unittest.main()