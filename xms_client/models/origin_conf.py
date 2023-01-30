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


class OriginConf(object):
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
        'class_id': 'str',
        'class_name': 'str',
        'delete_origin': 'bool',
        'expiration_days': 'int',
        'follow_redirect': 'bool',
        'policy_id': 'int',
        'redirect_code': 'int'
    }

    attribute_map = {
        'class_id': 'class_id',
        'class_name': 'class_name',
        'delete_origin': 'delete_origin',
        'expiration_days': 'expiration_days',
        'follow_redirect': 'follow_redirect',
        'policy_id': 'policy_id',
        'redirect_code': 'redirect_code'
    }

    def __init__(self, class_id=None, class_name=None, delete_origin=None, expiration_days=None, follow_redirect=None, policy_id=None, redirect_code=None):  # noqa: E501
        """OriginConf - a model defined in Swagger"""  # noqa: E501

        self._class_id = None
        self._class_name = None
        self._delete_origin = None
        self._expiration_days = None
        self._follow_redirect = None
        self._policy_id = None
        self._redirect_code = None
        self.discriminator = None

        if class_id is not None:
            self.class_id = class_id
        if class_name is not None:
            self.class_name = class_name
        if delete_origin is not None:
            self.delete_origin = delete_origin
        if expiration_days is not None:
            self.expiration_days = expiration_days
        if follow_redirect is not None:
            self.follow_redirect = follow_redirect
        if policy_id is not None:
            self.policy_id = policy_id
        if redirect_code is not None:
            self.redirect_code = redirect_code

    @property
    def class_id(self):
        """Gets the class_id of this OriginConf.  # noqa: E501


        :return: The class_id of this OriginConf.  # noqa: E501
        :rtype: str
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this OriginConf.


        :param class_id: The class_id of this OriginConf.  # noqa: E501
        :type: str
        """

        self._class_id = class_id

    @property
    def class_name(self):
        """Gets the class_name of this OriginConf.  # noqa: E501


        :return: The class_name of this OriginConf.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this OriginConf.


        :param class_name: The class_name of this OriginConf.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def delete_origin(self):
        """Gets the delete_origin of this OriginConf.  # noqa: E501


        :return: The delete_origin of this OriginConf.  # noqa: E501
        :rtype: bool
        """
        return self._delete_origin

    @delete_origin.setter
    def delete_origin(self, delete_origin):
        """Sets the delete_origin of this OriginConf.


        :param delete_origin: The delete_origin of this OriginConf.  # noqa: E501
        :type: bool
        """

        self._delete_origin = delete_origin

    @property
    def expiration_days(self):
        """Gets the expiration_days of this OriginConf.  # noqa: E501


        :return: The expiration_days of this OriginConf.  # noqa: E501
        :rtype: int
        """
        return self._expiration_days

    @expiration_days.setter
    def expiration_days(self, expiration_days):
        """Sets the expiration_days of this OriginConf.


        :param expiration_days: The expiration_days of this OriginConf.  # noqa: E501
        :type: int
        """

        self._expiration_days = expiration_days

    @property
    def follow_redirect(self):
        """Gets the follow_redirect of this OriginConf.  # noqa: E501


        :return: The follow_redirect of this OriginConf.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirect

    @follow_redirect.setter
    def follow_redirect(self, follow_redirect):
        """Sets the follow_redirect of this OriginConf.


        :param follow_redirect: The follow_redirect of this OriginConf.  # noqa: E501
        :type: bool
        """

        self._follow_redirect = follow_redirect

    @property
    def policy_id(self):
        """Gets the policy_id of this OriginConf.  # noqa: E501


        :return: The policy_id of this OriginConf.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this OriginConf.


        :param policy_id: The policy_id of this OriginConf.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def redirect_code(self):
        """Gets the redirect_code of this OriginConf.  # noqa: E501


        :return: The redirect_code of this OriginConf.  # noqa: E501
        :rtype: int
        """
        return self._redirect_code

    @redirect_code.setter
    def redirect_code(self, redirect_code):
        """Sets the redirect_code of this OriginConf.


        :param redirect_code: The redirect_code of this OriginConf.  # noqa: E501
        :type: int
        """

        self._redirect_code = redirect_code

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
        if not isinstance(other, OriginConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
