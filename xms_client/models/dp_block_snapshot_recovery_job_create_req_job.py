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

# from xms_client.models.dp_block_snapshot_recovery_job_create_req_job_backup_cluster import DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster  # noqa: F401,E501
# from xms_client.models.dp_block_snapshot_recovery_job_create_req_job_backup_snapshot import DpBlockSnapshotRecoveryJobCreateReqJobBackupSnapshot  # noqa: F401,E501
# from xms_client.models.dp_block_snapshot_recovery_job_create_req_job_backup_volume import DpBlockSnapshotRecoveryJobCreateReqJobBackupVolume  # noqa: F401,E501
# from xms_client.models.dp_block_snapshot_recovery_job_create_req_job_volume import DpBlockSnapshotRecoveryJobCreateReqJobVolume  # noqa: F401,E501


class DpBlockSnapshotRecoveryJobCreateReqJob(object):
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
        'backup_block_snapshot': 'DpBlockSnapshotRecoveryJobCreateReqJobBackupSnapshot',
        'backup_block_volume': 'DpBlockSnapshotRecoveryJobCreateReqJobBackupVolume',
        'backup_cluster': 'DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster',
        'block_volume': 'DpBlockSnapshotRecoveryJobCreateReqJobVolume',
        'dp_gateway_id': 'int',
        'dp_site_id': 'int',
        'resource_type': 'str'
    }

    attribute_map = {
        'backup_block_snapshot': 'backup_block_snapshot',
        'backup_block_volume': 'backup_block_volume',
        'backup_cluster': 'backup_cluster',
        'block_volume': 'block_volume',
        'dp_gateway_id': 'dp_gateway_id',
        'dp_site_id': 'dp_site_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, backup_block_snapshot=None, backup_block_volume=None, backup_cluster=None, block_volume=None, dp_gateway_id=None, dp_site_id=None, resource_type=None):  # noqa: E501
        """DpBlockSnapshotRecoveryJobCreateReqJob - a model defined in Swagger"""  # noqa: E501

        self._backup_block_snapshot = None
        self._backup_block_volume = None
        self._backup_cluster = None
        self._block_volume = None
        self._dp_gateway_id = None
        self._dp_site_id = None
        self._resource_type = None
        self.discriminator = None

        self.backup_block_snapshot = backup_block_snapshot
        self.backup_block_volume = backup_block_volume
        self.backup_cluster = backup_cluster
        self.block_volume = block_volume
        self.dp_gateway_id = dp_gateway_id
        self.dp_site_id = dp_site_id
        self.resource_type = resource_type

    @property
    def backup_block_snapshot(self):
        """Gets the backup_block_snapshot of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The backup_block_snapshot of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: DpBlockSnapshotRecoveryJobCreateReqJobBackupSnapshot
        """
        return self._backup_block_snapshot

    @backup_block_snapshot.setter
    def backup_block_snapshot(self, backup_block_snapshot):
        """Sets the backup_block_snapshot of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param backup_block_snapshot: The backup_block_snapshot of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: DpBlockSnapshotRecoveryJobCreateReqJobBackupSnapshot
        """
        if backup_block_snapshot is None:
            raise ValueError("Invalid value for `backup_block_snapshot`, must not be `None`")  # noqa: E501

        self._backup_block_snapshot = backup_block_snapshot

    @property
    def backup_block_volume(self):
        """Gets the backup_block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The backup_block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: DpBlockSnapshotRecoveryJobCreateReqJobBackupVolume
        """
        return self._backup_block_volume

    @backup_block_volume.setter
    def backup_block_volume(self, backup_block_volume):
        """Sets the backup_block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param backup_block_volume: The backup_block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: DpBlockSnapshotRecoveryJobCreateReqJobBackupVolume
        """
        if backup_block_volume is None:
            raise ValueError("Invalid value for `backup_block_volume`, must not be `None`")  # noqa: E501

        self._backup_block_volume = backup_block_volume

    @property
    def backup_cluster(self):
        """Gets the backup_cluster of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The backup_cluster of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster
        """
        return self._backup_cluster

    @backup_cluster.setter
    def backup_cluster(self, backup_cluster):
        """Sets the backup_cluster of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param backup_cluster: The backup_cluster of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster
        """
        if backup_cluster is None:
            raise ValueError("Invalid value for `backup_cluster`, must not be `None`")  # noqa: E501

        self._backup_cluster = backup_cluster

    @property
    def block_volume(self):
        """Gets the block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: DpBlockSnapshotRecoveryJobCreateReqJobVolume
        """
        return self._block_volume

    @block_volume.setter
    def block_volume(self, block_volume):
        """Sets the block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param block_volume: The block_volume of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: DpBlockSnapshotRecoveryJobCreateReqJobVolume
        """
        if block_volume is None:
            raise ValueError("Invalid value for `block_volume`, must not be `None`")  # noqa: E501

        self._block_volume = block_volume

    @property
    def dp_gateway_id(self):
        """Gets the dp_gateway_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The dp_gateway_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: int
        """
        return self._dp_gateway_id

    @dp_gateway_id.setter
    def dp_gateway_id(self, dp_gateway_id):
        """Sets the dp_gateway_id of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param dp_gateway_id: The dp_gateway_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: int
        """
        if dp_gateway_id is None:
            raise ValueError("Invalid value for `dp_gateway_id`, must not be `None`")  # noqa: E501

        self._dp_gateway_id = dp_gateway_id

    @property
    def dp_site_id(self):
        """Gets the dp_site_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The dp_site_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: int
        """
        return self._dp_site_id

    @dp_site_id.setter
    def dp_site_id(self, dp_site_id):
        """Sets the dp_site_id of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param dp_site_id: The dp_site_id of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: int
        """
        if dp_site_id is None:
            raise ValueError("Invalid value for `dp_site_id`, must not be `None`")  # noqa: E501

        self._dp_site_id = dp_site_id

    @property
    def resource_type(self):
        """Gets the resource_type of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501


        :return: The resource_type of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DpBlockSnapshotRecoveryJobCreateReqJob.


        :param resource_type: The resource_type of this DpBlockSnapshotRecoveryJobCreateReqJob.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

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
        if not isinstance(other, DpBlockSnapshotRecoveryJobCreateReqJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
