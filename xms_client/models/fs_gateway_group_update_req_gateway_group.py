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


class FSGatewayGroupUpdateReqGatewayGroup(object):
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
        'encoding': 'str',
        'name': 'str',
        'nfs_versions': 'list[str]',
        'security': 'str',
        'smb1_enabled': 'bool',
        'smb_ports': 'list[int]',
        'types': 'list[str]',
        'vip': 'str'
    }

    attribute_map = {
        'description': 'description',
        'encoding': 'encoding',
        'name': 'name',
        'nfs_versions': 'nfs_versions',
        'security': 'security',
        'smb1_enabled': 'smb1_enabled',
        'smb_ports': 'smb_ports',
        'types': 'types',
        'vip': 'vip'
    }

    def __init__(self, description=None, encoding=None, name=None, nfs_versions=None, security=None, smb1_enabled=None, smb_ports=None, types=None, vip=None):  # noqa: E501
        """FSGatewayGroupUpdateReqGatewayGroup - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._encoding = None
        self._name = None
        self._nfs_versions = None
        self._security = None
        self._smb1_enabled = None
        self._smb_ports = None
        self._types = None
        self._vip = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if encoding is not None:
            self.encoding = encoding
        if name is not None:
            self.name = name
        if nfs_versions is not None:
            self.nfs_versions = nfs_versions
        if security is not None:
            self.security = security
        if smb1_enabled is not None:
            self.smb1_enabled = smb1_enabled
        if smb_ports is not None:
            self.smb_ports = smb_ports
        if types is not None:
            self.types = types
        if vip is not None:
            self.vip = vip

    @property
    def description(self):
        """Gets the description of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        description of gateway group  # noqa: E501

        :return: The description of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FSGatewayGroupUpdateReqGatewayGroup.

        description of gateway group  # noqa: E501

        :param description: The description of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def encoding(self):
        """Gets the encoding of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        ftp encoding format, default is utf8  # noqa: E501

        :return: The encoding of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this FSGatewayGroupUpdateReqGatewayGroup.

        ftp encoding format, default is utf8  # noqa: E501

        :param encoding: The encoding of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def name(self):
        """Gets the name of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        name of gateway group  # noqa: E501

        :return: The name of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FSGatewayGroupUpdateReqGatewayGroup.

        name of gateway group  # noqa: E501

        :param name: The name of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nfs_versions(self):
        """Gets the nfs_versions of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        nfs versions supported  # noqa: E501

        :return: The nfs_versions of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._nfs_versions

    @nfs_versions.setter
    def nfs_versions(self, nfs_versions):
        """Sets the nfs_versions of this FSGatewayGroupUpdateReqGatewayGroup.

        nfs versions supported  # noqa: E501

        :param nfs_versions: The nfs_versions of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: list[str]
        """

        self._nfs_versions = nfs_versions

    @property
    def security(self):
        """Gets the security of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        smb security type  # noqa: E501

        :return: The security of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this FSGatewayGroupUpdateReqGatewayGroup.

        smb security type  # noqa: E501

        :param security: The security of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def smb1_enabled(self):
        """Gets the smb1_enabled of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        smb version 1.0 enabled  # noqa: E501

        :return: The smb1_enabled of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: bool
        """
        return self._smb1_enabled

    @smb1_enabled.setter
    def smb1_enabled(self, smb1_enabled):
        """Sets the smb1_enabled of this FSGatewayGroupUpdateReqGatewayGroup.

        smb version 1.0 enabled  # noqa: E501

        :param smb1_enabled: The smb1_enabled of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: bool
        """

        self._smb1_enabled = smb1_enabled

    @property
    def smb_ports(self):
        """Gets the smb_ports of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        smb ports  # noqa: E501

        :return: The smb_ports of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: list[int]
        """
        return self._smb_ports

    @smb_ports.setter
    def smb_ports(self, smb_ports):
        """Sets the smb_ports of this FSGatewayGroupUpdateReqGatewayGroup.

        smb ports  # noqa: E501

        :param smb_ports: The smb_ports of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: list[int]
        """

        self._smb_ports = smb_ports

    @property
    def types(self):
        """Gets the types of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        types of supported  # noqa: E501

        :return: The types of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this FSGatewayGroupUpdateReqGatewayGroup.

        types of supported  # noqa: E501

        :param types: The types of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def vip(self):
        """Gets the vip of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501

        virtual ip of gateway group  # noqa: E501

        :return: The vip of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this FSGatewayGroupUpdateReqGatewayGroup.

        virtual ip of gateway group  # noqa: E501

        :param vip: The vip of this FSGatewayGroupUpdateReqGatewayGroup.  # noqa: E501
        :type: str
        """

        self._vip = vip

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
        if not isinstance(other, FSGatewayGroupUpdateReqGatewayGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
