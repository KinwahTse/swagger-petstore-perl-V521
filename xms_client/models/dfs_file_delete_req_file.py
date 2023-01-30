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


class DfsFileDeleteReqFile(object):
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
        'dfs_rootfs_id': 'int',
        'path': 'str',
        'privileged_token': 'str'
    }

    attribute_map = {
        'dfs_rootfs_id': 'dfs_rootfs_id',
        'path': 'path',
        'privileged_token': 'privileged_token'
    }

    def __init__(self, dfs_rootfs_id=None, path=None, privileged_token=None):  # noqa: E501
        """DfsFileDeleteReqFile - a model defined in Swagger"""  # noqa: E501

        self._dfs_rootfs_id = None
        self._path = None
        self._privileged_token = None
        self.discriminator = None

        self.dfs_rootfs_id = dfs_rootfs_id
        self.path = path
        self.privileged_token = privileged_token

    @property
    def dfs_rootfs_id(self):
        """Gets the dfs_rootfs_id of this DfsFileDeleteReqFile.  # noqa: E501


        :return: The dfs_rootfs_id of this DfsFileDeleteReqFile.  # noqa: E501
        :rtype: int
        """
        return self._dfs_rootfs_id

    @dfs_rootfs_id.setter
    def dfs_rootfs_id(self, dfs_rootfs_id):
        """Sets the dfs_rootfs_id of this DfsFileDeleteReqFile.


        :param dfs_rootfs_id: The dfs_rootfs_id of this DfsFileDeleteReqFile.  # noqa: E501
        :type: int
        """
        if dfs_rootfs_id is None:
            raise ValueError("Invalid value for `dfs_rootfs_id`, must not be `None`")  # noqa: E501

        self._dfs_rootfs_id = dfs_rootfs_id

    @property
    def path(self):
        """Gets the path of this DfsFileDeleteReqFile.  # noqa: E501


        :return: The path of this DfsFileDeleteReqFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsFileDeleteReqFile.


        :param path: The path of this DfsFileDeleteReqFile.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def privileged_token(self):
        """Gets the privileged_token of this DfsFileDeleteReqFile.  # noqa: E501


        :return: The privileged_token of this DfsFileDeleteReqFile.  # noqa: E501
        :rtype: str
        """
        return self._privileged_token

    @privileged_token.setter
    def privileged_token(self, privileged_token):
        """Sets the privileged_token of this DfsFileDeleteReqFile.


        :param privileged_token: The privileged_token of this DfsFileDeleteReqFile.  # noqa: E501
        :type: str
        """
        if privileged_token is None:
            raise ValueError("Invalid value for `privileged_token`, must not be `None`")  # noqa: E501

        self._privileged_token = privileged_token

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
        if not isinstance(other, DfsFileDeleteReqFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
