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
from xms_client.api.alert_info_root_api import AlertInfoRootApi  # noqa: E501
from xms_client.rest import ApiException


class TestAlertInfoRootApi(unittest.TestCase):
    """AlertInfoRootApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.alert_info_root_api.AlertInfoRootApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ack_alert_info_root(self):
        """Test case for ack_alert_info_root

        """
        pass

    def test_get_alert_info_root(self):
        """Test case for get_alert_info_root

        """
        pass

    def test_resolve_alert_info_root(self):
        """Test case for resolve_alert_info_root

        """
        pass


if __name__ == '__main__':
    unittest.main()