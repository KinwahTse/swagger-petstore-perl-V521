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


class AccessTokenCreateReqAccessToken(object):
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
        'description': 'str',
        'name': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'roles': 'roles'
    }

    def __init__(self, description=None, name=None, roles=None):  # noqa: E501
        """AccessTokenCreateReqAccessToken - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._roles = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.roles = roles

    @property
    def description(self):
        """Gets the description of this AccessTokenCreateReqAccessToken.  # noqa: E501

        description of access token  # noqa: E501

        :return: The description of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessTokenCreateReqAccessToken.

        description of access token  # noqa: E501

        :param description: The description of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this AccessTokenCreateReqAccessToken.  # noqa: E501

        name of access token  # noqa: E501

        :return: The name of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessTokenCreateReqAccessToken.

        name of access token  # noqa: E501

        :param name: The name of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def roles(self):
        """Gets the roles of this AccessTokenCreateReqAccessToken.  # noqa: E501

        roles of access token  # noqa: E501

        :return: The roles of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessTokenCreateReqAccessToken.

        roles of access token  # noqa: E501

        :param roles: The roles of this AccessTokenCreateReqAccessToken.  # noqa: E501
        :type: list[str]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

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
        if not isinstance(other, AccessTokenCreateReqAccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
