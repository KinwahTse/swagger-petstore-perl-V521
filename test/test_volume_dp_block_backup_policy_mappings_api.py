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
from xms_client.api.volume_dp_block_backup_policy_mappings_api import VolumeDpBlockBackupPolicyMappingsApi  # noqa: E501
from xms_client.rest import ApiException


class TestVolumeDpBlockBackupPolicyMappingsApi(unittest.TestCase):
    """VolumeDpBlockBackupPolicyMappingsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.volume_dp_block_backup_policy_mappings_api.VolumeDpBlockBackupPolicyMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_volume_dp_block_backup_policy_mappings(self):
        """Test case for list_volume_dp_block_backup_policy_mappings

        """
        pass


if __name__ == '__main__':
    unittest.main()
