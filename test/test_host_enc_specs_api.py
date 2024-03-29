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
from xms_client.api.host_enc_specs_api import HostEncSpecsApi  # noqa: E501
from xms_client.rest import ApiException


class TestHostEncSpecsApi(unittest.TestCase):
    """HostEncSpecsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.host_enc_specs_api.HostEncSpecsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_host_enc_spec(self):
        """Test case for create_host_enc_spec

        """
        pass

    def test_delete_host_enc_spec(self):
        """Test case for delete_host_enc_spec

        """
        pass

    def test_get_host_enc_spec(self):
        """Test case for get_host_enc_spec

        """
        pass

    def test_list_host_enc_specs(self):
        """Test case for list_host_enc_specs

        """
        pass


if __name__ == '__main__':
    unittest.main()
