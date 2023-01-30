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

# from xms_client.models.os_builtin_blu_ray import OSBuiltinBluRay  # noqa: F401,E501


class OSBuiltinBluRayResp(object):
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
        'os_builtin_blu_ray': 'OSBuiltinBluRay'
    }

    attribute_map = {
        'os_builtin_blu_ray': 'os_builtin_blu_ray'
    }

    def __init__(self, os_builtin_blu_ray=None):  # noqa: E501
        """OSBuiltinBluRayResp - a model defined in Swagger"""  # noqa: E501

        self._os_builtin_blu_ray = None
        self.discriminator = None

        if os_builtin_blu_ray is not None:
            self.os_builtin_blu_ray = os_builtin_blu_ray

    @property
    def os_builtin_blu_ray(self):
        """Gets the os_builtin_blu_ray of this OSBuiltinBluRayResp.  # noqa: E501


        :return: The os_builtin_blu_ray of this OSBuiltinBluRayResp.  # noqa: E501
        :rtype: OSBuiltinBluRay
        """
        return self._os_builtin_blu_ray

    @os_builtin_blu_ray.setter
    def os_builtin_blu_ray(self, os_builtin_blu_ray):
        """Sets the os_builtin_blu_ray of this OSBuiltinBluRayResp.


        :param os_builtin_blu_ray: The os_builtin_blu_ray of this OSBuiltinBluRayResp.  # noqa: E501
        :type: OSBuiltinBluRay
        """

        self._os_builtin_blu_ray = os_builtin_blu_ray

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
        if not isinstance(other, OSBuiltinBluRayResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other