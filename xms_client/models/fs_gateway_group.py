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

# from xms_client.models.cluster_nestview import ClusterNestview  # noqa: F401,E501


class FSGatewayGroup(object):
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
        'action_status': 'str',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'description': 'str',
        'encoding': 'str',
        'folder_num': 'int',
        'id': 'int',
        'name': 'str',
        'nfs_versions': 'list[str]',
        'port': 'int',
        'security': 'str',
        'smb1_enabled': 'bool',
        'smb_ports': 'list[int]',
        'status': 'str',
        'types': 'list[str]',
        'update': 'datetime',
        'user_group_num': 'int',
        'vip': 'str',
        'vip_mask': 'int'
    }

    attribute_map = {
        'action_status': 'action_status',
        'cluster': 'cluster',
        'create': 'create',
        'description': 'description',
        'encoding': 'encoding',
        'folder_num': 'folder_num',
        'id': 'id',
        'name': 'name',
        'nfs_versions': 'nfs_versions',
        'port': 'port',
        'security': 'security',
        'smb1_enabled': 'smb1_enabled',
        'smb_ports': 'smb_ports',
        'status': 'status',
        'types': 'types',
        'update': 'update',
        'user_group_num': 'user_group_num',
        'vip': 'vip',
        'vip_mask': 'vip_mask'
    }

    def __init__(self, action_status=None, cluster=None, create=None, description=None, encoding=None, folder_num=None, id=None, name=None, nfs_versions=None, port=None, security=None, smb1_enabled=None, smb_ports=None, status=None, types=None, update=None, user_group_num=None, vip=None, vip_mask=None):  # noqa: E501
        """FSGatewayGroup - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._cluster = None
        self._create = None
        self._description = None
        self._encoding = None
        self._folder_num = None
        self._id = None
        self._name = None
        self._nfs_versions = None
        self._port = None
        self._security = None
        self._smb1_enabled = None
        self._smb_ports = None
        self._status = None
        self._types = None
        self._update = None
        self._user_group_num = None
        self._vip = None
        self._vip_mask = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if encoding is not None:
            self.encoding = encoding
        if folder_num is not None:
            self.folder_num = folder_num
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if nfs_versions is not None:
            self.nfs_versions = nfs_versions
        if port is not None:
            self.port = port
        if security is not None:
            self.security = security
        if smb1_enabled is not None:
            self.smb1_enabled = smb1_enabled
        if smb_ports is not None:
            self.smb_ports = smb_ports
        if status is not None:
            self.status = status
        if types is not None:
            self.types = types
        if update is not None:
            self.update = update
        if user_group_num is not None:
            self.user_group_num = user_group_num
        if vip is not None:
            self.vip = vip
        if vip_mask is not None:
            self.vip_mask = vip_mask

    @property
    def action_status(self):
        """Gets the action_status of this FSGatewayGroup.  # noqa: E501


        :return: The action_status of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this FSGatewayGroup.


        :param action_status: The action_status of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def cluster(self):
        """Gets the cluster of this FSGatewayGroup.  # noqa: E501


        :return: The cluster of this FSGatewayGroup.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this FSGatewayGroup.


        :param cluster: The cluster of this FSGatewayGroup.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this FSGatewayGroup.  # noqa: E501


        :return: The create of this FSGatewayGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this FSGatewayGroup.


        :param create: The create of this FSGatewayGroup.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this FSGatewayGroup.  # noqa: E501


        :return: The description of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FSGatewayGroup.


        :param description: The description of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def encoding(self):
        """Gets the encoding of this FSGatewayGroup.  # noqa: E501


        :return: The encoding of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this FSGatewayGroup.


        :param encoding: The encoding of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def folder_num(self):
        """Gets the folder_num of this FSGatewayGroup.  # noqa: E501


        :return: The folder_num of this FSGatewayGroup.  # noqa: E501
        :rtype: int
        """
        return self._folder_num

    @folder_num.setter
    def folder_num(self, folder_num):
        """Sets the folder_num of this FSGatewayGroup.


        :param folder_num: The folder_num of this FSGatewayGroup.  # noqa: E501
        :type: int
        """

        self._folder_num = folder_num

    @property
    def id(self):
        """Gets the id of this FSGatewayGroup.  # noqa: E501


        :return: The id of this FSGatewayGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FSGatewayGroup.


        :param id: The id of this FSGatewayGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FSGatewayGroup.  # noqa: E501


        :return: The name of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FSGatewayGroup.


        :param name: The name of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nfs_versions(self):
        """Gets the nfs_versions of this FSGatewayGroup.  # noqa: E501

        NFS attributes  # noqa: E501

        :return: The nfs_versions of this FSGatewayGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._nfs_versions

    @nfs_versions.setter
    def nfs_versions(self, nfs_versions):
        """Sets the nfs_versions of this FSGatewayGroup.

        NFS attributes  # noqa: E501

        :param nfs_versions: The nfs_versions of this FSGatewayGroup.  # noqa: E501
        :type: list[str]
        """

        self._nfs_versions = nfs_versions

    @property
    def port(self):
        """Gets the port of this FSGatewayGroup.  # noqa: E501

        FTP attributes  # noqa: E501

        :return: The port of this FSGatewayGroup.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FSGatewayGroup.

        FTP attributes  # noqa: E501

        :param port: The port of this FSGatewayGroup.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def security(self):
        """Gets the security of this FSGatewayGroup.  # noqa: E501

        SMB attributes  # noqa: E501

        :return: The security of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this FSGatewayGroup.

        SMB attributes  # noqa: E501

        :param security: The security of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def smb1_enabled(self):
        """Gets the smb1_enabled of this FSGatewayGroup.  # noqa: E501


        :return: The smb1_enabled of this FSGatewayGroup.  # noqa: E501
        :rtype: bool
        """
        return self._smb1_enabled

    @smb1_enabled.setter
    def smb1_enabled(self, smb1_enabled):
        """Sets the smb1_enabled of this FSGatewayGroup.


        :param smb1_enabled: The smb1_enabled of this FSGatewayGroup.  # noqa: E501
        :type: bool
        """

        self._smb1_enabled = smb1_enabled

    @property
    def smb_ports(self):
        """Gets the smb_ports of this FSGatewayGroup.  # noqa: E501


        :return: The smb_ports of this FSGatewayGroup.  # noqa: E501
        :rtype: list[int]
        """
        return self._smb_ports

    @smb_ports.setter
    def smb_ports(self, smb_ports):
        """Sets the smb_ports of this FSGatewayGroup.


        :param smb_ports: The smb_ports of this FSGatewayGroup.  # noqa: E501
        :type: list[int]
        """

        self._smb_ports = smb_ports

    @property
    def status(self):
        """Gets the status of this FSGatewayGroup.  # noqa: E501


        :return: The status of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FSGatewayGroup.


        :param status: The status of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def types(self):
        """Gets the types of this FSGatewayGroup.  # noqa: E501


        :return: The types of this FSGatewayGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this FSGatewayGroup.


        :param types: The types of this FSGatewayGroup.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def update(self):
        """Gets the update of this FSGatewayGroup.  # noqa: E501


        :return: The update of this FSGatewayGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FSGatewayGroup.


        :param update: The update of this FSGatewayGroup.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def user_group_num(self):
        """Gets the user_group_num of this FSGatewayGroup.  # noqa: E501


        :return: The user_group_num of this FSGatewayGroup.  # noqa: E501
        :rtype: int
        """
        return self._user_group_num

    @user_group_num.setter
    def user_group_num(self, user_group_num):
        """Sets the user_group_num of this FSGatewayGroup.


        :param user_group_num: The user_group_num of this FSGatewayGroup.  # noqa: E501
        :type: int
        """

        self._user_group_num = user_group_num

    @property
    def vip(self):
        """Gets the vip of this FSGatewayGroup.  # noqa: E501


        :return: The vip of this FSGatewayGroup.  # noqa: E501
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this FSGatewayGroup.


        :param vip: The vip of this FSGatewayGroup.  # noqa: E501
        :type: str
        """

        self._vip = vip

    @property
    def vip_mask(self):
        """Gets the vip_mask of this FSGatewayGroup.  # noqa: E501


        :return: The vip_mask of this FSGatewayGroup.  # noqa: E501
        :rtype: int
        """
        return self._vip_mask

    @vip_mask.setter
    def vip_mask(self, vip_mask):
        """Sets the vip_mask of this FSGatewayGroup.


        :param vip_mask: The vip_mask of this FSGatewayGroup.  # noqa: E501
        :type: int
        """

        self._vip_mask = vip_mask

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
        if not isinstance(other, FSGatewayGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
