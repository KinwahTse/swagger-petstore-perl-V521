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
from xms_client.api.cluster_api import ClusterApi  # noqa: E501
from xms_client.rest import ApiException


class TestClusterApi(unittest.TestCase):
    """ClusterApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.cluster_api.ClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boot_node(self):
        """Test case for boot_node

        """
        pass

    def test_cluster(self):
        """Test case for cluster

        """
        pass

    def test_commit_master_switching(self):
        """Test case for commit_master_switching

        """
        pass

    def test_delete_object_storage(self):
        """Test case for delete_object_storage

        """
        pass

    def test_download(self):
        """Test case for download

        """
        pass

    def test_enable_multi_zone(self):
        """Test case for enable_multi_zone

        """
        pass

    def test_get_action_log_report(self):
        """Test case for get_action_log_report

        """
        pass

    def test_get_alert_report(self):
        """Test case for get_alert_report

        """
        pass

    def test_get_cluster_overview(self):
        """Test case for get_cluster_overview

        """
        pass

    def test_get_cluster_report(self):
        """Test case for get_cluster_report

        """
        pass

    def test_get_cluster_samples(self):
        """Test case for get_cluster_samples

        """
        pass

    def test_get_event_log_report(self):
        """Test case for get_event_log_report

        """
        pass

    def test_get_object_storage(self):
        """Test case for get_object_storage

        """
        pass

    def test_get_object_storage_samples(self):
        """Test case for get_object_storage_samples

        """
        pass

    def test_get_stats_usage_prediction(self):
        """Test case for get_stats_usage_prediction

        """
        pass

    def test_init_object_storage(self):
        """Test case for init_object_storage

        """
        pass

    def test_installation(self):
        """Test case for installation

        """
        pass

    def test_prepare_master_switching(self):
        """Test case for prepare_master_switching

        """
        pass

    def test_remove_cluster_access_info(self):
        """Test case for remove_cluster_access_info

        """
        pass

    def test_rollback_master_switching(self):
        """Test case for rollback_master_switching

        """
        pass

    def test_server_time(self):
        """Test case for server_time

        """
        pass

    def test_set_boot_node(self):
        """Test case for set_boot_node

        """
        pass

    def test_set_cluster_access_info(self):
        """Test case for set_cluster_access_info

        """
        pass

    def test_set_cluster_network(self):
        """Test case for set_cluster_network

        """
        pass

    def test_set_object_storage(self):
        """Test case for set_object_storage

        """
        pass

    def test_set_object_storage_dns_names(self):
        """Test case for set_object_storage_dns_names

        """
        pass

    def test_set_object_storage_origin_pull_hosts(self):
        """Test case for set_object_storage_origin_pull_hosts

        """
        pass

    def test_set_object_storage_tiering_hosts(self):
        """Test case for set_object_storage_tiering_hosts

        """
        pass

    def test_switch_os_zone_to_master(self):
        """Test case for switch_os_zone_to_master

        """
        pass

    def test_update_cluster(self):
        """Test case for update_cluster

        """
        pass

    def test_update_cluster_maintenance(self):
        """Test case for update_cluster_maintenance

        """
        pass


if __name__ == '__main__':
    unittest.main()
