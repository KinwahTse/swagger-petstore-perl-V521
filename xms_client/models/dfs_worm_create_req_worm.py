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


class DfsWormCreateReqWorm(object):
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
        'auto_lock_period': 'str',
        'default_protect_period': 'str',
        'max_protect_period': 'str',
        'min_protect_period': 'str',
        'path': 'str',
        'rootfs_id': 'int'
    }

    attribute_map = {
        'auto_lock_period': 'auto_lock_period',
        'default_protect_period': 'default_protect_period',
        'max_protect_period': 'max_protect_period',
        'min_protect_period': 'min_protect_period',
        'path': 'path',
        'rootfs_id': 'rootfs_id'
    }

    def __init__(self, auto_lock_period=None, default_protect_period=None, max_protect_period=None, min_protect_period=None, path=None, rootfs_id=None):  # noqa: E501
        """DfsWormCreateReqWorm - a model defined in Swagger"""  # noqa: E501

        self._auto_lock_period = None
        self._default_protect_period = None
        self._max_protect_period = None
        self._min_protect_period = None
        self._path = None
        self._rootfs_id = None
        self.discriminator = None

        self.auto_lock_period = auto_lock_period
        self.default_protect_period = default_protect_period
        self.max_protect_period = max_protect_period
        self.min_protect_period = min_protect_period
        self.path = path
        self.rootfs_id = rootfs_id

    @property
    def auto_lock_period(self):
        """Gets the auto_lock_period of this DfsWormCreateReqWorm.  # noqa: E501

        automatic locking period  # noqa: E501

        :return: The auto_lock_period of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: str
        """
        return self._auto_lock_period

    @auto_lock_period.setter
    def auto_lock_period(self, auto_lock_period):
        """Sets the auto_lock_period of this DfsWormCreateReqWorm.

        automatic locking period  # noqa: E501

        :param auto_lock_period: The auto_lock_period of this DfsWormCreateReqWorm.  # noqa: E501
        :type: str
        """
        if auto_lock_period is None:
            raise ValueError("Invalid value for `auto_lock_period`, must not be `None`")  # noqa: E501

        self._auto_lock_period = auto_lock_period

    @property
    def default_protect_period(self):
        """Gets the default_protect_period of this DfsWormCreateReqWorm.  # noqa: E501

        default protect period  # noqa: E501

        :return: The default_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: str
        """
        return self._default_protect_period

    @default_protect_period.setter
    def default_protect_period(self, default_protect_period):
        """Sets the default_protect_period of this DfsWormCreateReqWorm.

        default protect period  # noqa: E501

        :param default_protect_period: The default_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :type: str
        """
        if default_protect_period is None:
            raise ValueError("Invalid value for `default_protect_period`, must not be `None`")  # noqa: E501

        self._default_protect_period = default_protect_period

    @property
    def max_protect_period(self):
        """Gets the max_protect_period of this DfsWormCreateReqWorm.  # noqa: E501

        maximum protect period  # noqa: E501

        :return: The max_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: str
        """
        return self._max_protect_period

    @max_protect_period.setter
    def max_protect_period(self, max_protect_period):
        """Sets the max_protect_period of this DfsWormCreateReqWorm.

        maximum protect period  # noqa: E501

        :param max_protect_period: The max_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :type: str
        """
        if max_protect_period is None:
            raise ValueError("Invalid value for `max_protect_period`, must not be `None`")  # noqa: E501

        self._max_protect_period = max_protect_period

    @property
    def min_protect_period(self):
        """Gets the min_protect_period of this DfsWormCreateReqWorm.  # noqa: E501

        minimum protect period  # noqa: E501

        :return: The min_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: str
        """
        return self._min_protect_period

    @min_protect_period.setter
    def min_protect_period(self, min_protect_period):
        """Sets the min_protect_period of this DfsWormCreateReqWorm.

        minimum protect period  # noqa: E501

        :param min_protect_period: The min_protect_period of this DfsWormCreateReqWorm.  # noqa: E501
        :type: str
        """
        if min_protect_period is None:
            raise ValueError("Invalid value for `min_protect_period`, must not be `None`")  # noqa: E501

        self._min_protect_period = min_protect_period

    @property
    def path(self):
        """Gets the path of this DfsWormCreateReqWorm.  # noqa: E501

        worm root path  # noqa: E501

        :return: The path of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsWormCreateReqWorm.

        worm root path  # noqa: E501

        :param path: The path of this DfsWormCreateReqWorm.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def rootfs_id(self):
        """Gets the rootfs_id of this DfsWormCreateReqWorm.  # noqa: E501

        id of dfs rootfs  # noqa: E501

        :return: The rootfs_id of this DfsWormCreateReqWorm.  # noqa: E501
        :rtype: int
        """
        return self._rootfs_id

    @rootfs_id.setter
    def rootfs_id(self, rootfs_id):
        """Sets the rootfs_id of this DfsWormCreateReqWorm.

        id of dfs rootfs  # noqa: E501

        :param rootfs_id: The rootfs_id of this DfsWormCreateReqWorm.  # noqa: E501
        :type: int
        """
        if rootfs_id is None:
            raise ValueError("Invalid value for `rootfs_id`, must not be `None`")  # noqa: E501

        self._rootfs_id = rootfs_id

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
        if not isinstance(other, DfsWormCreateReqWorm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other