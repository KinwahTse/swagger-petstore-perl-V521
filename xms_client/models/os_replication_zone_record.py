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
# from xms_client.models.object_storage_bucket_nestview import ObjectStorageBucketNestview  # noqa: F401,E501
# from xms_client.models.object_storage_zone_nestview import ObjectStorageZoneNestview  # noqa: F401,E501
# from xms_client.models.os_remote_policy_nestview import OSRemotePolicyNestview  # noqa: F401,E501
# from xms_client.models.os_replication_zone import OSReplicationZone  # noqa: F401,E501
# from xms_client.models.os_replication_zone_stat import OSReplicationZoneStat  # noqa: F401,E501
# from xms_client.models.remote_cluster_nestview import RemoteClusterNestview  # noqa: F401,E501


class OSReplicationZoneRecord(object):
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
        'dirty': 'bool',
        'os_bucket': 'ObjectStorageBucketNestview',
        'os_bucket_owner_cluster': 'RemoteClusterNestview',
        'os_bucket_owner_zone': 'ObjectStorageZoneNestview',
        'os_remote_policy': 'OSRemotePolicyNestview',
        'os_remote_policy_uuid': 'str',
        'os_replication_path_num': 'int',
        'os_zone': 'ObjectStorageZoneNestview',
        'os_zone_uuid': 'str',
        'readonly': 'bool',
        'replication_uuid': 'str',
        'status': 'str',
        'update': 'datetime',
        'uuid': 'str',
        'samples': 'list[OSReplicationZoneStat]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'dirty': 'dirty',
        'os_bucket': 'os_bucket',
        'os_bucket_owner_cluster': 'os_bucket_owner_cluster',
        'os_bucket_owner_zone': 'os_bucket_owner_zone',
        'os_remote_policy': 'os_remote_policy',
        'os_remote_policy_uuid': 'os_remote_policy_uuid',
        'os_replication_path_num': 'os_replication_path_num',
        'os_zone': 'os_zone',
        'os_zone_uuid': 'os_zone_uuid',
        'readonly': 'readonly',
        'replication_uuid': 'replication_uuid',
        'status': 'status',
        'update': 'update',
        'uuid': 'uuid',
        'samples': 'samples'
    }

    def __init__(self, cluster=None, create=None, dirty=None, os_bucket=None, os_bucket_owner_cluster=None, os_bucket_owner_zone=None, os_remote_policy=None, os_remote_policy_uuid=None, os_replication_path_num=None, os_zone=None, os_zone_uuid=None, readonly=None, replication_uuid=None, status=None, update=None, uuid=None, samples=None):  # noqa: E501
        """OSReplicationZoneRecord - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._dirty = None
        self._os_bucket = None
        self._os_bucket_owner_cluster = None
        self._os_bucket_owner_zone = None
        self._os_remote_policy = None
        self._os_remote_policy_uuid = None
        self._os_replication_path_num = None
        self._os_zone = None
        self._os_zone_uuid = None
        self._readonly = None
        self._replication_uuid = None
        self._status = None
        self._update = None
        self._uuid = None
        self._samples = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if dirty is not None:
            self.dirty = dirty
        if os_bucket is not None:
            self.os_bucket = os_bucket
        if os_bucket_owner_cluster is not None:
            self.os_bucket_owner_cluster = os_bucket_owner_cluster
        if os_bucket_owner_zone is not None:
            self.os_bucket_owner_zone = os_bucket_owner_zone
        if os_remote_policy is not None:
            self.os_remote_policy = os_remote_policy
        if os_remote_policy_uuid is not None:
            self.os_remote_policy_uuid = os_remote_policy_uuid
        if os_replication_path_num is not None:
            self.os_replication_path_num = os_replication_path_num
        if os_zone is not None:
            self.os_zone = os_zone
        if os_zone_uuid is not None:
            self.os_zone_uuid = os_zone_uuid
        if readonly is not None:
            self.readonly = readonly
        if replication_uuid is not None:
            self.replication_uuid = replication_uuid
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if uuid is not None:
            self.uuid = uuid
        if samples is not None:
            self.samples = samples

    @property
    def cluster(self):
        """Gets the cluster of this OSReplicationZoneRecord.  # noqa: E501


        :return: The cluster of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this OSReplicationZoneRecord.


        :param cluster: The cluster of this OSReplicationZoneRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this OSReplicationZoneRecord.  # noqa: E501


        :return: The create of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OSReplicationZoneRecord.


        :param create: The create of this OSReplicationZoneRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dirty(self):
        """Gets the dirty of this OSReplicationZoneRecord.  # noqa: E501


        :return: The dirty of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: bool
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """Sets the dirty of this OSReplicationZoneRecord.


        :param dirty: The dirty of this OSReplicationZoneRecord.  # noqa: E501
        :type: bool
        """

        self._dirty = dirty

    @property
    def os_bucket(self):
        """Gets the os_bucket of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_bucket of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: ObjectStorageBucketNestview
        """
        return self._os_bucket

    @os_bucket.setter
    def os_bucket(self, os_bucket):
        """Sets the os_bucket of this OSReplicationZoneRecord.


        :param os_bucket: The os_bucket of this OSReplicationZoneRecord.  # noqa: E501
        :type: ObjectStorageBucketNestview
        """

        self._os_bucket = os_bucket

    @property
    def os_bucket_owner_cluster(self):
        """Gets the os_bucket_owner_cluster of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_bucket_owner_cluster of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: RemoteClusterNestview
        """
        return self._os_bucket_owner_cluster

    @os_bucket_owner_cluster.setter
    def os_bucket_owner_cluster(self, os_bucket_owner_cluster):
        """Sets the os_bucket_owner_cluster of this OSReplicationZoneRecord.


        :param os_bucket_owner_cluster: The os_bucket_owner_cluster of this OSReplicationZoneRecord.  # noqa: E501
        :type: RemoteClusterNestview
        """

        self._os_bucket_owner_cluster = os_bucket_owner_cluster

    @property
    def os_bucket_owner_zone(self):
        """Gets the os_bucket_owner_zone of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_bucket_owner_zone of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: ObjectStorageZoneNestview
        """
        return self._os_bucket_owner_zone

    @os_bucket_owner_zone.setter
    def os_bucket_owner_zone(self, os_bucket_owner_zone):
        """Sets the os_bucket_owner_zone of this OSReplicationZoneRecord.


        :param os_bucket_owner_zone: The os_bucket_owner_zone of this OSReplicationZoneRecord.  # noqa: E501
        :type: ObjectStorageZoneNestview
        """

        self._os_bucket_owner_zone = os_bucket_owner_zone

    @property
    def os_remote_policy(self):
        """Gets the os_remote_policy of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_remote_policy of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: OSRemotePolicyNestview
        """
        return self._os_remote_policy

    @os_remote_policy.setter
    def os_remote_policy(self, os_remote_policy):
        """Sets the os_remote_policy of this OSReplicationZoneRecord.


        :param os_remote_policy: The os_remote_policy of this OSReplicationZoneRecord.  # noqa: E501
        :type: OSRemotePolicyNestview
        """

        self._os_remote_policy = os_remote_policy

    @property
    def os_remote_policy_uuid(self):
        """Gets the os_remote_policy_uuid of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_remote_policy_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: str
        """
        return self._os_remote_policy_uuid

    @os_remote_policy_uuid.setter
    def os_remote_policy_uuid(self, os_remote_policy_uuid):
        """Sets the os_remote_policy_uuid of this OSReplicationZoneRecord.


        :param os_remote_policy_uuid: The os_remote_policy_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :type: str
        """

        self._os_remote_policy_uuid = os_remote_policy_uuid

    @property
    def os_replication_path_num(self):
        """Gets the os_replication_path_num of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_replication_path_num of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: int
        """
        return self._os_replication_path_num

    @os_replication_path_num.setter
    def os_replication_path_num(self, os_replication_path_num):
        """Sets the os_replication_path_num of this OSReplicationZoneRecord.


        :param os_replication_path_num: The os_replication_path_num of this OSReplicationZoneRecord.  # noqa: E501
        :type: int
        """

        self._os_replication_path_num = os_replication_path_num

    @property
    def os_zone(self):
        """Gets the os_zone of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_zone of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: ObjectStorageZoneNestview
        """
        return self._os_zone

    @os_zone.setter
    def os_zone(self, os_zone):
        """Sets the os_zone of this OSReplicationZoneRecord.


        :param os_zone: The os_zone of this OSReplicationZoneRecord.  # noqa: E501
        :type: ObjectStorageZoneNestview
        """

        self._os_zone = os_zone

    @property
    def os_zone_uuid(self):
        """Gets the os_zone_uuid of this OSReplicationZoneRecord.  # noqa: E501


        :return: The os_zone_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: str
        """
        return self._os_zone_uuid

    @os_zone_uuid.setter
    def os_zone_uuid(self, os_zone_uuid):
        """Sets the os_zone_uuid of this OSReplicationZoneRecord.


        :param os_zone_uuid: The os_zone_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :type: str
        """

        self._os_zone_uuid = os_zone_uuid

    @property
    def readonly(self):
        """Gets the readonly of this OSReplicationZoneRecord.  # noqa: E501


        :return: The readonly of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this OSReplicationZoneRecord.


        :param readonly: The readonly of this OSReplicationZoneRecord.  # noqa: E501
        :type: bool
        """

        self._readonly = readonly

    @property
    def replication_uuid(self):
        """Gets the replication_uuid of this OSReplicationZoneRecord.  # noqa: E501


        :return: The replication_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: str
        """
        return self._replication_uuid

    @replication_uuid.setter
    def replication_uuid(self, replication_uuid):
        """Sets the replication_uuid of this OSReplicationZoneRecord.


        :param replication_uuid: The replication_uuid of this OSReplicationZoneRecord.  # noqa: E501
        :type: str
        """

        self._replication_uuid = replication_uuid

    @property
    def status(self):
        """Gets the status of this OSReplicationZoneRecord.  # noqa: E501


        :return: The status of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OSReplicationZoneRecord.


        :param status: The status of this OSReplicationZoneRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this OSReplicationZoneRecord.  # noqa: E501


        :return: The update of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this OSReplicationZoneRecord.


        :param update: The update of this OSReplicationZoneRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def uuid(self):
        """Gets the uuid of this OSReplicationZoneRecord.  # noqa: E501


        :return: The uuid of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this OSReplicationZoneRecord.


        :param uuid: The uuid of this OSReplicationZoneRecord.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def samples(self):
        """Gets the samples of this OSReplicationZoneRecord.  # noqa: E501


        :return: The samples of this OSReplicationZoneRecord.  # noqa: E501
        :rtype: list[OSReplicationZoneStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this OSReplicationZoneRecord.


        :param samples: The samples of this OSReplicationZoneRecord.  # noqa: E501
        :type: list[OSReplicationZoneStat]
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
        if not isinstance(other, OSReplicationZoneRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
