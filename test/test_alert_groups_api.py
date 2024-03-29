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
from xms_client.api.alert_groups_api import AlertGroupsApi  # noqa: E501
from xms_client.rest import ApiException


class TestAlertGroupsApi(unittest.TestCase):
    """AlertGroupsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.alert_groups_api.AlertGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_alert_group(self):
        """Test case for create_alert_group

        """
        pass

    def test_delete_alert_group(self):
        """Test case for delete_alert_group

        """
        pass

    def test_get_alert_group(self):
        """Test case for get_alert_group

        """
        pass

    def test_list_alert_groups(self):
        """Test case for list_alert_groups

        """
        pass

    def test_update_alert_group(self):
        """Test case for update_alert_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
