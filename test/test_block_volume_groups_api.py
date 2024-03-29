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
from xms_client.api.block_volume_groups_api import BlockVolumeGroupsApi  # noqa: E501
from xms_client.rest import ApiException


class TestBlockVolumeGroupsApi(unittest.TestCase):
    """BlockVolumeGroupsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.block_volume_groups_api.BlockVolumeGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_block_volume_group(self):
        """Test case for create_block_volume_group

        """
        pass

    def test_delete_block_volume_group(self):
        """Test case for delete_block_volume_group

        """
        pass

    def test_get_block_volume_group(self):
        """Test case for get_block_volume_group

        """
        pass

    def test_list_block_volume_groups(self):
        """Test case for list_block_volume_groups

        """
        pass

    def test_rollback_volume_group(self):
        """Test case for rollback_volume_group

        """
        pass

    def test_set_volume_group_snapshot_replication_protection(self):
        """Test case for set_volume_group_snapshot_replication_protection

        """
        pass

    def test_unset_volume_group_snapshot_replication_protection(self):
        """Test case for unset_volume_group_snapshot_replication_protection

        """
        pass

    def test_update_block_volume_group(self):
        """Test case for update_block_volume_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
