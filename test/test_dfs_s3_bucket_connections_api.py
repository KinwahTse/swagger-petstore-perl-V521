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
from xms_client.api.dfs_s3_bucket_connections_api import DfsS3BucketConnectionsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDfsS3BucketConnectionsApi(unittest.TestCase):
    """DfsS3BucketConnectionsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dfs_s3_bucket_connections_api.DfsS3BucketConnectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_dfs_s3_bucket_connections(self):
        """Test case for list_dfs_s3_bucket_connections

        """
        pass


if __name__ == '__main__':
    unittest.main()
