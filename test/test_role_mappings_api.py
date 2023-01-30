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
from xms_client.api.role_mappings_api import RoleMappingsApi  # noqa: E501
from xms_client.rest import ApiException


class TestRoleMappingsApi(unittest.TestCase):
    """RoleMappingsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.role_mappings_api.RoleMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role_mapping(self):
        """Test case for create_role_mapping

        """
        pass

    def test_delete_role_mapping(self):
        """Test case for delete_role_mapping

        """
        pass

    def test_get_role_mapping(self):
        """Test case for get_role_mapping

        """
        pass

    def test_list_role_mappings(self):
        """Test case for list_role_mappings

        """
        pass

    def test_update_role_mapping(self):
        """Test case for update_role_mapping

        """
        pass


if __name__ == '__main__':
    unittest.main()
