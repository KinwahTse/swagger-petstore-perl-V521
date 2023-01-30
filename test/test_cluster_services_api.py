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
from xms_client.api.cluster_services_api import ClusterServicesApi  # noqa: E501
from xms_client.rest import ApiException


class TestClusterServicesApi(unittest.TestCase):
    """ClusterServicesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.cluster_services_api.ClusterServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cluster_service(self):
        """Test case for get_cluster_service

        """
        pass

    def test_list_cluster_services(self):
        """Test case for list_cluster_services

        """
        pass

    def test_rebuild_cluster_service(self):
        """Test case for rebuild_cluster_service

        """
        pass

    def test_reindex_docs(self):
        """Test case for reindex_docs

        """
        pass


if __name__ == '__main__':
    unittest.main()