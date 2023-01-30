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


class AuthRSAKey(object):
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
        'expiration': 'datetime',
        'id': 'str',
        'public_key': 'str'
    }

    attribute_map = {
        'expiration': 'expiration',
        'id': 'id',
        'public_key': 'public_key'
    }

    def __init__(self, expiration=None, id=None, public_key=None):  # noqa: E501
        """AuthRSAKey - a model defined in Swagger"""  # noqa: E501

        self._expiration = None
        self._id = None
        self._public_key = None
        self.discriminator = None

        if expiration is not None:
            self.expiration = expiration
        if id is not None:
            self.id = id
        if public_key is not None:
            self.public_key = public_key

    @property
    def expiration(self):
        """Gets the expiration of this AuthRSAKey.  # noqa: E501


        :return: The expiration of this AuthRSAKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this AuthRSAKey.


        :param expiration: The expiration of this AuthRSAKey.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def id(self):
        """Gets the id of this AuthRSAKey.  # noqa: E501


        :return: The id of this AuthRSAKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthRSAKey.


        :param id: The id of this AuthRSAKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def public_key(self):
        """Gets the public_key of this AuthRSAKey.  # noqa: E501


        :return: The public_key of this AuthRSAKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AuthRSAKey.


        :param public_key: The public_key of this AuthRSAKey.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

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
        if not isinstance(other, AuthRSAKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
