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


class UsedQuota(object):
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
        'used_capacity': 'int',
        'used_hdd_capacity': 'int',
        'used_host_num': 'int',
        'used_ssd_capacity': 'int'
    }

    attribute_map = {
        'used_capacity': 'used_capacity',
        'used_hdd_capacity': 'used_hdd_capacity',
        'used_host_num': 'used_host_num',
        'used_ssd_capacity': 'used_ssd_capacity'
    }

    def __init__(self, used_capacity=None, used_hdd_capacity=None, used_host_num=None, used_ssd_capacity=None):  # noqa: E501
        """UsedQuota - a model defined in Swagger"""  # noqa: E501

        self._used_capacity = None
        self._used_hdd_capacity = None
        self._used_host_num = None
        self._used_ssd_capacity = None
        self.discriminator = None

        self.used_capacity = used_capacity
        self.used_hdd_capacity = used_hdd_capacity
        self.used_host_num = used_host_num
        self.used_ssd_capacity = used_ssd_capacity

    @property
    def used_capacity(self):
        """Gets the used_capacity of this UsedQuota.  # noqa: E501


        :return: The used_capacity of this UsedQuota.  # noqa: E501
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        """Sets the used_capacity of this UsedQuota.


        :param used_capacity: The used_capacity of this UsedQuota.  # noqa: E501
        :type: int
        """
        if used_capacity is None:
            raise ValueError("Invalid value for `used_capacity`, must not be `None`")  # noqa: E501

        self._used_capacity = used_capacity

    @property
    def used_hdd_capacity(self):
        """Gets the used_hdd_capacity of this UsedQuota.  # noqa: E501


        :return: The used_hdd_capacity of this UsedQuota.  # noqa: E501
        :rtype: int
        """
        return self._used_hdd_capacity

    @used_hdd_capacity.setter
    def used_hdd_capacity(self, used_hdd_capacity):
        """Sets the used_hdd_capacity of this UsedQuota.


        :param used_hdd_capacity: The used_hdd_capacity of this UsedQuota.  # noqa: E501
        :type: int
        """
        if used_hdd_capacity is None:
            raise ValueError("Invalid value for `used_hdd_capacity`, must not be `None`")  # noqa: E501

        self._used_hdd_capacity = used_hdd_capacity

    @property
    def used_host_num(self):
        """Gets the used_host_num of this UsedQuota.  # noqa: E501


        :return: The used_host_num of this UsedQuota.  # noqa: E501
        :rtype: int
        """
        return self._used_host_num

    @used_host_num.setter
    def used_host_num(self, used_host_num):
        """Sets the used_host_num of this UsedQuota.


        :param used_host_num: The used_host_num of this UsedQuota.  # noqa: E501
        :type: int
        """
        if used_host_num is None:
            raise ValueError("Invalid value for `used_host_num`, must not be `None`")  # noqa: E501

        self._used_host_num = used_host_num

    @property
    def used_ssd_capacity(self):
        """Gets the used_ssd_capacity of this UsedQuota.  # noqa: E501


        :return: The used_ssd_capacity of this UsedQuota.  # noqa: E501
        :rtype: int
        """
        return self._used_ssd_capacity

    @used_ssd_capacity.setter
    def used_ssd_capacity(self, used_ssd_capacity):
        """Sets the used_ssd_capacity of this UsedQuota.


        :param used_ssd_capacity: The used_ssd_capacity of this UsedQuota.  # noqa: E501
        :type: int
        """
        if used_ssd_capacity is None:
            raise ValueError("Invalid value for `used_ssd_capacity`, must not be `None`")  # noqa: E501

        self._used_ssd_capacity = used_ssd_capacity

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
        if not isinstance(other, UsedQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other