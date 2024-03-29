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
from xms_client.api.pools_api import PoolsApi  # noqa: E501
from xms_client.rest import ApiException


class TestPoolsApi(unittest.TestCase):
    """PoolsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.pools_api.PoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_osds_to_pool(self):
        """Test case for add_osds_to_pool

        """
        pass

    def test_calc_capacity(self):
        """Test case for calc_capacity

        """
        pass

    def test_check_full(self):
        """Test case for check_full

        """
        pass

    def test_create_pool(self):
        """Test case for create_pool

        """
        pass

    def test_delete_pool(self):
        """Test case for delete_pool

        """
        pass

    def test_disable_pool_device_type_check(self):
        """Test case for disable_pool_device_type_check

        """
        pass

    def test_disable_pool_numa(self):
        """Test case for disable_pool_numa

        """
        pass

    def test_enable_pool_device_type_check(self):
        """Test case for enable_pool_device_type_check

        """
        pass

    def test_enable_pool_numa(self):
        """Test case for enable_pool_numa

        """
        pass

    def test_get_pool(self):
        """Test case for get_pool

        """
        pass

    def test_get_pool_predictions(self):
        """Test case for get_pool_predictions

        """
        pass

    def test_get_pool_samples(self):
        """Test case for get_pool_samples

        """
        pass

    def test_get_pool_topology(self):
        """Test case for get_pool_topology

        """
        pass

    def test_initialize_empty_pool(self):
        """Test case for initialize_empty_pool

        """
        pass

    def test_list_pools(self):
        """Test case for list_pools

        """
        pass

    def test_remove_osds_from_pool(self):
        """Test case for remove_osds_from_pool

        """
        pass

    def test_reweight_pool(self):
        """Test case for reweight_pool

        """
        pass

    def test_switch_pool_role(self):
        """Test case for switch_pool_role

        """
        pass

    def test_update_ec_pool_crush_rule(self):
        """Test case for update_ec_pool_crush_rule

        """
        pass

    def test_update_pool(self):
        """Test case for update_pool

        """
        pass

    def test_update_pool_gc_policy(self):
        """Test case for update_pool_gc_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()
