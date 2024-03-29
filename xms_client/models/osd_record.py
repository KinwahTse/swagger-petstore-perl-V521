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
# from xms_client.models.disk import Disk  # noqa: F401,E501
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.osd import Osd  # noqa: F401,E501
# from xms_client.models.osd_group_nestview import OsdGroupNestview  # noqa: F401,E501
# from xms_client.models.osd_stat import OsdStat  # noqa: F401,E501
# from xms_client.models.partition import Partition  # noqa: F401,E501
# from xms_client.models.pool_nestview import PoolNestview  # noqa: F401,E501


class OsdRecord(object):
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
        'bind_osd_group': 'OsdGroupNestview',
        'bind_pool': 'PoolNestview',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'data_dir': 'str',
        'disk': 'Disk',
        'exit_count': 'int',
        'exit_time': 'datetime',
        'host': 'HostNestview',
        'id': 'int',
        '_in': 'bool',
        'init_time': 'datetime',
        'last_scrub_time': 'datetime',
        'meta_bytes': 'int',
        'min_alloc_size': 'int',
        'name': 'str',
        'numa_node': 'int',
        'omap_byte': 'int',
        'osd_group': 'OsdGroupNestview',
        'osd_id': 'int',
        'partition': 'Partition',
        'pool': 'PoolNestview',
        'read_cache_size': 'int',
        'role': 'str',
        'status': 'str',
        'status_class': 'str',
        'type': 'str',
        'up': 'bool',
        'update': 'datetime',
        'uuid': 'str',
        'samples': 'list[OsdStat]'
    }

    attribute_map = {
        'action_status': 'action_status',
        'bind_osd_group': 'bind_osd_group',
        'bind_pool': 'bind_pool',
        'cluster': 'cluster',
        'create': 'create',
        'data_dir': 'data_dir',
        'disk': 'disk',
        'exit_count': 'exit_count',
        'exit_time': 'exit_time',
        'host': 'host',
        'id': 'id',
        '_in': 'in',
        'init_time': 'init_time',
        'last_scrub_time': 'last_scrub_time',
        'meta_bytes': 'meta_bytes',
        'min_alloc_size': 'min_alloc_size',
        'name': 'name',
        'numa_node': 'numa_node',
        'omap_byte': 'omap_byte',
        'osd_group': 'osd_group',
        'osd_id': 'osd_id',
        'partition': 'partition',
        'pool': 'pool',
        'read_cache_size': 'read_cache_size',
        'role': 'role',
        'status': 'status',
        'status_class': 'status_class',
        'type': 'type',
        'up': 'up',
        'update': 'update',
        'uuid': 'uuid',
        'samples': 'samples'
    }

    def __init__(self, action_status=None, bind_osd_group=None, bind_pool=None, cluster=None, create=None, data_dir=None, disk=None, exit_count=None, exit_time=None, host=None, id=None, _in=None, init_time=None, last_scrub_time=None, meta_bytes=None, min_alloc_size=None, name=None, numa_node=None, omap_byte=None, osd_group=None, osd_id=None, partition=None, pool=None, read_cache_size=None, role=None, status=None, status_class=None, type=None, up=None, update=None, uuid=None, samples=None):  # noqa: E501
        """OsdRecord - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._bind_osd_group = None
        self._bind_pool = None
        self._cluster = None
        self._create = None
        self._data_dir = None
        self._disk = None
        self._exit_count = None
        self._exit_time = None
        self._host = None
        self._id = None
        self.__in = None
        self._init_time = None
        self._last_scrub_time = None
        self._meta_bytes = None
        self._min_alloc_size = None
        self._name = None
        self._numa_node = None
        self._omap_byte = None
        self._osd_group = None
        self._osd_id = None
        self._partition = None
        self._pool = None
        self._read_cache_size = None
        self._role = None
        self._status = None
        self._status_class = None
        self._type = None
        self._up = None
        self._update = None
        self._uuid = None
        self._samples = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if bind_osd_group is not None:
            self.bind_osd_group = bind_osd_group
        if bind_pool is not None:
            self.bind_pool = bind_pool
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if data_dir is not None:
            self.data_dir = data_dir
        if disk is not None:
            self.disk = disk
        if exit_count is not None:
            self.exit_count = exit_count
        if exit_time is not None:
            self.exit_time = exit_time
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if _in is not None:
            self._in = _in
        if init_time is not None:
            self.init_time = init_time
        if last_scrub_time is not None:
            self.last_scrub_time = last_scrub_time
        if meta_bytes is not None:
            self.meta_bytes = meta_bytes
        if min_alloc_size is not None:
            self.min_alloc_size = min_alloc_size
        if name is not None:
            self.name = name
        if numa_node is not None:
            self.numa_node = numa_node
        if omap_byte is not None:
            self.omap_byte = omap_byte
        if osd_group is not None:
            self.osd_group = osd_group
        if osd_id is not None:
            self.osd_id = osd_id
        if partition is not None:
            self.partition = partition
        if pool is not None:
            self.pool = pool
        if read_cache_size is not None:
            self.read_cache_size = read_cache_size
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if status_class is not None:
            self.status_class = status_class
        if type is not None:
            self.type = type
        if up is not None:
            self.up = up
        if update is not None:
            self.update = update
        if uuid is not None:
            self.uuid = uuid
        if samples is not None:
            self.samples = samples

    @property
    def action_status(self):
        """Gets the action_status of this OsdRecord.  # noqa: E501


        :return: The action_status of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this OsdRecord.


        :param action_status: The action_status of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def bind_osd_group(self):
        """Gets the bind_osd_group of this OsdRecord.  # noqa: E501


        :return: The bind_osd_group of this OsdRecord.  # noqa: E501
        :rtype: OsdGroupNestview
        """
        return self._bind_osd_group

    @bind_osd_group.setter
    def bind_osd_group(self, bind_osd_group):
        """Sets the bind_osd_group of this OsdRecord.


        :param bind_osd_group: The bind_osd_group of this OsdRecord.  # noqa: E501
        :type: OsdGroupNestview
        """

        self._bind_osd_group = bind_osd_group

    @property
    def bind_pool(self):
        """Gets the bind_pool of this OsdRecord.  # noqa: E501


        :return: The bind_pool of this OsdRecord.  # noqa: E501
        :rtype: PoolNestview
        """
        return self._bind_pool

    @bind_pool.setter
    def bind_pool(self, bind_pool):
        """Sets the bind_pool of this OsdRecord.


        :param bind_pool: The bind_pool of this OsdRecord.  # noqa: E501
        :type: PoolNestview
        """

        self._bind_pool = bind_pool

    @property
    def cluster(self):
        """Gets the cluster of this OsdRecord.  # noqa: E501


        :return: The cluster of this OsdRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this OsdRecord.


        :param cluster: The cluster of this OsdRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this OsdRecord.  # noqa: E501


        :return: The create of this OsdRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OsdRecord.


        :param create: The create of this OsdRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def data_dir(self):
        """Gets the data_dir of this OsdRecord.  # noqa: E501


        :return: The data_dir of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._data_dir

    @data_dir.setter
    def data_dir(self, data_dir):
        """Sets the data_dir of this OsdRecord.


        :param data_dir: The data_dir of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._data_dir = data_dir

    @property
    def disk(self):
        """Gets the disk of this OsdRecord.  # noqa: E501


        :return: The disk of this OsdRecord.  # noqa: E501
        :rtype: Disk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this OsdRecord.


        :param disk: The disk of this OsdRecord.  # noqa: E501
        :type: Disk
        """

        self._disk = disk

    @property
    def exit_count(self):
        """Gets the exit_count of this OsdRecord.  # noqa: E501


        :return: The exit_count of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._exit_count

    @exit_count.setter
    def exit_count(self, exit_count):
        """Sets the exit_count of this OsdRecord.


        :param exit_count: The exit_count of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._exit_count = exit_count

    @property
    def exit_time(self):
        """Gets the exit_time of this OsdRecord.  # noqa: E501


        :return: The exit_time of this OsdRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._exit_time

    @exit_time.setter
    def exit_time(self, exit_time):
        """Sets the exit_time of this OsdRecord.


        :param exit_time: The exit_time of this OsdRecord.  # noqa: E501
        :type: datetime
        """

        self._exit_time = exit_time

    @property
    def host(self):
        """Gets the host of this OsdRecord.  # noqa: E501


        :return: The host of this OsdRecord.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this OsdRecord.


        :param host: The host of this OsdRecord.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this OsdRecord.  # noqa: E501


        :return: The id of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OsdRecord.


        :param id: The id of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def _in(self):
        """Gets the _in of this OsdRecord.  # noqa: E501


        :return: The _in of this OsdRecord.  # noqa: E501
        :rtype: bool
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this OsdRecord.


        :param _in: The _in of this OsdRecord.  # noqa: E501
        :type: bool
        """

        self.__in = _in

    @property
    def init_time(self):
        """Gets the init_time of this OsdRecord.  # noqa: E501


        :return: The init_time of this OsdRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._init_time

    @init_time.setter
    def init_time(self, init_time):
        """Sets the init_time of this OsdRecord.


        :param init_time: The init_time of this OsdRecord.  # noqa: E501
        :type: datetime
        """

        self._init_time = init_time

    @property
    def last_scrub_time(self):
        """Gets the last_scrub_time of this OsdRecord.  # noqa: E501


        :return: The last_scrub_time of this OsdRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scrub_time

    @last_scrub_time.setter
    def last_scrub_time(self, last_scrub_time):
        """Sets the last_scrub_time of this OsdRecord.


        :param last_scrub_time: The last_scrub_time of this OsdRecord.  # noqa: E501
        :type: datetime
        """

        self._last_scrub_time = last_scrub_time

    @property
    def meta_bytes(self):
        """Gets the meta_bytes of this OsdRecord.  # noqa: E501


        :return: The meta_bytes of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._meta_bytes

    @meta_bytes.setter
    def meta_bytes(self, meta_bytes):
        """Sets the meta_bytes of this OsdRecord.


        :param meta_bytes: The meta_bytes of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._meta_bytes = meta_bytes

    @property
    def min_alloc_size(self):
        """Gets the min_alloc_size of this OsdRecord.  # noqa: E501


        :return: The min_alloc_size of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._min_alloc_size

    @min_alloc_size.setter
    def min_alloc_size(self, min_alloc_size):
        """Sets the min_alloc_size of this OsdRecord.


        :param min_alloc_size: The min_alloc_size of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._min_alloc_size = min_alloc_size

    @property
    def name(self):
        """Gets the name of this OsdRecord.  # noqa: E501


        :return: The name of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OsdRecord.


        :param name: The name of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def numa_node(self):
        """Gets the numa_node of this OsdRecord.  # noqa: E501


        :return: The numa_node of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._numa_node

    @numa_node.setter
    def numa_node(self, numa_node):
        """Sets the numa_node of this OsdRecord.


        :param numa_node: The numa_node of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._numa_node = numa_node

    @property
    def omap_byte(self):
        """Gets the omap_byte of this OsdRecord.  # noqa: E501


        :return: The omap_byte of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._omap_byte

    @omap_byte.setter
    def omap_byte(self, omap_byte):
        """Sets the omap_byte of this OsdRecord.


        :param omap_byte: The omap_byte of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._omap_byte = omap_byte

    @property
    def osd_group(self):
        """Gets the osd_group of this OsdRecord.  # noqa: E501


        :return: The osd_group of this OsdRecord.  # noqa: E501
        :rtype: OsdGroupNestview
        """
        return self._osd_group

    @osd_group.setter
    def osd_group(self, osd_group):
        """Sets the osd_group of this OsdRecord.


        :param osd_group: The osd_group of this OsdRecord.  # noqa: E501
        :type: OsdGroupNestview
        """

        self._osd_group = osd_group

    @property
    def osd_id(self):
        """Gets the osd_id of this OsdRecord.  # noqa: E501


        :return: The osd_id of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._osd_id

    @osd_id.setter
    def osd_id(self, osd_id):
        """Sets the osd_id of this OsdRecord.


        :param osd_id: The osd_id of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._osd_id = osd_id

    @property
    def partition(self):
        """Gets the partition of this OsdRecord.  # noqa: E501


        :return: The partition of this OsdRecord.  # noqa: E501
        :rtype: Partition
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this OsdRecord.


        :param partition: The partition of this OsdRecord.  # noqa: E501
        :type: Partition
        """

        self._partition = partition

    @property
    def pool(self):
        """Gets the pool of this OsdRecord.  # noqa: E501


        :return: The pool of this OsdRecord.  # noqa: E501
        :rtype: PoolNestview
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this OsdRecord.


        :param pool: The pool of this OsdRecord.  # noqa: E501
        :type: PoolNestview
        """

        self._pool = pool

    @property
    def read_cache_size(self):
        """Gets the read_cache_size of this OsdRecord.  # noqa: E501


        :return: The read_cache_size of this OsdRecord.  # noqa: E501
        :rtype: int
        """
        return self._read_cache_size

    @read_cache_size.setter
    def read_cache_size(self, read_cache_size):
        """Sets the read_cache_size of this OsdRecord.


        :param read_cache_size: The read_cache_size of this OsdRecord.  # noqa: E501
        :type: int
        """

        self._read_cache_size = read_cache_size

    @property
    def role(self):
        """Gets the role of this OsdRecord.  # noqa: E501


        :return: The role of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OsdRecord.


        :param role: The role of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def status(self):
        """Gets the status of this OsdRecord.  # noqa: E501


        :return: The status of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OsdRecord.


        :param status: The status of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_class(self):
        """Gets the status_class of this OsdRecord.  # noqa: E501


        :return: The status_class of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._status_class

    @status_class.setter
    def status_class(self, status_class):
        """Sets the status_class of this OsdRecord.


        :param status_class: The status_class of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._status_class = status_class

    @property
    def type(self):
        """Gets the type of this OsdRecord.  # noqa: E501


        :return: The type of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OsdRecord.


        :param type: The type of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def up(self):
        """Gets the up of this OsdRecord.  # noqa: E501


        :return: The up of this OsdRecord.  # noqa: E501
        :rtype: bool
        """
        return self._up

    @up.setter
    def up(self, up):
        """Sets the up of this OsdRecord.


        :param up: The up of this OsdRecord.  # noqa: E501
        :type: bool
        """

        self._up = up

    @property
    def update(self):
        """Gets the update of this OsdRecord.  # noqa: E501


        :return: The update of this OsdRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this OsdRecord.


        :param update: The update of this OsdRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def uuid(self):
        """Gets the uuid of this OsdRecord.  # noqa: E501


        :return: The uuid of this OsdRecord.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this OsdRecord.


        :param uuid: The uuid of this OsdRecord.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def samples(self):
        """Gets the samples of this OsdRecord.  # noqa: E501


        :return: The samples of this OsdRecord.  # noqa: E501
        :rtype: list[OsdStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this OsdRecord.


        :param samples: The samples of this OsdRecord.  # noqa: E501
        :type: list[OsdStat]
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
        if not isinstance(other, OsdRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
