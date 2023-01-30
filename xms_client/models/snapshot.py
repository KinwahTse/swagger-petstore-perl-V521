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
# from xms_client.models.consistent_snapshot_nestview import ConsistentSnapshotNestview  # noqa: F401,E501
# from xms_client.models.pool_nestview import PoolNestview  # noqa: F401,E501
# from xms_client.models.remote_cluster_nestview import RemoteClusterNestview  # noqa: F401,E501
# from xms_client.models.volume_group_snapshot_nestview import VolumeGroupSnapshotNestview  # noqa: F401,E501
# from xms_client.models.volume_nestview import VolumeNestview  # noqa: F401,E501


class Snapshot(object):
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
        'allocated_size': 'int',
        'block_consistent_snapshot': 'ConsistentSnapshotNestview',
        'block_volume_group_snapshot': 'VolumeGroupSnapshotNestview',
        'cloned_block_volume_num': 'int',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'creator': 'str',
        'description': 'str',
        'hidden': 'bool',
        'id': 'int',
        'name': 'str',
        'passive': 'bool',
        'pool': 'PoolNestview',
        'protected': 'bool',
        'remote_cluster': 'RemoteClusterNestview',
        'reserved': 'bool',
        'size': 'int',
        'snap_name': 'str',
        'status': 'str',
        'uid': 'str',
        'update': 'datetime',
        'volume': 'VolumeNestview'
    }

    attribute_map = {
        'action_status': 'action_status',
        'allocated_size': 'allocated_size',
        'block_consistent_snapshot': 'block_consistent_snapshot',
        'block_volume_group_snapshot': 'block_volume_group_snapshot',
        'cloned_block_volume_num': 'cloned_block_volume_num',
        'cluster': 'cluster',
        'create': 'create',
        'creator': 'creator',
        'description': 'description',
        'hidden': 'hidden',
        'id': 'id',
        'name': 'name',
        'passive': 'passive',
        'pool': 'pool',
        'protected': 'protected',
        'remote_cluster': 'remote_cluster',
        'reserved': 'reserved',
        'size': 'size',
        'snap_name': 'snap_name',
        'status': 'status',
        'uid': 'uid',
        'update': 'update',
        'volume': 'volume'
    }

    def __init__(self, action_status=None, allocated_size=None, block_consistent_snapshot=None, block_volume_group_snapshot=None, cloned_block_volume_num=None, cluster=None, create=None, creator=None, description=None, hidden=None, id=None, name=None, passive=None, pool=None, protected=None, remote_cluster=None, reserved=None, size=None, snap_name=None, status=None, uid=None, update=None, volume=None):  # noqa: E501
        """Snapshot - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._allocated_size = None
        self._block_consistent_snapshot = None
        self._block_volume_group_snapshot = None
        self._cloned_block_volume_num = None
        self._cluster = None
        self._create = None
        self._creator = None
        self._description = None
        self._hidden = None
        self._id = None
        self._name = None
        self._passive = None
        self._pool = None
        self._protected = None
        self._remote_cluster = None
        self._reserved = None
        self._size = None
        self._snap_name = None
        self._status = None
        self._uid = None
        self._update = None
        self._volume = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if allocated_size is not None:
            self.allocated_size = allocated_size
        if block_consistent_snapshot is not None:
            self.block_consistent_snapshot = block_consistent_snapshot
        if block_volume_group_snapshot is not None:
            self.block_volume_group_snapshot = block_volume_group_snapshot
        if cloned_block_volume_num is not None:
            self.cloned_block_volume_num = cloned_block_volume_num
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if passive is not None:
            self.passive = passive
        if pool is not None:
            self.pool = pool
        if protected is not None:
            self.protected = protected
        if remote_cluster is not None:
            self.remote_cluster = remote_cluster
        if reserved is not None:
            self.reserved = reserved
        if size is not None:
            self.size = size
        if snap_name is not None:
            self.snap_name = snap_name
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid
        if update is not None:
            self.update = update
        if volume is not None:
            self.volume = volume

    @property
    def action_status(self):
        """Gets the action_status of this Snapshot.  # noqa: E501


        :return: The action_status of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this Snapshot.


        :param action_status: The action_status of this Snapshot.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def allocated_size(self):
        """Gets the allocated_size of this Snapshot.  # noqa: E501


        :return: The allocated_size of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._allocated_size

    @allocated_size.setter
    def allocated_size(self, allocated_size):
        """Sets the allocated_size of this Snapshot.


        :param allocated_size: The allocated_size of this Snapshot.  # noqa: E501
        :type: int
        """

        self._allocated_size = allocated_size

    @property
    def block_consistent_snapshot(self):
        """Gets the block_consistent_snapshot of this Snapshot.  # noqa: E501


        :return: The block_consistent_snapshot of this Snapshot.  # noqa: E501
        :rtype: ConsistentSnapshotNestview
        """
        return self._block_consistent_snapshot

    @block_consistent_snapshot.setter
    def block_consistent_snapshot(self, block_consistent_snapshot):
        """Sets the block_consistent_snapshot of this Snapshot.


        :param block_consistent_snapshot: The block_consistent_snapshot of this Snapshot.  # noqa: E501
        :type: ConsistentSnapshotNestview
        """

        self._block_consistent_snapshot = block_consistent_snapshot

    @property
    def block_volume_group_snapshot(self):
        """Gets the block_volume_group_snapshot of this Snapshot.  # noqa: E501


        :return: The block_volume_group_snapshot of this Snapshot.  # noqa: E501
        :rtype: VolumeGroupSnapshotNestview
        """
        return self._block_volume_group_snapshot

    @block_volume_group_snapshot.setter
    def block_volume_group_snapshot(self, block_volume_group_snapshot):
        """Sets the block_volume_group_snapshot of this Snapshot.


        :param block_volume_group_snapshot: The block_volume_group_snapshot of this Snapshot.  # noqa: E501
        :type: VolumeGroupSnapshotNestview
        """

        self._block_volume_group_snapshot = block_volume_group_snapshot

    @property
    def cloned_block_volume_num(self):
        """Gets the cloned_block_volume_num of this Snapshot.  # noqa: E501


        :return: The cloned_block_volume_num of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._cloned_block_volume_num

    @cloned_block_volume_num.setter
    def cloned_block_volume_num(self, cloned_block_volume_num):
        """Sets the cloned_block_volume_num of this Snapshot.


        :param cloned_block_volume_num: The cloned_block_volume_num of this Snapshot.  # noqa: E501
        :type: int
        """

        self._cloned_block_volume_num = cloned_block_volume_num

    @property
    def cluster(self):
        """Gets the cluster of this Snapshot.  # noqa: E501


        :return: The cluster of this Snapshot.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Snapshot.


        :param cluster: The cluster of this Snapshot.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this Snapshot.  # noqa: E501


        :return: The create of this Snapshot.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this Snapshot.


        :param create: The create of this Snapshot.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def creator(self):
        """Gets the creator of this Snapshot.  # noqa: E501


        :return: The creator of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Snapshot.


        :param creator: The creator of this Snapshot.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this Snapshot.  # noqa: E501


        :return: The description of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Snapshot.


        :param description: The description of this Snapshot.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this Snapshot.  # noqa: E501


        :return: The hidden of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Snapshot.


        :param hidden: The hidden of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this Snapshot.  # noqa: E501


        :return: The id of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Snapshot.


        :param id: The id of this Snapshot.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Snapshot.  # noqa: E501


        :return: The name of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshot.


        :param name: The name of this Snapshot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def passive(self):
        """Gets the passive of this Snapshot.  # noqa: E501


        :return: The passive of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._passive

    @passive.setter
    def passive(self, passive):
        """Sets the passive of this Snapshot.


        :param passive: The passive of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._passive = passive

    @property
    def pool(self):
        """Gets the pool of this Snapshot.  # noqa: E501


        :return: The pool of this Snapshot.  # noqa: E501
        :rtype: PoolNestview
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Snapshot.


        :param pool: The pool of this Snapshot.  # noqa: E501
        :type: PoolNestview
        """

        self._pool = pool

    @property
    def protected(self):
        """Gets the protected of this Snapshot.  # noqa: E501


        :return: The protected of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this Snapshot.


        :param protected: The protected of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._protected = protected

    @property
    def remote_cluster(self):
        """Gets the remote_cluster of this Snapshot.  # noqa: E501

        the snapshot is replicated from a remote cluster  # noqa: E501

        :return: The remote_cluster of this Snapshot.  # noqa: E501
        :rtype: RemoteClusterNestview
        """
        return self._remote_cluster

    @remote_cluster.setter
    def remote_cluster(self, remote_cluster):
        """Sets the remote_cluster of this Snapshot.

        the snapshot is replicated from a remote cluster  # noqa: E501

        :param remote_cluster: The remote_cluster of this Snapshot.  # noqa: E501
        :type: RemoteClusterNestview
        """

        self._remote_cluster = remote_cluster

    @property
    def reserved(self):
        """Gets the reserved of this Snapshot.  # noqa: E501


        :return: The reserved of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this Snapshot.


        :param reserved: The reserved of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._reserved = reserved

    @property
    def size(self):
        """Gets the size of this Snapshot.  # noqa: E501


        :return: The size of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Snapshot.


        :param size: The size of this Snapshot.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def snap_name(self):
        """Gets the snap_name of this Snapshot.  # noqa: E501


        :return: The snap_name of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._snap_name

    @snap_name.setter
    def snap_name(self, snap_name):
        """Sets the snap_name of this Snapshot.


        :param snap_name: The snap_name of this Snapshot.  # noqa: E501
        :type: str
        """

        self._snap_name = snap_name

    @property
    def status(self):
        """Gets the status of this Snapshot.  # noqa: E501


        :return: The status of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Snapshot.


        :param status: The status of this Snapshot.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this Snapshot.  # noqa: E501


        :return: The uid of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Snapshot.


        :param uid: The uid of this Snapshot.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def update(self):
        """Gets the update of this Snapshot.  # noqa: E501


        :return: The update of this Snapshot.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this Snapshot.


        :param update: The update of this Snapshot.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def volume(self):
        """Gets the volume of this Snapshot.  # noqa: E501


        :return: The volume of this Snapshot.  # noqa: E501
        :rtype: VolumeNestview
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Snapshot.


        :param volume: The volume of this Snapshot.  # noqa: E501
        :type: VolumeNestview
        """

        self._volume = volume

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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
