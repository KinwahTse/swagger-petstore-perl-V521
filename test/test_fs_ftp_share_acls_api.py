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
from xms_client.api.fs_ftp_share_acls_api import FsFtpShareAclsApi  # noqa: E501
from xms_client.rest import ApiException


class TestFsFtpShareAclsApi(unittest.TestCase):
    """FsFtpShareAclsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.fs_ftp_share_acls_api.FsFtpShareAclsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_fsftp_share_ac_ls(self):
        """Test case for list_fsftp_share_ac_ls

        """
        pass


if __name__ == '__main__':
    unittest.main()
