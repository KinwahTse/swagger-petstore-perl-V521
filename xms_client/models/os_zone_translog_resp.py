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

# from xms_client.models.os_zone_translog import OSZoneTranslog  # noqa: F401,E501


class OSZoneTranslogResp(object):
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
        'os_zone_translog': 'OSZoneTranslog'
    }

    attribute_map = {
        'os_zone_translog': 'os_zone_translog'
    }

    def __init__(self, os_zone_translog=None):  # noqa: E501
        """OSZoneTranslogResp - a model defined in Swagger"""  # noqa: E501

        self._os_zone_translog = None
        self.discriminator = None

        if os_zone_translog is not None:
            self.os_zone_translog = os_zone_translog

    @property
    def os_zone_translog(self):
        """Gets the os_zone_translog of this OSZoneTranslogResp.  # noqa: E501


        :return: The os_zone_translog of this OSZoneTranslogResp.  # noqa: E501
        :rtype: OSZoneTranslog
        """
        return self._os_zone_translog

    @os_zone_translog.setter
    def os_zone_translog(self, os_zone_translog):
        """Sets the os_zone_translog of this OSZoneTranslogResp.


        :param os_zone_translog: The os_zone_translog of this OSZoneTranslogResp.  # noqa: E501
        :type: OSZoneTranslog
        """

        self._os_zone_translog = os_zone_translog

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
        if not isinstance(other, OSZoneTranslogResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
