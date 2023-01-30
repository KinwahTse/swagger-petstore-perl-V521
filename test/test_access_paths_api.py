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
from xms_client.api.access_paths_api import AccessPathsApi  # noqa: E501
from xms_client.rest import ApiException


class TestAccessPathsApi(unittest.TestCase):
    """AccessPathsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.access_paths_api.AccessPathsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_access_path(self):
        """Test case for create_access_path

        """
        pass

    def test_delete_access_path(self):
        """Test case for delete_access_path

        """
        pass

    def test_get_access_path(self):
        """Test case for get_access_path

        """
        pass

    def test_list_access_paths(self):
        """Test case for list_access_paths

        """
        pass

    def test_update_access_path(self):
        """Test case for update_access_path

        """
        pass


if __name__ == '__main__':
    unittest.main()
