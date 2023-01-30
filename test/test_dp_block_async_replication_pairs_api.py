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
from xms_client.api.dp_block_async_replication_pairs_api import DpBlockAsyncReplicationPairsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDpBlockAsyncReplicationPairsApi(unittest.TestCase):
    """DpBlockAsyncReplicationPairsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dp_block_async_replication_pairs_api.DpBlockAsyncReplicationPairsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_async_failover_dp_block_async_replication_pair(self):
        """Test case for async_failover_dp_block_async_replication_pair

        """
        pass

    def test_create_dp_block_async_replication_pair(self):
        """Test case for create_dp_block_async_replication_pair

        """
        pass

    def test_delete_dp_block_async_replication_pair(self):
        """Test case for delete_dp_block_async_replication_pair

        """
        pass

    def test_failback_dp_block_async_replication_pair(self):
        """Test case for failback_dp_block_async_replication_pair

        """
        pass

    def test_get_dp_block_async_replication_pair(self):
        """Test case for get_dp_block_async_replication_pair

        """
        pass

    def test_list_dp_block_async_replication_pair(self):
        """Test case for list_dp_block_async_replication_pair

        """
        pass

    def test_pause_dp_block_async_replication_pair(self):
        """Test case for pause_dp_block_async_replication_pair

        """
        pass

    def test_resume_dp_block_async_replication_pair(self):
        """Test case for resume_dp_block_async_replication_pair

        """
        pass

    def test_rollback_dp_block_async_replication_pair(self):
        """Test case for rollback_dp_block_async_replication_pair

        """
        pass

    def test_sync_dp_block_async_replication_pair(self):
        """Test case for sync_dp_block_async_replication_pair

        """
        pass

    def test_sync_failover_dp_block_async_replication_pair(self):
        """Test case for sync_failover_dp_block_async_replication_pair

        """
        pass

    def test_update_dp_block_async_replication_pair(self):
        """Test case for update_dp_block_async_replication_pair

        """
        pass


if __name__ == '__main__':
    unittest.main()