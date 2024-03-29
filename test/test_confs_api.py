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
from xms_client.api.confs_api import ConfsApi  # noqa: E501
from xms_client.rest import ApiException


class TestConfsApi(unittest.TestCase):
    """ConfsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.confs_api.ConfsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_conf_item(self):
        """Test case for delete_conf_item

        """
        pass

    def test_get_conf_item(self):
        """Test case for get_conf_item

        """
        pass

    def test_list_conf_items(self):
        """Test case for list_conf_items

        """
        pass

    def test_list_conf_items_query(self):
        """Test case for list_conf_items_query

        """
        pass

    def test_set_conf_item(self):
        """Test case for set_conf_item

        """
        pass

    def test_set_conf_items(self):
        """Test case for set_conf_items

        """
        pass


if __name__ == '__main__':
    unittest.main()
