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
from xms_client.api.dfs_s3_buckets_api import DfsS3BucketsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDfsS3BucketsApi(unittest.TestCase):
    """DfsS3BucketsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dfs_s3_buckets_api.DfsS3BucketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dfs_s3_bucket(self):
        """Test case for create_dfs_s3_bucket

        """
        pass

    def test_delete_dfs_s3_bucket(self):
        """Test case for delete_dfs_s3_bucket

        """
        pass

    def test_delete_dfs_s3_bucket_policy(self):
        """Test case for delete_dfs_s3_bucket_policy

        """
        pass

    def test_get_dfs_s3_bucket(self):
        """Test case for get_dfs_s3_bucket

        """
        pass

    def test_get_dfs_s3_bucket_samples(self):
        """Test case for get_dfs_s3_bucket_samples

        """
        pass

    def test_list_dfs_s3_buckets(self):
        """Test case for list_dfs_s3_buckets

        """
        pass

    def test_set_dfs_s3_bucket_policy(self):
        """Test case for set_dfs_s3_bucket_policy

        """
        pass

    def test_update_dfs_s3_bucket(self):
        """Test case for update_dfs_s3_bucket

        """
        pass


if __name__ == '__main__':
    unittest.main()