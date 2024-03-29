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


class OSZoneLockCreateReqLock(object):
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
        'key': 'str',
        'resource_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'resource_type': 'resource_type',
        'value': 'value'
    }

    def __init__(self, key=None, resource_type=None, value=None):  # noqa: E501
        """OSZoneLockCreateReqLock - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._resource_type = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.resource_type = resource_type
        self.value = value

    @property
    def key(self):
        """Gets the key of this OSZoneLockCreateReqLock.  # noqa: E501

        key of lock, for example name of os bucket  # noqa: E501

        :return: The key of this OSZoneLockCreateReqLock.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this OSZoneLockCreateReqLock.

        key of lock, for example name of os bucket  # noqa: E501

        :param key: The key of this OSZoneLockCreateReqLock.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def resource_type(self):
        """Gets the resource_type of this OSZoneLockCreateReqLock.  # noqa: E501

        resource type of lock, including os_bucket  # noqa: E501

        :return: The resource_type of this OSZoneLockCreateReqLock.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this OSZoneLockCreateReqLock.

        resource type of lock, including os_bucket  # noqa: E501

        :param resource_type: The resource_type of this OSZoneLockCreateReqLock.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def value(self):
        """Gets the value of this OSZoneLockCreateReqLock.  # noqa: E501

        value of lock, for example action of os bucket  # noqa: E501

        :return: The value of this OSZoneLockCreateReqLock.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OSZoneLockCreateReqLock.

        value of lock, for example action of os bucket  # noqa: E501

        :param value: The value of this OSZoneLockCreateReqLock.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, OSZoneLockCreateReqLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
