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
from xms_client.api.applications_api import ApplicationsApi  # noqa: E501
from xms_client.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application(self):
        """Test case for create_application

        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        """
        pass

    def test_list_applications(self):
        """Test case for list_applications

        """
        pass

    def test_update_application(self):
        """Test case for update_application

        """
        pass


if __name__ == '__main__':
    unittest.main()
