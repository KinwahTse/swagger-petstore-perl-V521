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
from xms_client.api.dp_volume_group_snapshot_replication_jobs_api import DpVolumeGroupSnapshotReplicationJobsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDpVolumeGroupSnapshotReplicationJobsApi(unittest.TestCase):
    """DpVolumeGroupSnapshotReplicationJobsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dp_volume_group_snapshot_replication_jobs_api.DpVolumeGroupSnapshotReplicationJobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_dp_volume_group_snapshot_replication_job(self):
        """Test case for delete_dp_volume_group_snapshot_replication_job

        """
        pass

    def test_get_dp_volume_group_snapshot_replication_job(self):
        """Test case for get_dp_volume_group_snapshot_replication_job

        """
        pass

    def test_list_dp_volume_group_snapshot_replication_job(self):
        """Test case for list_dp_volume_group_snapshot_replication_job

        """
        pass


if __name__ == '__main__':
    unittest.main()
