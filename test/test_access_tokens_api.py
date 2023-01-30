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
from xms_client.api.access_tokens_api import AccessTokensApi  # noqa: E501
from xms_client.rest import ApiException


class TestAccessTokensApi(unittest.TestCase):
    """AccessTokensApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.access_tokens_api.AccessTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_access_token(self):
        """Test case for create_access_token

        """
        pass

    def test_delete_access_token(self):
        """Test case for delete_access_token

        """
        pass

    def test_get_access_token(self):
        """Test case for get_access_token

        """
        pass

    def test_list_access_tokens(self):
        """Test case for list_access_tokens

        """
        pass

    def test_regenerate_access_token(self):
        """Test case for regenerate_access_token

        """
        pass

    def test_update_access_token(self):
        """Test case for update_access_token

        """
        pass

    def test_validate_access_token(self):
        """Test case for validate_access_token

        """
        pass


if __name__ == '__main__':
    unittest.main()
