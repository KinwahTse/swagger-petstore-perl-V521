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
from xms_client.api.fs_ldaps_api import FsLdapsApi  # noqa: E501
from xms_client.rest import ApiException


class TestFsLdapsApi(unittest.TestCase):
    """FsLdapsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.fs_ldaps_api.FsLdapsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_fs_ldap(self):
        """Test case for create_fs_ldap

        """
        pass

    def test_delete_fs_ldap(self):
        """Test case for delete_fs_ldap

        """
        pass

    def test_get_fs_ldap(self):
        """Test case for get_fs_ldap

        """
        pass

    def test_list_fs_ldaps(self):
        """Test case for list_fs_ldaps

        """
        pass

    def test_update_fs_ldap(self):
        """Test case for update_fs_ldap

        """
        pass

    def test_verify_fs_ldap(self):
        """Test case for verify_fs_ldap

        """
        pass


if __name__ == '__main__':
    unittest.main()