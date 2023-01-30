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


class OSZoneTranslogsResp(object):
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
        'os_zone_translogs': 'list[OSZoneTranslog]'
    }

    attribute_map = {
        'os_zone_translogs': 'os_zone_translogs'
    }

    def __init__(self, os_zone_translogs=None):  # noqa: E501
        """OSZoneTranslogsResp - a model defined in Swagger"""  # noqa: E501

        self._os_zone_translogs = None
        self.discriminator = None

        if os_zone_translogs is not None:
            self.os_zone_translogs = os_zone_translogs

    @property
    def os_zone_translogs(self):
        """Gets the os_zone_translogs of this OSZoneTranslogsResp.  # noqa: E501


        :return: The os_zone_translogs of this OSZoneTranslogsResp.  # noqa: E501
        :rtype: list[OSZoneTranslog]
        """
        return self._os_zone_translogs

    @os_zone_translogs.setter
    def os_zone_translogs(self, os_zone_translogs):
        """Sets the os_zone_translogs of this OSZoneTranslogsResp.


        :param os_zone_translogs: The os_zone_translogs of this OSZoneTranslogsResp.  # noqa: E501
        :type: list[OSZoneTranslog]
        """

        self._os_zone_translogs = os_zone_translogs

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
        if not isinstance(other, OSZoneTranslogsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
