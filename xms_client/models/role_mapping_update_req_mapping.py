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


class RoleMappingUpdateReqMapping(object):
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
        'default': 'bool',
        'value': 'str'
    }

    attribute_map = {
        'default': 'default',
        'value': 'value'
    }

    def __init__(self, default=None, value=None):  # noqa: E501
        """RoleMappingUpdateReqMapping - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._value = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if value is not None:
            self.value = value

    @property
    def default(self):
        """Gets the default of this RoleMappingUpdateReqMapping.  # noqa: E501


        :return: The default of this RoleMappingUpdateReqMapping.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this RoleMappingUpdateReqMapping.


        :param default: The default of this RoleMappingUpdateReqMapping.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def value(self):
        """Gets the value of this RoleMappingUpdateReqMapping.  # noqa: E501

        roles of identity platform  # noqa: E501

        :return: The value of this RoleMappingUpdateReqMapping.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RoleMappingUpdateReqMapping.

        roles of identity platform  # noqa: E501

        :param value: The value of this RoleMappingUpdateReqMapping.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, RoleMappingUpdateReqMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other