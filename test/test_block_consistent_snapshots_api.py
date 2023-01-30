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
from xms_client.api.block_consistent_snapshots_api import BlockConsistentSnapshotsApi  # noqa: E501
from xms_client.rest import ApiException


class TestBlockConsistentSnapshotsApi(unittest.TestCase):
    """BlockConsistentSnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.block_consistent_snapshots_api.BlockConsistentSnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_block_consistent_snapshot(self):
        """Test case for create_block_consistent_snapshot

        """
        pass

    def test_delete_block_consistent_snapshot(self):
        """Test case for delete_block_consistent_snapshot

        """
        pass

    def test_get_block_consistent_snapshot(self):
        """Test case for get_block_consistent_snapshot

        """
        pass

    def test_list_block_consistent_snapshots(self):
        """Test case for list_block_consistent_snapshots

        """
        pass


if __name__ == '__main__':
    unittest.main()
