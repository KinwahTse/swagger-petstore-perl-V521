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


class HostCreateReqHost(object):
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
        'admin_ip': 'str',
        'cluster_id': 'int',
        'description': 'str',
        'gateway_ips': 'list[str]',
        'meta_device': 'str',
        'private_ip': 'str',
        'protection_domain_id': 'int',
        'public_ip': 'str',
        'roles': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'admin_ip': 'admin_ip',
        'cluster_id': 'cluster_id',
        'description': 'description',
        'gateway_ips': 'gateway_ips',
        'meta_device': 'meta_device',
        'private_ip': 'private_ip',
        'protection_domain_id': 'protection_domain_id',
        'public_ip': 'public_ip',
        'roles': 'roles',
        'type': 'type'
    }

    def __init__(self, admin_ip=None, cluster_id=None, description=None, gateway_ips=None, meta_device=None, private_ip=None, protection_domain_id=None, public_ip=None, roles=None, type=None):  # noqa: E501
        """HostCreateReqHost - a model defined in Swagger"""  # noqa: E501

        self._admin_ip = None
        self._cluster_id = None
        self._description = None
        self._gateway_ips = None
        self._meta_device = None
        self._private_ip = None
        self._protection_domain_id = None
        self._public_ip = None
        self._roles = None
        self._type = None
        self.discriminator = None

        self.admin_ip = admin_ip
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if description is not None:
            self.description = description
        if gateway_ips is not None:
            self.gateway_ips = gateway_ips
        if meta_device is not None:
            self.meta_device = meta_device
        if private_ip is not None:
            self.private_ip = private_ip
        if protection_domain_id is not None:
            self.protection_domain_id = protection_domain_id
        if public_ip is not None:
            self.public_ip = public_ip
        if roles is not None:
            self.roles = roles
        if type is not None:
            self.type = type

    @property
    def admin_ip(self):
        """Gets the admin_ip of this HostCreateReqHost.  # noqa: E501

        admin ip  # noqa: E501

        :return: The admin_ip of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._admin_ip

    @admin_ip.setter
    def admin_ip(self, admin_ip):
        """Sets the admin_ip of this HostCreateReqHost.

        admin ip  # noqa: E501

        :param admin_ip: The admin_ip of this HostCreateReqHost.  # noqa: E501
        :type: str
        """
        if admin_ip is None:
            raise ValueError("Invalid value for `admin_ip`, must not be `None`")  # noqa: E501

        self._admin_ip = admin_ip

    @property
    def cluster_id(self):
        """Gets the cluster_id of this HostCreateReqHost.  # noqa: E501

        cluster id  # noqa: E501

        :return: The cluster_id of this HostCreateReqHost.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this HostCreateReqHost.

        cluster id  # noqa: E501

        :param cluster_id: The cluster_id of this HostCreateReqHost.  # noqa: E501
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this HostCreateReqHost.  # noqa: E501

        host description  # noqa: E501

        :return: The description of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostCreateReqHost.

        host description  # noqa: E501

        :param description: The description of this HostCreateReqHost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gateway_ips(self):
        """Gets the gateway_ips of this HostCreateReqHost.  # noqa: E501

        gateway ips for s3  # noqa: E501

        :return: The gateway_ips of this HostCreateReqHost.  # noqa: E501
        :rtype: list[str]
        """
        return self._gateway_ips

    @gateway_ips.setter
    def gateway_ips(self, gateway_ips):
        """Sets the gateway_ips of this HostCreateReqHost.

        gateway ips for s3  # noqa: E501

        :param gateway_ips: The gateway_ips of this HostCreateReqHost.  # noqa: E501
        :type: list[str]
        """

        self._gateway_ips = gateway_ips

    @property
    def meta_device(self):
        """Gets the meta_device of this HostCreateReqHost.  # noqa: E501

        meta device for docker  # noqa: E501

        :return: The meta_device of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._meta_device

    @meta_device.setter
    def meta_device(self, meta_device):
        """Sets the meta_device of this HostCreateReqHost.

        meta device for docker  # noqa: E501

        :param meta_device: The meta_device of this HostCreateReqHost.  # noqa: E501
        :type: str
        """

        self._meta_device = meta_device

    @property
    def private_ip(self):
        """Gets the private_ip of this HostCreateReqHost.  # noqa: E501

        cluster private ip for internal data access  # noqa: E501

        :return: The private_ip of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this HostCreateReqHost.

        cluster private ip for internal data access  # noqa: E501

        :param private_ip: The private_ip of this HostCreateReqHost.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def protection_domain_id(self):
        """Gets the protection_domain_id of this HostCreateReqHost.  # noqa: E501

        deprecated  # noqa: E501

        :return: The protection_domain_id of this HostCreateReqHost.  # noqa: E501
        :rtype: int
        """
        return self._protection_domain_id

    @protection_domain_id.setter
    def protection_domain_id(self, protection_domain_id):
        """Sets the protection_domain_id of this HostCreateReqHost.

        deprecated  # noqa: E501

        :param protection_domain_id: The protection_domain_id of this HostCreateReqHost.  # noqa: E501
        :type: int
        """

        self._protection_domain_id = protection_domain_id

    @property
    def public_ip(self):
        """Gets the public_ip of this HostCreateReqHost.  # noqa: E501

        public ip for outside data access  # noqa: E501

        :return: The public_ip of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this HostCreateReqHost.

        public ip for outside data access  # noqa: E501

        :param public_ip: The public_ip of this HostCreateReqHost.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def roles(self):
        """Gets the roles of this HostCreateReqHost.  # noqa: E501

        host roles: admin,monitor,block_storage_gateway,file_storage_gateway,s3_gateway,nfs_gateway  # noqa: E501

        :return: The roles of this HostCreateReqHost.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this HostCreateReqHost.

        host roles: admin,monitor,block_storage_gateway,file_storage_gateway,s3_gateway,nfs_gateway  # noqa: E501

        :param roles: The roles of this HostCreateReqHost.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def type(self):
        """Gets the type of this HostCreateReqHost.  # noqa: E501

        storage server or storage client  # noqa: E501

        :return: The type of this HostCreateReqHost.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostCreateReqHost.

        storage server or storage client  # noqa: E501

        :param type: The type of this HostCreateReqHost.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, HostCreateReqHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
