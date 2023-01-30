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
from xms_client.api.block_snapshots_api import BlockSnapshotsApi  # noqa: E501
from xms_client.rest import ApiException


class TestBlockSnapshotsApi(unittest.TestCase):
    """BlockSnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.block_snapshots_api.BlockSnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_block_snapshot(self):
        """Test case for create_block_snapshot

        """
        pass

    def test_delete_block_snapshot(self):
        """Test case for delete_block_snapshot

        """
        pass

    def test_get_block_snapshot(self):
        """Test case for get_block_snapshot

        """
        pass

    def test_list_block_snapshots(self):
        """Test case for list_block_snapshots

        """
        pass

    def test_update_snapshot(self):
        """Test case for update_snapshot

        """
        pass


if __name__ == '__main__':
    unittest.main()
