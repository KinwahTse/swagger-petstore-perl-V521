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
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.s3_load_balancer import S3LoadBalancer  # noqa: F401,E501
# from xms_client.models.s3_load_balancer_group_nestview import S3LoadBalancerGroupNestview  # noqa: F401,E501
# from xms_client.models.s3_load_balancer_stat import S3LoadBalancerStat  # noqa: F401,E501
# from xms_client.models.ssl_certificate_nestview import SSLCertificateNestview  # noqa: F401,E501


class S3LoadBalancerRecord(object):
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
        'description': 'str',
        'group': 'S3LoadBalancerGroupNestview',
        'host': 'HostNestview',
        'https_port': 'int',
        'id': 'int',
        'interface_name': 'str',
        'ip': 'str',
        'name': 'str',
        'oss_api_enabled': 'bool',
        'port': 'int',
        'roles': 'list[str]',
        'search_https_port': 'int',
        'search_port': 'int',
        'ssl_certificate': 'SSLCertificateNestview',
        'status': 'str',
        'sync_port': 'int',
        'update': 'datetime',
        'vip': 'str',
        'vip_mask': 'int',
        'vips': 'str',
        'web_service_port': 'int',
        'samples': 'list[S3LoadBalancerStat]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'description': 'description',
        'group': 'group',
        'host': 'host',
        'https_port': 'https_port',
        'id': 'id',
        'interface_name': 'interface_name',
        'ip': 'ip',
        'name': 'name',
        'oss_api_enabled': 'oss_api_enabled',
        'port': 'port',
        'roles': 'roles',
        'search_https_port': 'search_https_port',
        'search_port': 'search_port',
        'ssl_certificate': 'ssl_certificate',
        'status': 'status',
        'sync_port': 'sync_port',
        'update': 'update',
        'vip': 'vip',
        'vip_mask': 'vip_mask',
        'vips': 'vips',
        'web_service_port': 'web_service_port',
        'samples': 'samples'
    }

    def __init__(self, cluster=None, create=None, description=None, group=None, host=None, https_port=None, id=None, interface_name=None, ip=None, name=None, oss_api_enabled=None, port=None, roles=None, search_https_port=None, search_port=None, ssl_certificate=None, status=None, sync_port=None, update=None, vip=None, vip_mask=None, vips=None, web_service_port=None, samples=None):  # noqa: E501
        """S3LoadBalancerRecord - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._description = None
        self._group = None
        self._host = None
        self._https_port = None
        self._id = None
        self._interface_name = None
        self._ip = None
        self._name = None
        self._oss_api_enabled = None
        self._port = None
        self._roles = None
        self._search_https_port = None
        self._search_port = None
        self._ssl_certificate = None
        self._status = None
        self._sync_port = None
        self._update = None
        self._vip = None
        self._vip_mask = None
        self._vips = None
        self._web_service_port = None
        self._samples = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group
        if host is not None:
            self.host = host
        if https_port is not None:
            self.https_port = https_port
        if id is not None:
            self.id = id
        if interface_name is not None:
            self.interface_name = interface_name
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name
        if oss_api_enabled is not None:
            self.oss_api_enabled = oss_api_enabled
        if port is not None:
            self.port = port
        if roles is not None:
            self.roles = roles
        if search_https_port is not None:
            self.search_https_port = search_https_port
        if search_port is not None:
            self.search_port = search_port
        if ssl_certificate is not None:
            self.ssl_certificate = ssl_certificate
        if status is not None:
            self.status = status
        if sync_port is not None:
            self.sync_port = sync_port
        if update is not None:
            self.update = update
        if vip is not None:
            self.vip = vip
        if vip_mask is not None:
            self.vip_mask = vip_mask
        if vips is not None:
            self.vips = vips
        if web_service_port is not None:
            self.web_service_port = web_service_port
        if samples is not None:
            self.samples = samples

    @property
    def cluster(self):
        """Gets the cluster of this S3LoadBalancerRecord.  # noqa: E501


        :return: The cluster of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this S3LoadBalancerRecord.


        :param cluster: The cluster of this S3LoadBalancerRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this S3LoadBalancerRecord.  # noqa: E501


        :return: The create of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this S3LoadBalancerRecord.


        :param create: The create of this S3LoadBalancerRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this S3LoadBalancerRecord.  # noqa: E501


        :return: The description of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this S3LoadBalancerRecord.


        :param description: The description of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group(self):
        """Gets the group of this S3LoadBalancerRecord.  # noqa: E501


        :return: The group of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: S3LoadBalancerGroupNestview
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this S3LoadBalancerRecord.


        :param group: The group of this S3LoadBalancerRecord.  # noqa: E501
        :type: S3LoadBalancerGroupNestview
        """

        self._group = group

    @property
    def host(self):
        """Gets the host of this S3LoadBalancerRecord.  # noqa: E501


        :return: The host of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this S3LoadBalancerRecord.


        :param host: The host of this S3LoadBalancerRecord.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def https_port(self):
        """Gets the https_port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The https_port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this S3LoadBalancerRecord.


        :param https_port: The https_port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._https_port = https_port

    @property
    def id(self):
        """Gets the id of this S3LoadBalancerRecord.  # noqa: E501


        :return: The id of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this S3LoadBalancerRecord.


        :param id: The id of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interface_name(self):
        """Gets the interface_name of this S3LoadBalancerRecord.  # noqa: E501

        the interface where vip is bound, exclusive to ip  # noqa: E501

        :return: The interface_name of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this S3LoadBalancerRecord.

        the interface where vip is bound, exclusive to ip  # noqa: E501

        :param interface_name: The interface_name of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def ip(self):
        """Gets the ip of this S3LoadBalancerRecord.  # noqa: E501

        the interface of ip where vip is bound, exclusive to interface_name  # noqa: E501

        :return: The ip of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this S3LoadBalancerRecord.

        the interface of ip where vip is bound, exclusive to interface_name  # noqa: E501

        :param ip: The ip of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this S3LoadBalancerRecord.  # noqa: E501


        :return: The name of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3LoadBalancerRecord.


        :param name: The name of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oss_api_enabled(self):
        """Gets the oss_api_enabled of this S3LoadBalancerRecord.  # noqa: E501


        :return: The oss_api_enabled of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: bool
        """
        return self._oss_api_enabled

    @oss_api_enabled.setter
    def oss_api_enabled(self, oss_api_enabled):
        """Sets the oss_api_enabled of this S3LoadBalancerRecord.


        :param oss_api_enabled: The oss_api_enabled of this S3LoadBalancerRecord.  # noqa: E501
        :type: bool
        """

        self._oss_api_enabled = oss_api_enabled

    @property
    def port(self):
        """Gets the port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this S3LoadBalancerRecord.


        :param port: The port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def roles(self):
        """Gets the roles of this S3LoadBalancerRecord.  # noqa: E501


        :return: The roles of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this S3LoadBalancerRecord.


        :param roles: The roles of this S3LoadBalancerRecord.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def search_https_port(self):
        """Gets the search_https_port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The search_https_port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._search_https_port

    @search_https_port.setter
    def search_https_port(self, search_https_port):
        """Sets the search_https_port of this S3LoadBalancerRecord.


        :param search_https_port: The search_https_port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._search_https_port = search_https_port

    @property
    def search_port(self):
        """Gets the search_port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The search_port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._search_port

    @search_port.setter
    def search_port(self, search_port):
        """Sets the search_port of this S3LoadBalancerRecord.


        :param search_port: The search_port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._search_port = search_port

    @property
    def ssl_certificate(self):
        """Gets the ssl_certificate of this S3LoadBalancerRecord.  # noqa: E501


        :return: The ssl_certificate of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: SSLCertificateNestview
        """
        return self._ssl_certificate

    @ssl_certificate.setter
    def ssl_certificate(self, ssl_certificate):
        """Sets the ssl_certificate of this S3LoadBalancerRecord.


        :param ssl_certificate: The ssl_certificate of this S3LoadBalancerRecord.  # noqa: E501
        :type: SSLCertificateNestview
        """

        self._ssl_certificate = ssl_certificate

    @property
    def status(self):
        """Gets the status of this S3LoadBalancerRecord.  # noqa: E501


        :return: The status of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this S3LoadBalancerRecord.


        :param status: The status of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sync_port(self):
        """Gets the sync_port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The sync_port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._sync_port

    @sync_port.setter
    def sync_port(self, sync_port):
        """Sets the sync_port of this S3LoadBalancerRecord.


        :param sync_port: The sync_port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._sync_port = sync_port

    @property
    def update(self):
        """Gets the update of this S3LoadBalancerRecord.  # noqa: E501


        :return: The update of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this S3LoadBalancerRecord.


        :param update: The update of this S3LoadBalancerRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def vip(self):
        """Gets the vip of this S3LoadBalancerRecord.  # noqa: E501

        designated(master) vip  # noqa: E501

        :return: The vip of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this S3LoadBalancerRecord.

        designated(master) vip  # noqa: E501

        :param vip: The vip of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._vip = vip

    @property
    def vip_mask(self):
        """Gets the vip_mask of this S3LoadBalancerRecord.  # noqa: E501

        mask of vip, default: 32  # noqa: E501

        :return: The vip_mask of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._vip_mask

    @vip_mask.setter
    def vip_mask(self, vip_mask):
        """Sets the vip_mask of this S3LoadBalancerRecord.

        mask of vip, default: 32  # noqa: E501

        :param vip_mask: The vip_mask of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._vip_mask = vip_mask

    @property
    def vips(self):
        """Gets the vips of this S3LoadBalancerRecord.  # noqa: E501

        current effective vips  # noqa: E501

        :return: The vips of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: str
        """
        return self._vips

    @vips.setter
    def vips(self, vips):
        """Sets the vips of this S3LoadBalancerRecord.

        current effective vips  # noqa: E501

        :param vips: The vips of this S3LoadBalancerRecord.  # noqa: E501
        :type: str
        """

        self._vips = vips

    @property
    def web_service_port(self):
        """Gets the web_service_port of this S3LoadBalancerRecord.  # noqa: E501


        :return: The web_service_port of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: int
        """
        return self._web_service_port

    @web_service_port.setter
    def web_service_port(self, web_service_port):
        """Sets the web_service_port of this S3LoadBalancerRecord.


        :param web_service_port: The web_service_port of this S3LoadBalancerRecord.  # noqa: E501
        :type: int
        """

        self._web_service_port = web_service_port

    @property
    def samples(self):
        """Gets the samples of this S3LoadBalancerRecord.  # noqa: E501


        :return: The samples of this S3LoadBalancerRecord.  # noqa: E501
        :rtype: list[S3LoadBalancerStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this S3LoadBalancerRecord.


        :param samples: The samples of this S3LoadBalancerRecord.  # noqa: E501
        :type: list[S3LoadBalancerStat]
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
        if not isinstance(other, S3LoadBalancerRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
