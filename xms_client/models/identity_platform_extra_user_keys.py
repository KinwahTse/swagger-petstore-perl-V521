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


class IdentityPlatformExtraUserKeys(object):
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
        'user_id': 'str',
        'user_name': 'str',
        'user_roles': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_roles': 'user_roles'
    }

    def __init__(self, user_id=None, user_name=None, user_roles=None):  # noqa: E501
        """IdentityPlatformExtraUserKeys - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._user_name = None
        self._user_roles = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_roles is not None:
            self.user_roles = user_roles

    @property
    def user_id(self):
        """Gets the user_id of this IdentityPlatformExtraUserKeys.  # noqa: E501


        :return: The user_id of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this IdentityPlatformExtraUserKeys.


        :param user_id: The user_id of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this IdentityPlatformExtraUserKeys.  # noqa: E501


        :return: The user_name of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this IdentityPlatformExtraUserKeys.


        :param user_name: The user_name of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_roles(self):
        """Gets the user_roles of this IdentityPlatformExtraUserKeys.  # noqa: E501


        :return: The user_roles of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :rtype: str
        """
        return self._user_roles

    @user_roles.setter
    def user_roles(self, user_roles):
        """Sets the user_roles of this IdentityPlatformExtraUserKeys.


        :param user_roles: The user_roles of this IdentityPlatformExtraUserKeys.  # noqa: E501
        :type: str
        """

        self._user_roles = user_roles

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
        if not isinstance(other, IdentityPlatformExtraUserKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
