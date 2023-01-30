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

# from xms_client.models.lifecycle_base import LifecycleBase  # noqa: F401,E501


class LifecycleTransition(object):
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
        'days': 'int',
        'start_at': 'str',
        'stop_at': 'str',
        'storage_class': 'str',
        'type': 'str'
    }

    attribute_map = {
        'days': 'days',
        'start_at': 'start_at',
        'stop_at': 'stop_at',
        'storage_class': 'storage_class',
        'type': 'type'
    }

    def __init__(self, days=None, start_at=None, stop_at=None, storage_class=None, type=None):  # noqa: E501
        """LifecycleTransition - a model defined in Swagger"""  # noqa: E501

        self._days = None
        self._start_at = None
        self._stop_at = None
        self._storage_class = None
        self._type = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if start_at is not None:
            self.start_at = start_at
        if stop_at is not None:
            self.stop_at = stop_at
        if storage_class is not None:
            self.storage_class = storage_class
        if type is not None:
            self.type = type

    @property
    def days(self):
        """Gets the days of this LifecycleTransition.  # noqa: E501


        :return: The days of this LifecycleTransition.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this LifecycleTransition.


        :param days: The days of this LifecycleTransition.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def start_at(self):
        """Gets the start_at of this LifecycleTransition.  # noqa: E501


        :return: The start_at of this LifecycleTransition.  # noqa: E501
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this LifecycleTransition.


        :param start_at: The start_at of this LifecycleTransition.  # noqa: E501
        :type: str
        """

        self._start_at = start_at

    @property
    def stop_at(self):
        """Gets the stop_at of this LifecycleTransition.  # noqa: E501


        :return: The stop_at of this LifecycleTransition.  # noqa: E501
        :rtype: str
        """
        return self._stop_at

    @stop_at.setter
    def stop_at(self, stop_at):
        """Sets the stop_at of this LifecycleTransition.


        :param stop_at: The stop_at of this LifecycleTransition.  # noqa: E501
        :type: str
        """

        self._stop_at = stop_at

    @property
    def storage_class(self):
        """Gets the storage_class of this LifecycleTransition.  # noqa: E501


        :return: The storage_class of this LifecycleTransition.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this LifecycleTransition.


        :param storage_class: The storage_class of this LifecycleTransition.  # noqa: E501
        :type: str
        """

        self._storage_class = storage_class

    @property
    def type(self):
        """Gets the type of this LifecycleTransition.  # noqa: E501


        :return: The type of this LifecycleTransition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LifecycleTransition.


        :param type: The type of this LifecycleTransition.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, LifecycleTransition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
