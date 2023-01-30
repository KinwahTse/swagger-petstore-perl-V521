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
from xms_client.api.alert_infos_api import AlertInfosApi  # noqa: E501
from xms_client.rest import ApiException


class TestAlertInfosApi(unittest.TestCase):
    """AlertInfosApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.alert_infos_api.AlertInfosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ack_alert_info(self):
        """Test case for ack_alert_info

        """
        pass

    def test_count_alert_infos(self):
        """Test case for count_alert_infos

        """
        pass

    def test_delete_alert_info(self):
        """Test case for delete_alert_info

        """
        pass

    def test_get_alert_info(self):
        """Test case for get_alert_info

        """
        pass

    def test_get_alert_infos_report(self):
        """Test case for get_alert_infos_report

        """
        pass

    def test_list_alert_infos(self):
        """Test case for list_alert_infos

        """
        pass

    def test_resolve_alert_info(self):
        """Test case for resolve_alert_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
