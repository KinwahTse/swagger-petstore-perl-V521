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
from xms_client.api.action_logs_api import ActionLogsApi  # noqa: E501
from xms_client.rest import ApiException


class TestActionLogsApi(unittest.TestCase):
    """ActionLogsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.action_logs_api.ActionLogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_action_log(self):
        """Test case for get_action_log

        """
        pass

    def test_list_action_logs(self):
        """Test case for list_action_logs

        """
        pass


if __name__ == '__main__':
    unittest.main()
