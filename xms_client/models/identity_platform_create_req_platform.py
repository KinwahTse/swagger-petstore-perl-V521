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

# from xms_client.models.identity_platform_extra import IdentityPlatformExtra  # noqa: F401,E501


class IdentityPlatformCreateReqPlatform(object):
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
        'enabled': 'bool',
        'extra': 'IdentityPlatformExtra',
        'login_page_enabled': 'bool',
        'name': 'str',
        'type': 'str',
        'url': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'extra': 'extra',
        'login_page_enabled': 'login_page_enabled',
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'vendor': 'vendor'
    }

    def __init__(self, enabled=None, extra=None, login_page_enabled=None, name=None, type=None, url=None, vendor=None):  # noqa: E501
        """IdentityPlatformCreateReqPlatform - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._extra = None
        self._login_page_enabled = None
        self._name = None
        self._type = None
        self._url = None
        self._vendor = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if extra is not None:
            self.extra = extra
        if login_page_enabled is not None:
            self.login_page_enabled = login_page_enabled
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if vendor is not None:
            self.vendor = vendor

    @property
    def enabled(self):
        """Gets the enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501


        :return: The enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityPlatformCreateReqPlatform.


        :param enabled: The enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def extra(self):
        """Gets the extra of this IdentityPlatformCreateReqPlatform.  # noqa: E501


        :return: The extra of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: IdentityPlatformExtra
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this IdentityPlatformCreateReqPlatform.


        :param extra: The extra of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: IdentityPlatformExtra
        """

        self._extra = extra

    @property
    def login_page_enabled(self):
        """Gets the login_page_enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501


        :return: The login_page_enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: bool
        """
        return self._login_page_enabled

    @login_page_enabled.setter
    def login_page_enabled(self, login_page_enabled):
        """Sets the login_page_enabled of this IdentityPlatformCreateReqPlatform.


        :param login_page_enabled: The login_page_enabled of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: bool
        """

        self._login_page_enabled = login_page_enabled

    @property
    def name(self):
        """Gets the name of this IdentityPlatformCreateReqPlatform.  # noqa: E501

        name of identity platform  # noqa: E501

        :return: The name of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityPlatformCreateReqPlatform.

        name of identity platform  # noqa: E501

        :param name: The name of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this IdentityPlatformCreateReqPlatform.  # noqa: E501

        type of identity platform  # noqa: E501

        :return: The type of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityPlatformCreateReqPlatform.

        type of identity platform  # noqa: E501

        :param type: The type of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this IdentityPlatformCreateReqPlatform.  # noqa: E501


        :return: The url of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdentityPlatformCreateReqPlatform.


        :param url: The url of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def vendor(self):
        """Gets the vendor of this IdentityPlatformCreateReqPlatform.  # noqa: E501


        :return: The vendor of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this IdentityPlatformCreateReqPlatform.


        :param vendor: The vendor of this IdentityPlatformCreateReqPlatform.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, IdentityPlatformCreateReqPlatform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
