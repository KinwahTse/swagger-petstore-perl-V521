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
from xms_client.api.host_maintain_validators_api import HostMaintainValidatorsApi  # noqa: E501
from xms_client.rest import ApiException


class TestHostMaintainValidatorsApi(unittest.TestCase):
    """HostMaintainValidatorsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.host_maintain_validators_api.HostMaintainValidatorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_host_maintain_validator(self):
        """Test case for create_host_maintain_validator

        """
        pass

    def test_get_host_maintain_validator(self):
        """Test case for get_host_maintain_validator

        """
        pass


if __name__ == '__main__':
    unittest.main()
