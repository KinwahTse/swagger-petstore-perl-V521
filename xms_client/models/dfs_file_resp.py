# coding: utf-8

"""
    XMS API

    XMS is the controller of distributed storage system  # noqa: E501

    OpenAPI spec version: XSCALEROS_5.2.100.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401
import six

# from xms_client.models.dfs_file import DfsFile  # noqa: F401,E501


class DfsFileResp(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dfs_file': 'DfsFile'
    }

    attribute_map = {
        'dfs_file': 'dfs_file'
    }

    def __init__(self, dfs_file=None):  # noqa: E501
        """DfsFileResp - a model defined in Swagger"""  # noqa: E501

        self._dfs_file = None
        self.discriminator = None

        if dfs_file is not None:
            self.dfs_file = dfs_file

    @property
    def dfs_file(self):
        """Gets the dfs_file of this DfsFileResp.  # noqa: E501

        dfs file  # noqa: E501

        :return: The dfs_file of this DfsFileResp.  # noqa: E501
        :rtype: DfsFile
        """
        return self._dfs_file

    @dfs_file.setter
    def dfs_file(self, dfs_file):
        """Sets the dfs_file of this DfsFileResp.

        dfs file  # noqa: E501

        :param dfs_file: The dfs_file of this DfsFileResp.  # noqa: E501
        :type: DfsFile
        """

        self._dfs_file = dfs_file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DfsFileResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
