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
# from xms_client.models.dfs_nfs_share_nestview import DfsNFSShareNestview  # noqa: F401,E501


class DfsNFSConnection(object):
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
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'dfs_gateway': 'DfsGatewayNestview',
        'dfs_nfs_share': 'DfsNFSShareNestview',
        'id': 'int',
        'update': 'datetime'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'cluster': 'cluster',
        'create': 'create',
        'dfs_gateway': 'dfs_gateway',
        'dfs_nfs_share': 'dfs_nfs_share',
        'id': 'id',
        'update': 'update'
    }

    def __init__(self, client_ip=None, cluster=None, create=None, dfs_gateway=None, dfs_nfs_share=None, id=None, update=None):  # noqa: E501
        """DfsNFSConnection - a model defined in Swagger"""  # noqa: E501

        self._client_ip = None
        self._cluster = None
        self._create = None
        self._dfs_gateway = None
        self._dfs_nfs_share = None
        self._id = None
        self._update = None
        self.discriminator = None

        if client_ip is not None:
            self.client_ip = client_ip
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if dfs_gateway is not None:
            self.dfs_gateway = dfs_gateway
        if dfs_nfs_share is not None:
            self.dfs_nfs_share = dfs_nfs_share
        if id is not None:
            self.id = id
        if update is not None:
            self.update = update

    @property
    def client_ip(self):
        """Gets the client_ip of this DfsNFSConnection.  # noqa: E501


        :return: The client_ip of this DfsNFSConnection.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this DfsNFSConnection.


        :param client_ip: The client_ip of this DfsNFSConnection.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def cluster(self):
        """Gets the cluster of this DfsNFSConnection.  # noqa: E501


        :return: The cluster of this DfsNFSConnection.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsNFSConnection.


        :param cluster: The cluster of this DfsNFSConnection.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsNFSConnection.  # noqa: E501


        :return: The create of this DfsNFSConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsNFSConnection.


        :param create: The create of this DfsNFSConnection.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dfs_gateway(self):
        """Gets the dfs_gateway of this DfsNFSConnection.  # noqa: E501


        :return: The dfs_gateway of this DfsNFSConnection.  # noqa: E501
        :rtype: DfsGatewayNestview
        """
        return self._dfs_gateway

    @dfs_gateway.setter
    def dfs_gateway(self, dfs_gateway):
        """Sets the dfs_gateway of this DfsNFSConnection.


        :param dfs_gateway: The dfs_gateway of this DfsNFSConnection.  # noqa: E501
        :type: DfsGatewayNestview
        """

        self._dfs_gateway = dfs_gateway

    @property
    def dfs_nfs_share(self):
        """Gets the dfs_nfs_share of this DfsNFSConnection.  # noqa: E501


        :return: The dfs_nfs_share of this DfsNFSConnection.  # noqa: E501
        :rtype: DfsNFSShareNestview
        """
        return self._dfs_nfs_share

    @dfs_nfs_share.setter
    def dfs_nfs_share(self, dfs_nfs_share):
        """Sets the dfs_nfs_share of this DfsNFSConnection.


        :param dfs_nfs_share: The dfs_nfs_share of this DfsNFSConnection.  # noqa: E501
        :type: DfsNFSShareNestview
        """

        self._dfs_nfs_share = dfs_nfs_share

    @property
    def id(self):
        """Gets the id of this DfsNFSConnection.  # noqa: E501


        :return: The id of this DfsNFSConnection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsNFSConnection.


        :param id: The id of this DfsNFSConnection.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def update(self):
        """Gets the update of this DfsNFSConnection.  # noqa: E501


        :return: The update of this DfsNFSConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsNFSConnection.


        :param update: The update of this DfsNFSConnection.  # noqa: E501
        :type: datetime
        """

        self._update = update

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
        if not isinstance(other, DfsNFSConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other