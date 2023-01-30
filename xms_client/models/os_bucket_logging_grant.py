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


class OSBucketLoggingGrant(object):
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
        'os_user_email': 'str',
        'os_user_name': 'str',
        'permission': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'os_user_email': 'os_user_email',
        'os_user_name': 'os_user_name',
        'permission': 'permission',
        'uri': 'uri'
    }

    def __init__(self, os_user_email=None, os_user_name=None, permission=None, uri=None):  # noqa: E501
        """OSBucketLoggingGrant - a model defined in Swagger"""  # noqa: E501

        self._os_user_email = None
        self._os_user_name = None
        self._permission = None
        self._uri = None
        self.discriminator = None

        if os_user_email is not None:
            self.os_user_email = os_user_email
        if os_user_name is not None:
            self.os_user_name = os_user_name
        if permission is not None:
            self.permission = permission
        if uri is not None:
            self.uri = uri

    @property
    def os_user_email(self):
        """Gets the os_user_email of this OSBucketLoggingGrant.  # noqa: E501


        :return: The os_user_email of this OSBucketLoggingGrant.  # noqa: E501
        :rtype: str
        """
        return self._os_user_email

    @os_user_email.setter
    def os_user_email(self, os_user_email):
        """Sets the os_user_email of this OSBucketLoggingGrant.


        :param os_user_email: The os_user_email of this OSBucketLoggingGrant.  # noqa: E501
        :type: str
        """

        self._os_user_email = os_user_email

    @property
    def os_user_name(self):
        """Gets the os_user_name of this OSBucketLoggingGrant.  # noqa: E501


        :return: The os_user_name of this OSBucketLoggingGrant.  # noqa: E501
        :rtype: str
        """
        return self._os_user_name

    @os_user_name.setter
    def os_user_name(self, os_user_name):
        """Sets the os_user_name of this OSBucketLoggingGrant.


        :param os_user_name: The os_user_name of this OSBucketLoggingGrant.  # noqa: E501
        :type: str
        """

        self._os_user_name = os_user_name

    @property
    def permission(self):
        """Gets the permission of this OSBucketLoggingGrant.  # noqa: E501


        :return: The permission of this OSBucketLoggingGrant.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this OSBucketLoggingGrant.


        :param permission: The permission of this OSBucketLoggingGrant.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def uri(self):
        """Gets the uri of this OSBucketLoggingGrant.  # noqa: E501


        :return: The uri of this OSBucketLoggingGrant.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this OSBucketLoggingGrant.


        :param uri: The uri of this OSBucketLoggingGrant.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, OSBucketLoggingGrant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other