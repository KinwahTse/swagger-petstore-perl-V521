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
from xms_client.api.domain_user_validators_api import DomainUserValidatorsApi  # noqa: E501
from xms_client.rest import ApiException


class TestDomainUserValidatorsApi(unittest.TestCase):
    """DomainUserValidatorsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.domain_user_validators_api.DomainUserValidatorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_domain_user_validator(self):
        """Test case for create_domain_user_validator

        """
        pass

    def test_get_domain_user_validator(self):
        """Test case for get_domain_user_validator

        """
        pass


if __name__ == '__main__':
    unittest.main()
