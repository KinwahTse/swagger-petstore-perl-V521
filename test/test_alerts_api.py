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
from xms_client.api.alerts_api import AlertsApi  # noqa: E501
from xms_client.rest import ApiException


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.alerts_api.AlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_alerts(self):
        """Test case for count_alerts

        """
        pass

    def test_delete_alert(self):
        """Test case for delete_alert

        """
        pass

    def test_delete_alerts(self):
        """Test case for delete_alerts

        """
        pass

    def test_do_alert(self):
        """Test case for do_alert

        """
        pass

    def test_do_alerts(self):
        """Test case for do_alerts

        """
        pass

    def test_get_alert(self):
        """Test case for get_alert

        """
        pass

    def test_list_alerts(self):
        """Test case for list_alerts

        """
        pass

    def test_resolve_alert(self):
        """Test case for resolve_alert

        """
        pass

    def test_resolve_alerts(self):
        """Test case for resolve_alerts

        """
        pass


if __name__ == '__main__':
    unittest.main()
