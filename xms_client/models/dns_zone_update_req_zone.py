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


class DNSZoneUpdateReqZone(object):
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
        'origin': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'origin': 'origin',
        'ttl': 'ttl'
    }

    def __init__(self, origin=None, ttl=None):  # noqa: E501
        """DNSZoneUpdateReqZone - a model defined in Swagger"""  # noqa: E501

        self._origin = None
        self._ttl = None
        self.discriminator = None

        if origin is not None:
            self.origin = origin
        if ttl is not None:
            self.ttl = ttl

    @property
    def origin(self):
        """Gets the origin of this DNSZoneUpdateReqZone.  # noqa: E501

        dns origin in zone  # noqa: E501

        :return: The origin of this DNSZoneUpdateReqZone.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this DNSZoneUpdateReqZone.

        dns origin in zone  # noqa: E501

        :param origin: The origin of this DNSZoneUpdateReqZone.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def ttl(self):
        """Gets the ttl of this DNSZoneUpdateReqZone.  # noqa: E501

        dns ttl with zone  # noqa: E501

        :return: The ttl of this DNSZoneUpdateReqZone.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DNSZoneUpdateReqZone.

        dns ttl with zone  # noqa: E501

        :param ttl: The ttl of this DNSZoneUpdateReqZone.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

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
        if not isinstance(other, DNSZoneUpdateReqZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
