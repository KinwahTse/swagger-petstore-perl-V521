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
from xms_client.api.osds_api import OsdsApi  # noqa: E501
from xms_client.rest import ApiException


class TestOsdsApi(unittest.TestCase):
    """OsdsApi unit test stubs"""

    def setUp(self):
        self.api = xms_client.api.osds_api.OsdsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_osd(self):
        """Test case for activate_osd

        """
        pass

    def test_create_osd(self):
        """Test case for create_osd

        """
        pass

    def test_delete_osd(self):
        """Test case for delete_osd

        """
        pass

    def test_get_chunks(self):
        """Test case for get_chunks

        """
        pass

    def test_get_osd(self):
        """Test case for get_osd

        """
        pass

    def test_get_osd_predictions(self):
        """Test case for get_osd_predictions

        """
        pass

    def test_get_osd_samples(self):
        """Test case for get_osd_samples

        """
        pass

    def test_list_osds(self):
        """Test case for list_osds

        """
        pass

    def test_maintain_osd(self):
        """Test case for maintain_osd

        """
        pass

    def test_rebuild_osd(self):
        """Test case for rebuild_osd

        """
        pass

    def test_switch_osd_role(self):
        """Test case for switch_osd_role

        """
        pass

    def test_unmaintain_osd(self):
        """Test case for unmaintain_osd

        """
        pass

    def test_unset_osd_isolation(self):
        """Test case for unset_osd_isolation

        """
        pass

    def test_update_osd_numa_node(self):
        """Test case for update_osd_numa_node

        """
        pass


if __name__ == '__main__':
    unittest.main()
