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


class NFSGateway(object):
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
        'bucket_num': 'int',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'description': 'str',
        'gateway_ip': 'str',
        'gateway_name': 'str',
        'host': 'HostNestview',
        'id': 'int',
        'mount_clients': 'str',
        'mount_num': 'int',
        'name': 'str',
        'port': 'int',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'bucket_num': 'bucket_num',
        'cluster': 'cluster',
        'create': 'create',
        'description': 'description',
        'gateway_ip': 'gateway_ip',
        'gateway_name': 'gateway_name',
        'host': 'host',
        'id': 'id',
        'mount_clients': 'mount_clients',
        'mount_num': 'mount_num',
        'name': 'name',
        'port': 'port',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, bucket_num=None, cluster=None, create=None, description=None, gateway_ip=None, gateway_name=None, host=None, id=None, mount_clients=None, mount_num=None, name=None, port=None, status=None, update=None):  # noqa: E501
        """NFSGateway - a model defined in Swagger"""  # noqa: E501

        self._bucket_num = None
        self._cluster = None
        self._create = None
        self._description = None
        self._gateway_ip = None
        self._gateway_name = None
        self._host = None
        self._id = None
        self._mount_clients = None
        self._mount_num = None
        self._name = None
        self._port = None
        self._status = None
        self._update = None
        self.discriminator = None

        if bucket_num is not None:
            self.bucket_num = bucket_num
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if gateway_name is not None:
            self.gateway_name = gateway_name
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if mount_clients is not None:
            self.mount_clients = mount_clients
        if mount_num is not None:
            self.mount_num = mount_num
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def bucket_num(self):
        """Gets the bucket_num of this NFSGateway.  # noqa: E501


        :return: The bucket_num of this NFSGateway.  # noqa: E501
        :rtype: int
        """
        return self._bucket_num

    @bucket_num.setter
    def bucket_num(self, bucket_num):
        """Sets the bucket_num of this NFSGateway.


        :param bucket_num: The bucket_num of this NFSGateway.  # noqa: E501
        :type: int
        """

        self._bucket_num = bucket_num

    @property
    def cluster(self):
        """Gets the cluster of this NFSGateway.  # noqa: E501


        :return: The cluster of this NFSGateway.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this NFSGateway.


        :param cluster: The cluster of this NFSGateway.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this NFSGateway.  # noqa: E501


        :return: The create of this NFSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this NFSGateway.


        :param create: The create of this NFSGateway.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this NFSGateway.  # noqa: E501


        :return: The description of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NFSGateway.


        :param description: The description of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this NFSGateway.  # noqa: E501


        :return: The gateway_ip of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this NFSGateway.


        :param gateway_ip: The gateway_ip of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

    @property
    def gateway_name(self):
        """Gets the gateway_name of this NFSGateway.  # noqa: E501


        :return: The gateway_name of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, gateway_name):
        """Sets the gateway_name of this NFSGateway.


        :param gateway_name: The gateway_name of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._gateway_name = gateway_name

    @property
    def host(self):
        """Gets the host of this NFSGateway.  # noqa: E501


        :return: The host of this NFSGateway.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this NFSGateway.


        :param host: The host of this NFSGateway.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this NFSGateway.  # noqa: E501


        :return: The id of this NFSGateway.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NFSGateway.


        :param id: The id of this NFSGateway.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mount_clients(self):
        """Gets the mount_clients of this NFSGateway.  # noqa: E501


        :return: The mount_clients of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._mount_clients

    @mount_clients.setter
    def mount_clients(self, mount_clients):
        """Sets the mount_clients of this NFSGateway.


        :param mount_clients: The mount_clients of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._mount_clients = mount_clients

    @property
    def mount_num(self):
        """Gets the mount_num of this NFSGateway.  # noqa: E501


        :return: The mount_num of this NFSGateway.  # noqa: E501
        :rtype: int
        """
        return self._mount_num

    @mount_num.setter
    def mount_num(self, mount_num):
        """Sets the mount_num of this NFSGateway.


        :param mount_num: The mount_num of this NFSGateway.  # noqa: E501
        :type: int
        """

        self._mount_num = mount_num

    @property
    def name(self):
        """Gets the name of this NFSGateway.  # noqa: E501


        :return: The name of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NFSGateway.


        :param name: The name of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this NFSGateway.  # noqa: E501


        :return: The port of this NFSGateway.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NFSGateway.


        :param port: The port of this NFSGateway.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def status(self):
        """Gets the status of this NFSGateway.  # noqa: E501


        :return: The status of this NFSGateway.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NFSGateway.


        :param status: The status of this NFSGateway.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this NFSGateway.  # noqa: E501


        :return: The update of this NFSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this NFSGateway.


        :param update: The update of this NFSGateway.  # noqa: E501
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
        if not isinstance(other, NFSGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
