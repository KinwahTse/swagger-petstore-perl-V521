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


class DfsDirectoryReqDirectory(object):
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
        'clean': 'bool',
        'dfs_rootfs_id': 'int',
        'path': 'str'
    }

    attribute_map = {
        'clean': 'clean',
        'dfs_rootfs_id': 'dfs_rootfs_id',
        'path': 'path'
    }

    def __init__(self, clean=None, dfs_rootfs_id=None, path=None):  # noqa: E501
        """DfsDirectoryReqDirectory - a model defined in Swagger"""  # noqa: E501

        self._clean = None
        self._dfs_rootfs_id = None
        self._path = None
        self.discriminator = None

        if clean is not None:
            self.clean = clean
        self.dfs_rootfs_id = dfs_rootfs_id
        self.path = path

    @property
    def clean(self):
        """Gets the clean of this DfsDirectoryReqDirectory.  # noqa: E501

        clean resources on empty dir  # noqa: E501

        :return: The clean of this DfsDirectoryReqDirectory.  # noqa: E501
        :rtype: bool
        """
        return self._clean

    @clean.setter
    def clean(self, clean):
        """Sets the clean of this DfsDirectoryReqDirectory.

        clean resources on empty dir  # noqa: E501

        :param clean: The clean of this DfsDirectoryReqDirectory.  # noqa: E501
        :type: bool
        """

        self._clean = clean

    @property
    def dfs_rootfs_id(self):
        """Gets the dfs_rootfs_id of this DfsDirectoryReqDirectory.  # noqa: E501

        dfs rootfs id  # noqa: E501

        :return: The dfs_rootfs_id of this DfsDirectoryReqDirectory.  # noqa: E501
        :rtype: int
        """
        return self._dfs_rootfs_id

    @dfs_rootfs_id.setter
    def dfs_rootfs_id(self, dfs_rootfs_id):
        """Sets the dfs_rootfs_id of this DfsDirectoryReqDirectory.

        dfs rootfs id  # noqa: E501

        :param dfs_rootfs_id: The dfs_rootfs_id of this DfsDirectoryReqDirectory.  # noqa: E501
        :type: int
        """
        if dfs_rootfs_id is None:
            raise ValueError("Invalid value for `dfs_rootfs_id`, must not be `None`")  # noqa: E501

        self._dfs_rootfs_id = dfs_rootfs_id

    @property
    def path(self):
        """Gets the path of this DfsDirectoryReqDirectory.  # noqa: E501

        directory path  # noqa: E501

        :return: The path of this DfsDirectoryReqDirectory.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsDirectoryReqDirectory.

        directory path  # noqa: E501

        :param path: The path of this DfsDirectoryReqDirectory.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, DfsDirectoryReqDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
