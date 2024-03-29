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


class HostInitializationReqInitialization(object):
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
        'admin_ips': 'list[str]',
        'disable_firewalld': 'bool',
        'hostname_prefix': 'str',
        'set_hostname': 'bool',
        'ssh_password': 'str',
        'ssh_user': 'str'
    }

    attribute_map = {
        'admin_ips': 'admin_ips',
        'disable_firewalld': 'disable_firewalld',
        'hostname_prefix': 'hostname_prefix',
        'set_hostname': 'set_hostname',
        'ssh_password': 'ssh_password',
        'ssh_user': 'ssh_user'
    }

    def __init__(self, admin_ips=None, disable_firewalld=None, hostname_prefix=None, set_hostname=None, ssh_password=None, ssh_user=None):  # noqa: E501
        """HostInitializationReqInitialization - a model defined in Swagger"""  # noqa: E501

        self._admin_ips = None
        self._disable_firewalld = None
        self._hostname_prefix = None
        self._set_hostname = None
        self._ssh_password = None
        self._ssh_user = None
        self.discriminator = None

        self.admin_ips = admin_ips
        if disable_firewalld is not None:
            self.disable_firewalld = disable_firewalld
        if hostname_prefix is not None:
            self.hostname_prefix = hostname_prefix
        if set_hostname is not None:
            self.set_hostname = set_hostname
        if ssh_password is not None:
            self.ssh_password = ssh_password
        self.ssh_user = ssh_user

    @property
    def admin_ips(self):
        """Gets the admin_ips of this HostInitializationReqInitialization.  # noqa: E501


        :return: The admin_ips of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: list[str]
        """
        return self._admin_ips

    @admin_ips.setter
    def admin_ips(self, admin_ips):
        """Sets the admin_ips of this HostInitializationReqInitialization.


        :param admin_ips: The admin_ips of this HostInitializationReqInitialization.  # noqa: E501
        :type: list[str]
        """
        if admin_ips is None:
            raise ValueError("Invalid value for `admin_ips`, must not be `None`")  # noqa: E501

        self._admin_ips = admin_ips

    @property
    def disable_firewalld(self):
        """Gets the disable_firewalld of this HostInitializationReqInitialization.  # noqa: E501


        :return: The disable_firewalld of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: bool
        """
        return self._disable_firewalld

    @disable_firewalld.setter
    def disable_firewalld(self, disable_firewalld):
        """Sets the disable_firewalld of this HostInitializationReqInitialization.


        :param disable_firewalld: The disable_firewalld of this HostInitializationReqInitialization.  # noqa: E501
        :type: bool
        """

        self._disable_firewalld = disable_firewalld

    @property
    def hostname_prefix(self):
        """Gets the hostname_prefix of this HostInitializationReqInitialization.  # noqa: E501


        :return: The hostname_prefix of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: str
        """
        return self._hostname_prefix

    @hostname_prefix.setter
    def hostname_prefix(self, hostname_prefix):
        """Sets the hostname_prefix of this HostInitializationReqInitialization.


        :param hostname_prefix: The hostname_prefix of this HostInitializationReqInitialization.  # noqa: E501
        :type: str
        """

        self._hostname_prefix = hostname_prefix

    @property
    def set_hostname(self):
        """Gets the set_hostname of this HostInitializationReqInitialization.  # noqa: E501


        :return: The set_hostname of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: bool
        """
        return self._set_hostname

    @set_hostname.setter
    def set_hostname(self, set_hostname):
        """Sets the set_hostname of this HostInitializationReqInitialization.


        :param set_hostname: The set_hostname of this HostInitializationReqInitialization.  # noqa: E501
        :type: bool
        """

        self._set_hostname = set_hostname

    @property
    def ssh_password(self):
        """Gets the ssh_password of this HostInitializationReqInitialization.  # noqa: E501


        :return: The ssh_password of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: str
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this HostInitializationReqInitialization.


        :param ssh_password: The ssh_password of this HostInitializationReqInitialization.  # noqa: E501
        :type: str
        """

        self._ssh_password = ssh_password

    @property
    def ssh_user(self):
        """Gets the ssh_user of this HostInitializationReqInitialization.  # noqa: E501


        :return: The ssh_user of this HostInitializationReqInitialization.  # noqa: E501
        :rtype: str
        """
        return self._ssh_user

    @ssh_user.setter
    def ssh_user(self, ssh_user):
        """Sets the ssh_user of this HostInitializationReqInitialization.


        :param ssh_user: The ssh_user of this HostInitializationReqInitialization.  # noqa: E501
        :type: str
        """
        if ssh_user is None:
            raise ValueError("Invalid value for `ssh_user`, must not be `None`")  # noqa: E501

        self._ssh_user = ssh_user

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
        if not isinstance(other, HostInitializationReqInitialization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
