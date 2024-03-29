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
from xms_client.api.identity_platforms_api import IdentityPlatformsApi  # noqa: E501
from xms_client.rest import ApiException


class TestIdentityPlatformsApi(unittest.TestCase):
    """IdentityPlatformsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.identity_platforms_api.IdentityPlatformsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_identity_platform(self):
        """Test case for create_identity_platform

        """
        pass

    def test_delete_identity_platform(self):
        """Test case for delete_identity_platform

        """
        pass

    def test_get_identity_platform(self):
        """Test case for get_identity_platform

        """
        pass

    def test_list_identity_platforms(self):
        """Test case for list_identity_platforms

        """
        pass

    def test_login_sso_types(self):
        """Test case for login_sso_types

        """
        pass

    def test_regenerate_identity_key(self):
        """Test case for regenerate_identity_key

        """
        pass

    def test_update_identity_platform(self):
        """Test case for update_identity_platform

        """
        pass


if __name__ == '__main__':
    unittest.main()
