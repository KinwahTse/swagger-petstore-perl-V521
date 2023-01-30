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
# from xms_client.models.dfs_gateway_group_nestview import DfsGatewayGroupNestview  # noqa: F401,E501
# from xms_client.models.dfs_hdfs import DfsHdfs  # noqa: F401,E501
# from xms_client.models.dns_domain_name import DNSDomainName  # noqa: F401,E501


class DfsGatewayZone(object):
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
        'default': 'bool',
        'dfs_gateway_group': 'DfsGatewayGroupNestview',
        'dfs_hdfses': 'list[DfsHdfs]',
        'dns_domain_names': 'list[DNSDomainName]',
        'gateway_num': 'int',
        'id': 'int',
        'name': 'str',
        'status': 'str',
        'update': 'datetime',
        'vip_balance_status': 'str',
        'vip_gateways': 'list[str]',
        'vip_num': 'int'
    }

    attribute_map = {
        'action_status': 'action_status',
        'cluster': 'cluster',
        'create': 'create',
        'default': 'default',
        'dfs_gateway_group': 'dfs_gateway_group',
        'dfs_hdfses': 'dfs_hdfses',
        'dns_domain_names': 'dns_domain_names',
        'gateway_num': 'gateway_num',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'update': 'update',
        'vip_balance_status': 'vip_balance_status',
        'vip_gateways': 'vip_gateways',
        'vip_num': 'vip_num'
    }

    def __init__(self, action_status=None, cluster=None, create=None, default=None, dfs_gateway_group=None, dfs_hdfses=None, dns_domain_names=None, gateway_num=None, id=None, name=None, status=None, update=None, vip_balance_status=None, vip_gateways=None, vip_num=None):  # noqa: E501
        """DfsGatewayZone - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._cluster = None
        self._create = None
        self._default = None
        self._dfs_gateway_group = None
        self._dfs_hdfses = None
        self._dns_domain_names = None
        self._gateway_num = None
        self._id = None
        self._name = None
        self._status = None
        self._update = None
        self._vip_balance_status = None
        self._vip_gateways = None
        self._vip_num = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if default is not None:
            self.default = default
        if dfs_gateway_group is not None:
            self.dfs_gateway_group = dfs_gateway_group
        if dfs_hdfses is not None:
            self.dfs_hdfses = dfs_hdfses
        if dns_domain_names is not None:
            self.dns_domain_names = dns_domain_names
        if gateway_num is not None:
            self.gateway_num = gateway_num
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if vip_balance_status is not None:
            self.vip_balance_status = vip_balance_status
        if vip_gateways is not None:
            self.vip_gateways = vip_gateways
        if vip_num is not None:
            self.vip_num = vip_num

    @property
    def action_status(self):
        """Gets the action_status of this DfsGatewayZone.  # noqa: E501


        :return: The action_status of this DfsGatewayZone.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this DfsGatewayZone.


        :param action_status: The action_status of this DfsGatewayZone.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def cluster(self):
        """Gets the cluster of this DfsGatewayZone.  # noqa: E501


        :return: The cluster of this DfsGatewayZone.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsGatewayZone.


        :param cluster: The cluster of this DfsGatewayZone.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsGatewayZone.  # noqa: E501


        :return: The create of this DfsGatewayZone.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsGatewayZone.


        :param create: The create of this DfsGatewayZone.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def default(self):
        """Gets the default of this DfsGatewayZone.  # noqa: E501


        :return: The default of this DfsGatewayZone.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DfsGatewayZone.


        :param default: The default of this DfsGatewayZone.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def dfs_gateway_group(self):
        """Gets the dfs_gateway_group of this DfsGatewayZone.  # noqa: E501


        :return: The dfs_gateway_group of this DfsGatewayZone.  # noqa: E501
        :rtype: DfsGatewayGroupNestview
        """
        return self._dfs_gateway_group

    @dfs_gateway_group.setter
    def dfs_gateway_group(self, dfs_gateway_group):
        """Sets the dfs_gateway_group of this DfsGatewayZone.


        :param dfs_gateway_group: The dfs_gateway_group of this DfsGatewayZone.  # noqa: E501
        :type: DfsGatewayGroupNestview
        """

        self._dfs_gateway_group = dfs_gateway_group

    @property
    def dfs_hdfses(self):
        """Gets the dfs_hdfses of this DfsGatewayZone.  # noqa: E501


        :return: The dfs_hdfses of this DfsGatewayZone.  # noqa: E501
        :rtype: list[DfsHdfs]
        """
        return self._dfs_hdfses

    @dfs_hdfses.setter
    def dfs_hdfses(self, dfs_hdfses):
        """Sets the dfs_hdfses of this DfsGatewayZone.


        :param dfs_hdfses: The dfs_hdfses of this DfsGatewayZone.  # noqa: E501
        :type: list[DfsHdfs]
        """

        self._dfs_hdfses = dfs_hdfses

    @property
    def dns_domain_names(self):
        """Gets the dns_domain_names of this DfsGatewayZone.  # noqa: E501


        :return: The dns_domain_names of this DfsGatewayZone.  # noqa: E501
        :rtype: list[DNSDomainName]
        """
        return self._dns_domain_names

    @dns_domain_names.setter
    def dns_domain_names(self, dns_domain_names):
        """Sets the dns_domain_names of this DfsGatewayZone.


        :param dns_domain_names: The dns_domain_names of this DfsGatewayZone.  # noqa: E501
        :type: list[DNSDomainName]
        """

        self._dns_domain_names = dns_domain_names

    @property
    def gateway_num(self):
        """Gets the gateway_num of this DfsGatewayZone.  # noqa: E501


        :return: The gateway_num of this DfsGatewayZone.  # noqa: E501
        :rtype: int
        """
        return self._gateway_num

    @gateway_num.setter
    def gateway_num(self, gateway_num):
        """Sets the gateway_num of this DfsGatewayZone.


        :param gateway_num: The gateway_num of this DfsGatewayZone.  # noqa: E501
        :type: int
        """

        self._gateway_num = gateway_num

    @property
    def id(self):
        """Gets the id of this DfsGatewayZone.  # noqa: E501


        :return: The id of this DfsGatewayZone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsGatewayZone.


        :param id: The id of this DfsGatewayZone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DfsGatewayZone.  # noqa: E501


        :return: The name of this DfsGatewayZone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DfsGatewayZone.


        :param name: The name of this DfsGatewayZone.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this DfsGatewayZone.  # noqa: E501


        :return: The status of this DfsGatewayZone.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DfsGatewayZone.


        :param status: The status of this DfsGatewayZone.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this DfsGatewayZone.  # noqa: E501


        :return: The update of this DfsGatewayZone.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsGatewayZone.


        :param update: The update of this DfsGatewayZone.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def vip_balance_status(self):
        """Gets the vip_balance_status of this DfsGatewayZone.  # noqa: E501


        :return: The vip_balance_status of this DfsGatewayZone.  # noqa: E501
        :rtype: str
        """
        return self._vip_balance_status

    @vip_balance_status.setter
    def vip_balance_status(self, vip_balance_status):
        """Sets the vip_balance_status of this DfsGatewayZone.


        :param vip_balance_status: The vip_balance_status of this DfsGatewayZone.  # noqa: E501
        :type: str
        """

        self._vip_balance_status = vip_balance_status

    @property
    def vip_gateways(self):
        """Gets the vip_gateways of this DfsGatewayZone.  # noqa: E501

        gateways for VIP addresses in policy routing  # noqa: E501

        :return: The vip_gateways of this DfsGatewayZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._vip_gateways

    @vip_gateways.setter
    def vip_gateways(self, vip_gateways):
        """Sets the vip_gateways of this DfsGatewayZone.

        gateways for VIP addresses in policy routing  # noqa: E501

        :param vip_gateways: The vip_gateways of this DfsGatewayZone.  # noqa: E501
        :type: list[str]
        """

        self._vip_gateways = vip_gateways

    @property
    def vip_num(self):
        """Gets the vip_num of this DfsGatewayZone.  # noqa: E501


        :return: The vip_num of this DfsGatewayZone.  # noqa: E501
        :rtype: int
        """
        return self._vip_num

    @vip_num.setter
    def vip_num(self, vip_num):
        """Sets the vip_num of this DfsGatewayZone.


        :param vip_num: The vip_num of this DfsGatewayZone.  # noqa: E501
        :type: int
        """

        self._vip_num = vip_num

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
        if not isinstance(other, DfsGatewayZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
