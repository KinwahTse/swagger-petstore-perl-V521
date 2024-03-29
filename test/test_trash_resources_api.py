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
from xms_client.api.trash_resources_api import TrashResourcesApi  # noqa: E501
from xms_client.rest import ApiException


class TestTrashResourcesApi(unittest.TestCase):
    """TrashResourcesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.trash_resources_api.TrashResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_trash_resource(self):
        """Test case for delete_trash_resource

        """
        pass

    def test_get_trash_resource(self):
        """Test case for get_trash_resource

        """
        pass

    def test_list_trash_resources(self):
        """Test case for list_trash_resources

        """
        pass

    def test_restore_trash_resource(self):
        """Test case for restore_trash_resource

        """
        pass


if __name__ == '__main__':
    unittest.main()
