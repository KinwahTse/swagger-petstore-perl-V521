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
# from xms_client.models.fs_gateway_group_nestview import FSGatewayGroupNestview  # noqa: F401,E501
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.network_address_nestview import NetworkAddressNestview  # noqa: F401,E501


class FSGateway(object):
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
        'fs_gateway_group': 'FSGatewayGroupNestview',
        'host': 'HostNestview',
        'id': 'int',
        'network_address': 'NetworkAddressNestview',
        'nic_name': 'str',
        'status': 'str',
        'update': 'datetime',
        'vip': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'fs_gateway_group': 'fs_gateway_group',
        'host': 'host',
        'id': 'id',
        'network_address': 'network_address',
        'nic_name': 'nic_name',
        'status': 'status',
        'update': 'update',
        'vip': 'vip'
    }

    def __init__(self, cluster=None, create=None, fs_gateway_group=None, host=None, id=None, network_address=None, nic_name=None, status=None, update=None, vip=None):  # noqa: E501
        """FSGateway - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._fs_gateway_group = None
        self._host = None
        self._id = None
        self._network_address = None
        self._nic_name = None
        self._status = None
        self._update = None
        self._vip = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if fs_gateway_group is not None:
            self.fs_gateway_group = fs_gateway_group
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if network_address is not None:
            self.network_address = network_address
        if nic_name is not None:
            self.nic_name = nic_name
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if vip is not None:
            self.vip = vip

    @property
    def cluster(self):
        """Gets the cluster of this FSGateway.  # noqa: E501


        :return: The cluster of this FSGateway.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this FSGateway.


        :param cluster: The cluster of this FSGateway.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this FSGateway.  # noqa: E501


        :return: The create of this FSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this FSGateway.


        :param create: The create of this FSGateway.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def fs_gateway_group(self):
        """Gets the fs_gateway_group of this FSGateway.  # noqa: E501


        :return: The fs_gateway_group of this FSGateway.  # noqa: E501
        :rtype: FSGatewayGroupNestview
        """
        return self._fs_gateway_group

    @fs_gateway_group.setter
    def fs_gateway_group(self, fs_gateway_group):
        """Sets the fs_gateway_group of this FSGateway.


        :param fs_gateway_group: The fs_gateway_group of this FSGateway.  # noqa: E501
        :type: FSGatewayGroupNestview
        """

        self._fs_gateway_group = fs_gateway_group

    @property
    def host(self):
        """Gets the host of this FSGateway.  # noqa: E501


        :return: The host of this FSGateway.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this FSGateway.


        :param host: The host of this FSGateway.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this FSGateway.  # noqa: E501


        :return: The id of this FSGateway.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FSGateway.


        :param id: The id of this FSGateway.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def network_address(self):
        """Gets the network_address of this FSGateway.  # noqa: E501


        :return: The network_address of this FSGateway.  # noqa: E501
        :rtype: NetworkAddressNestview
        """
        return self._network_address

    @network_address.setter
    def network_address(self, network_address):
        """Sets the network_address of this FSGateway.


        :param network_address: The network_address of this FSGateway.  # noqa: E501
        :type: NetworkAddressNestview
        """

        self._network_address = network_address

    @property
    def nic_name(self):
        """Gets the nic_name of this FSGateway.  # noqa: E501


        :return: The nic_name of this FSGateway.  # noqa: E501
        :rtype: str
        """
        return self._nic_name

    @nic_name.setter
    def nic_name(self, nic_name):
        """Sets the nic_name of this FSGateway.


        :param nic_name: The nic_name of this FSGateway.  # noqa: E501
        :type: str
        """

        self._nic_name = nic_name

    @property
    def status(self):
        """Gets the status of this FSGateway.  # noqa: E501


        :return: The status of this FSGateway.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FSGateway.


        :param status: The status of this FSGateway.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this FSGateway.  # noqa: E501


        :return: The update of this FSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FSGateway.


        :param update: The update of this FSGateway.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def vip(self):
        """Gets the vip of this FSGateway.  # noqa: E501


        :return: The vip of this FSGateway.  # noqa: E501
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this FSGateway.


        :param vip: The vip of this FSGateway.  # noqa: E501
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
        if not isinstance(other, FSGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
