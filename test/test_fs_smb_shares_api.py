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
from xms_client.api.fs_smb_shares_api import FsSmbSharesApi  # noqa: E501
from xms_client.rest import ApiException


class TestFsSmbSharesApi(unittest.TestCase):
    """FsSmbSharesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.fs_smb_shares_api.FsSmbSharesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_fssmb_share_ac_ls(self):
        """Test case for add_fssmb_share_ac_ls

        """
        pass

    def test_create_fssmb_share(self):
        """Test case for create_fssmb_share

        """
        pass

    def test_delete_fssmb_share(self):
        """Test case for delete_fssmb_share

        """
        pass

    def test_get_fssmb_share(self):
        """Test case for get_fssmb_share

        """
        pass

    def test_list_fssmb_shares(self):
        """Test case for list_fssmb_shares

        """
        pass

    def test_remove_fssmb_share_ac_ls(self):
        """Test case for remove_fssmb_share_ac_ls

        """
        pass

    def test_update_fssmb_share(self):
        """Test case for update_fssmb_share

        """
        pass

    def test_update_fssmb_share_ac_ls(self):
        """Test case for update_fssmb_share_ac_ls

        """
        pass


if __name__ == '__main__':
    unittest.main()
