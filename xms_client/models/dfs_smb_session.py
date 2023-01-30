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
# from xms_client.models.dfs_gateway_nestview import DfsGatewayNestview  # noqa: F401,E501
# from xms_client.models.dfs_smb_share_nestview import DfsSMBShareNestview  # noqa: F401,E501


class DfsSMBSession(object):
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
        'client_ip': 'str',
        'client_port': 'int',
        'cluster': 'ClusterNestview',
        'connected_at': 'datetime',
        'create': 'datetime',
        'dfs_gateway': 'DfsGatewayNestview',
        'dfs_smb_share': 'DfsSMBShareNestview',
        'group': 'str',
        'id': 'int',
        'protocol_version': 'str',
        'update': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'client_port': 'client_port',
        'cluster': 'cluster',
        'connected_at': 'connected_at',
        'create': 'create',
        'dfs_gateway': 'dfs_gateway',
        'dfs_smb_share': 'dfs_smb_share',
        'group': 'group',
        'id': 'id',
        'protocol_version': 'protocol_version',
        'update': 'update',
        'username': 'username'
    }

    def __init__(self, client_ip=None, client_port=None, cluster=None, connected_at=None, create=None, dfs_gateway=None, dfs_smb_share=None, group=None, id=None, protocol_version=None, update=None, username=None):  # noqa: E501
        """DfsSMBSession - a model defined in Swagger"""  # noqa: E501

        self._client_ip = None
        self._client_port = None
        self._cluster = None
        self._connected_at = None
        self._create = None
        self._dfs_gateway = None
        self._dfs_smb_share = None
        self._group = None
        self._id = None
        self._protocol_version = None
        self._update = None
        self._username = None
        self.discriminator = None

        if client_ip is not None:
            self.client_ip = client_ip
        if client_port is not None:
            self.client_port = client_port
        if cluster is not None:
            self.cluster = cluster
        if connected_at is not None:
            self.connected_at = connected_at
        if create is not None:
            self.create = create
        if dfs_gateway is not None:
            self.dfs_gateway = dfs_gateway
        if dfs_smb_share is not None:
            self.dfs_smb_share = dfs_smb_share
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if update is not None:
            self.update = update
        if username is not None:
            self.username = username

    @property
    def client_ip(self):
        """Gets the client_ip of this DfsSMBSession.  # noqa: E501


        :return: The client_ip of this DfsSMBSession.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this DfsSMBSession.


        :param client_ip: The client_ip of this DfsSMBSession.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def client_port(self):
        """Gets the client_port of this DfsSMBSession.  # noqa: E501


        :return: The client_port of this DfsSMBSession.  # noqa: E501
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        """Sets the client_port of this DfsSMBSession.


        :param client_port: The client_port of this DfsSMBSession.  # noqa: E501
        :type: int
        """

        self._client_port = client_port

    @property
    def cluster(self):
        """Gets the cluster of this DfsSMBSession.  # noqa: E501


        :return: The cluster of this DfsSMBSession.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsSMBSession.


        :param cluster: The cluster of this DfsSMBSession.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def connected_at(self):
        """Gets the connected_at of this DfsSMBSession.  # noqa: E501


        :return: The connected_at of this DfsSMBSession.  # noqa: E501
        :rtype: datetime
        """
        return self._connected_at

    @connected_at.setter
    def connected_at(self, connected_at):
        """Sets the connected_at of this DfsSMBSession.


        :param connected_at: The connected_at of this DfsSMBSession.  # noqa: E501
        :type: datetime
        """

        self._connected_at = connected_at

    @property
    def create(self):
        """Gets the create of this DfsSMBSession.  # noqa: E501


        :return: The create of this DfsSMBSession.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsSMBSession.


        :param create: The create of this DfsSMBSession.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dfs_gateway(self):
        """Gets the dfs_gateway of this DfsSMBSession.  # noqa: E501


        :return: The dfs_gateway of this DfsSMBSession.  # noqa: E501
        :rtype: DfsGatewayNestview
        """
        return self._dfs_gateway

    @dfs_gateway.setter
    def dfs_gateway(self, dfs_gateway):
        """Sets the dfs_gateway of this DfsSMBSession.


        :param dfs_gateway: The dfs_gateway of this DfsSMBSession.  # noqa: E501
        :type: DfsGatewayNestview
        """

        self._dfs_gateway = dfs_gateway

    @property
    def dfs_smb_share(self):
        """Gets the dfs_smb_share of this DfsSMBSession.  # noqa: E501


        :return: The dfs_smb_share of this DfsSMBSession.  # noqa: E501
        :rtype: DfsSMBShareNestview
        """
        return self._dfs_smb_share

    @dfs_smb_share.setter
    def dfs_smb_share(self, dfs_smb_share):
        """Sets the dfs_smb_share of this DfsSMBSession.


        :param dfs_smb_share: The dfs_smb_share of this DfsSMBSession.  # noqa: E501
        :type: DfsSMBShareNestview
        """

        self._dfs_smb_share = dfs_smb_share

    @property
    def group(self):
        """Gets the group of this DfsSMBSession.  # noqa: E501


        :return: The group of this DfsSMBSession.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DfsSMBSession.


        :param group: The group of this DfsSMBSession.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def id(self):
        """Gets the id of this DfsSMBSession.  # noqa: E501


        :return: The id of this DfsSMBSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsSMBSession.


        :param id: The id of this DfsSMBSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def protocol_version(self):
        """Gets the protocol_version of this DfsSMBSession.  # noqa: E501


        :return: The protocol_version of this DfsSMBSession.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this DfsSMBSession.


        :param protocol_version: The protocol_version of this DfsSMBSession.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    @property
    def update(self):
        """Gets the update of this DfsSMBSession.  # noqa: E501


        :return: The update of this DfsSMBSession.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsSMBSession.


        :param update: The update of this DfsSMBSession.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def username(self):
        """Gets the username of this DfsSMBSession.  # noqa: E501


        :return: The username of this DfsSMBSession.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DfsSMBSession.


        :param username: The username of this DfsSMBSession.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, DfsSMBSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other