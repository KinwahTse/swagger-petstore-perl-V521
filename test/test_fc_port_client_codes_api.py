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
from xms_client.api.fc_port_client_codes_api import FcPortClientCodesApi  # noqa: E501
from xms_client.rest import ApiException


class TestFcPortClientCodesApi(unittest.TestCase):
    """FcPortClientCodesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.fc_port_client_codes_api.FcPortClientCodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_fc_port_client_codes(self):
        """Test case for list_fc_port_client_codes

        """
        pass


if __name__ == '__main__':
    unittest.main()