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
from xms_client.api.domain_user_groups_api import DomainUserGroupsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDomainUserGroupsApi(unittest.TestCase):
    """DomainUserGroupsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.domain_user_groups_api.DomainUserGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_domain_user_group(self):
        """Test case for delete_domain_user_group

        """
        pass

    def test_list_domain_user_groups(self):
        """Test case for list_domain_user_groups

        """
        pass


if __name__ == '__main__':
    unittest.main()
