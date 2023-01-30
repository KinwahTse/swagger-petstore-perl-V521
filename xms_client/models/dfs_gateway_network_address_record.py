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
# from xms_client.models.dfs_gateway import DfsGateway  # noqa: F401,E501
# from xms_client.models.dfs_gateway_network_address import DfsGatewayNetworkAddress  # noqa: F401,E501
# from xms_client.models.dfs_gateway_stat import DfsGatewayStat  # noqa: F401,E501
# from xms_client.models.dfs_gateway_zone_nestview import DfsGatewayZoneNestview  # noqa: F401,E501
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.network_address_nestview import NetworkAddressNestview  # noqa: F401,E501


class DfsGatewayNetworkAddressRecord(object):
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
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'dfs_gateway': 'DfsGateway',
        'dfs_gateway_zone': 'DfsGatewayZoneNestview',
        'host': 'HostNestview',
        'id': 'int',
        'network_address': 'NetworkAddressNestview',
        'update': 'datetime',
        'samples': 'list[DfsGatewayStat]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'dfs_gateway': 'dfs_gateway',
        'dfs_gateway_zone': 'dfs_gateway_zone',
        'host': 'host',
        'id': 'id',
        'network_address': 'network_address',
        'update': 'update',
        'samples': 'samples'
    }

    def __init__(self, cluster=None, create=None, dfs_gateway=None, dfs_gateway_zone=None, host=None, id=None, network_address=None, update=None, samples=None):  # noqa: E501
        """DfsGatewayNetworkAddressRecord - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._dfs_gateway = None
        self._dfs_gateway_zone = None
        self._host = None
        self._id = None
        self._network_address = None
        self._update = None
        self._samples = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if dfs_gateway is not None:
            self.dfs_gateway = dfs_gateway
        if dfs_gateway_zone is not None:
            self.dfs_gateway_zone = dfs_gateway_zone
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if network_address is not None:
            self.network_address = network_address
        if update is not None:
            self.update = update
        if samples is not None:
            self.samples = samples

    @property
    def cluster(self):
        """Gets the cluster of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The cluster of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsGatewayNetworkAddressRecord.


        :param cluster: The cluster of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The create of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsGatewayNetworkAddressRecord.


        :param create: The create of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dfs_gateway(self):
        """Gets the dfs_gateway of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The dfs_gateway of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: DfsGateway
        """
        return self._dfs_gateway

    @dfs_gateway.setter
    def dfs_gateway(self, dfs_gateway):
        """Sets the dfs_gateway of this DfsGatewayNetworkAddressRecord.


        :param dfs_gateway: The dfs_gateway of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: DfsGateway
        """

        self._dfs_gateway = dfs_gateway

    @property
    def dfs_gateway_zone(self):
        """Gets the dfs_gateway_zone of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The dfs_gateway_zone of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: DfsGatewayZoneNestview
        """
        return self._dfs_gateway_zone

    @dfs_gateway_zone.setter
    def dfs_gateway_zone(self, dfs_gateway_zone):
        """Sets the dfs_gateway_zone of this DfsGatewayNetworkAddressRecord.


        :param dfs_gateway_zone: The dfs_gateway_zone of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: DfsGatewayZoneNestview
        """

        self._dfs_gateway_zone = dfs_gateway_zone

    @property
    def host(self):
        """Gets the host of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The host of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DfsGatewayNetworkAddressRecord.


        :param host: The host of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The id of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsGatewayNetworkAddressRecord.


        :param id: The id of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def network_address(self):
        """Gets the network_address of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The network_address of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: NetworkAddressNestview
        """
        return self._network_address

    @network_address.setter
    def network_address(self, network_address):
        """Sets the network_address of this DfsGatewayNetworkAddressRecord.


        :param network_address: The network_address of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: NetworkAddressNestview
        """

        self._network_address = network_address

    @property
    def update(self):
        """Gets the update of this DfsGatewayNetworkAddressRecord.  # noqa: E501


        :return: The update of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsGatewayNetworkAddressRecord.


        :param update: The update of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def samples(self):
        """Gets the samples of this DfsGatewayNetworkAddressRecord.  # noqa: E501

        TODO(liubo): next version maybe change to DfsGatewayNetworkAddressStat  # noqa: E501

        :return: The samples of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :rtype: list[DfsGatewayStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this DfsGatewayNetworkAddressRecord.

        TODO(liubo): next version maybe change to DfsGatewayNetworkAddressStat  # noqa: E501

        :param samples: The samples of this DfsGatewayNetworkAddressRecord.  # noqa: E501
        :type: list[DfsGatewayStat]
        """

        self._samples = samples

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
        if not isinstance(other, DfsGatewayNetworkAddressRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
