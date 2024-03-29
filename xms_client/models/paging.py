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


class Paging(object):
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
        'count': 'int',
        'duration': 'int',
        'duration_begin': 'datetime',
        'duration_end': 'datetime',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'period': 'str',
        'total_count': 'int',
        'truncated': 'bool'
    }

    attribute_map = {
        'count': 'count',
        'duration': 'duration',
        'duration_begin': 'duration_begin',
        'duration_end': 'duration_end',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'period': 'period',
        'total_count': 'total_count',
        'truncated': 'truncated'
    }

    def __init__(self, count=None, duration=None, duration_begin=None, duration_end=None, limit=None, next=None, offset=None, period=None, total_count=None, truncated=None):  # noqa: E501
        """Paging - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._duration = None
        self._duration_begin = None
        self._duration_end = None
        self._limit = None
        self._next = None
        self._offset = None
        self._period = None
        self._total_count = None
        self._truncated = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration
        if duration_begin is not None:
            self.duration_begin = duration_begin
        if duration_end is not None:
            self.duration_end = duration_end
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if period is not None:
            self.period = period
        if total_count is not None:
            self.total_count = total_count
        if truncated is not None:
            self.truncated = truncated

    @property
    def count(self):
        """Gets the count of this Paging.  # noqa: E501


        :return: The count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Paging.


        :param count: The count of this Paging.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def duration(self):
        """Gets the duration of this Paging.  # noqa: E501


        :return: The duration of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Paging.


        :param duration: The duration of this Paging.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def duration_begin(self):
        """Gets the duration_begin of this Paging.  # noqa: E501


        :return: The duration_begin of this Paging.  # noqa: E501
        :rtype: datetime
        """
        return self._duration_begin

    @duration_begin.setter
    def duration_begin(self, duration_begin):
        """Sets the duration_begin of this Paging.


        :param duration_begin: The duration_begin of this Paging.  # noqa: E501
        :type: datetime
        """

        self._duration_begin = duration_begin

    @property
    def duration_end(self):
        """Gets the duration_end of this Paging.  # noqa: E501


        :return: The duration_end of this Paging.  # noqa: E501
        :rtype: datetime
        """
        return self._duration_end

    @duration_end.setter
    def duration_end(self, duration_end):
        """Sets the duration_end of this Paging.


        :param duration_end: The duration_end of this Paging.  # noqa: E501
        :type: datetime
        """

        self._duration_end = duration_end

    @property
    def limit(self):
        """Gets the limit of this Paging.  # noqa: E501


        :return: The limit of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Paging.


        :param limit: The limit of this Paging.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this Paging.  # noqa: E501


        :return: The next of this Paging.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Paging.


        :param next: The next of this Paging.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this Paging.  # noqa: E501


        :return: The offset of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Paging.


        :param offset: The offset of this Paging.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def period(self):
        """Gets the period of this Paging.  # noqa: E501


        :return: The period of this Paging.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Paging.


        :param period: The period of this Paging.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def total_count(self):
        """Gets the total_count of this Paging.  # noqa: E501


        :return: The total_count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Paging.


        :param total_count: The total_count of this Paging.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def truncated(self):
        """Gets the truncated of this Paging.  # noqa: E501


        :return: The truncated of this Paging.  # noqa: E501
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this Paging.


        :param truncated: The truncated of this Paging.  # noqa: E501
        :type: bool
        """

        self._truncated = truncated

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
        if not isinstance(other, Paging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
