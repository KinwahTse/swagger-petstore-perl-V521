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
from xms_client.api.vips_api import VipsApi  # noqa: E501
from xms_client.rest import ApiException


class TestVipsApi(unittest.TestCase):
    """VipsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.vips_api.VipsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_vip(self):
        """Test case for create_vip

        """
        pass

    def test_delete_vip(self):
        """Test case for delete_vip

        """
        pass

    def test_get_vip(self):
        """Test case for get_vip

        """
        pass

    def test_list_vi_ps(self):
        """Test case for list_vi_ps

        """
        pass

    def test_update_vip(self):
        """Test case for update_vip

        """
        pass


if __name__ == '__main__':
    unittest.main()
