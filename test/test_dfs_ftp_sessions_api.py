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
from xms_client.api.dfs_ftp_sessions_api import DfsFtpSessionsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDfsFtpSessionsApi(unittest.TestCase):
    """DfsFtpSessionsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.dfs_ftp_sessions_api.DfsFtpSessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_dfs_ftp_sessions(self):
        """Test case for list_dfs_ftp_sessions

        """
        pass


if __name__ == '__main__':
    unittest.main()
