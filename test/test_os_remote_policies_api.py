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
from xms_client.api.os_remote_policies_api import OsRemotePoliciesApi  # noqa: E501
from xms_client.rest import ApiException


class TestOsRemotePoliciesApi(unittest.TestCase):
    """OsRemotePoliciesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.os_remote_policies_api.OsRemotePoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_os_remote_policy(self):
        """Test case for get_os_remote_policy

        """
        pass

    def test_list_os_remote_policies(self):
        """Test case for list_os_remote_policies

        """
        pass


if __name__ == '__main__':
    unittest.main()
