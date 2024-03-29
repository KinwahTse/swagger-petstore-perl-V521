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
from xms_client.api.trashes_api import TrashesApi  # noqa: E501
from xms_client.rest import ApiException


class TestTrashesApi(unittest.TestCase):
    """TrashesApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.trashes_api.TrashesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cleanup_trash(self):
        """Test case for cleanup_trash

        """
        pass

    def test_get_trash(self):
        """Test case for get_trash

        """
        pass

    def test_list_trashes(self):
        """Test case for list_trashes

        """
        pass

    def test_update_trash(self):
        """Test case for update_trash

        """
        pass


if __name__ == '__main__':
    unittest.main()
