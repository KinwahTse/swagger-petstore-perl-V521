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
from xms_client.api.fs_client_groups_api import FsClientGroupsApi  # noqa: E501
from xms_client.rest import ApiException


class TestFsClientGroupsApi(unittest.TestCase):
    """FsClientGroupsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.fs_client_groups_api.FsClientGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_fs_clients(self):
        """Test case for add_fs_clients

        """
        pass

    def test_create_fs_client_group(self):
        """Test case for create_fs_client_group

        """
        pass

    def test_delete_fs_client_group(self):
        """Test case for delete_fs_client_group

        """
        pass

    def test_get_fs_client_group(self):
        """Test case for get_fs_client_group

        """
        pass

    def test_list_fs_client_groups(self):
        """Test case for list_fs_client_groups

        """
        pass

    def test_remove_fs_clients(self):
        """Test case for remove_fs_clients

        """
        pass

    def test_update_fs_client_group(self):
        """Test case for update_fs_client_group

        """
        pass


if __name__ == '__main__':
    unittest.main()