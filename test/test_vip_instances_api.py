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
from xms_client.api.vip_instances_api import VipInstancesApi  # noqa: E501
from xms_client.rest import ApiException


class TestVipInstancesApi(unittest.TestCase):
    """VipInstancesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.vip_instances_api.VipInstancesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_vip_instance(self):
        """Test case for get_vip_instance

        """
        pass

    def test_list_vip_instances(self):
        """Test case for list_vip_instances

        """
        pass


if __name__ == '__main__':
    unittest.main()
