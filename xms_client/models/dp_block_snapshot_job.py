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

# from xms_client.models.dp_block_snapshot_policy_nestview import DpBlockSnapshotPolicyNestview  # noqa: F401,E501
# from xms_client.models.snapshot_nestview import SnapshotNestview  # noqa: F401,E501
# from xms_client.models.volume_nestview import VolumeNestview  # noqa: F401,E501


class DpBlockSnapshotJob(object):
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
        'block_snapshot': 'SnapshotNestview',
        'block_volume': 'VolumeNestview',
        'block_volume_size': 'int',
        'diff_type': 'str',
        'dp_block_snapshot_policy': 'DpBlockSnapshotPolicyNestview',
        'finished_at': 'datetime',
        'id': 'int',
        'progress': 'float',
        'size': 'int',
        'started_at': 'datetime',
        'status': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'block_snapshot': 'block_snapshot',
        'block_volume': 'block_volume',
        'block_volume_size': 'block_volume_size',
        'diff_type': 'diff_type',
        'dp_block_snapshot_policy': 'dp_block_snapshot_policy',
        'finished_at': 'finished_at',
        'id': 'id',
        'progress': 'progress',
        'size': 'size',
        'started_at': 'started_at',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, block_snapshot=None, block_volume=None, block_volume_size=None, diff_type=None, dp_block_snapshot_policy=None, finished_at=None, id=None, progress=None, size=None, started_at=None, status=None, updated_at=None):  # noqa: E501
        """DpBlockSnapshotJob - a model defined in Swagger"""  # noqa: E501

        self._block_snapshot = None
        self._block_volume = None
        self._block_volume_size = None
        self._diff_type = None
        self._dp_block_snapshot_policy = None
        self._finished_at = None
        self._id = None
        self._progress = None
        self._size = None
        self._started_at = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if block_snapshot is not None:
            self.block_snapshot = block_snapshot
        if block_volume is not None:
            self.block_volume = block_volume
        if block_volume_size is not None:
            self.block_volume_size = block_volume_size
        if diff_type is not None:
            self.diff_type = diff_type
        if dp_block_snapshot_policy is not None:
            self.dp_block_snapshot_policy = dp_block_snapshot_policy
        if finished_at is not None:
            self.finished_at = finished_at
        if id is not None:
            self.id = id
        if progress is not None:
            self.progress = progress
        if size is not None:
            self.size = size
        if started_at is not None:
            self.started_at = started_at
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def block_snapshot(self):
        """Gets the block_snapshot of this DpBlockSnapshotJob.  # noqa: E501


        :return: The block_snapshot of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: SnapshotNestview
        """
        return self._block_snapshot

    @block_snapshot.setter
    def block_snapshot(self, block_snapshot):
        """Sets the block_snapshot of this DpBlockSnapshotJob.


        :param block_snapshot: The block_snapshot of this DpBlockSnapshotJob.  # noqa: E501
        :type: SnapshotNestview
        """

        self._block_snapshot = block_snapshot

    @property
    def block_volume(self):
        """Gets the block_volume of this DpBlockSnapshotJob.  # noqa: E501


        :return: The block_volume of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: VolumeNestview
        """
        return self._block_volume

    @block_volume.setter
    def block_volume(self, block_volume):
        """Sets the block_volume of this DpBlockSnapshotJob.


        :param block_volume: The block_volume of this DpBlockSnapshotJob.  # noqa: E501
        :type: VolumeNestview
        """

        self._block_volume = block_volume

    @property
    def block_volume_size(self):
        """Gets the block_volume_size of this DpBlockSnapshotJob.  # noqa: E501


        :return: The block_volume_size of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: int
        """
        return self._block_volume_size

    @block_volume_size.setter
    def block_volume_size(self, block_volume_size):
        """Sets the block_volume_size of this DpBlockSnapshotJob.


        :param block_volume_size: The block_volume_size of this DpBlockSnapshotJob.  # noqa: E501
        :type: int
        """

        self._block_volume_size = block_volume_size

    @property
    def diff_type(self):
        """Gets the diff_type of this DpBlockSnapshotJob.  # noqa: E501


        :return: The diff_type of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: str
        """
        return self._diff_type

    @diff_type.setter
    def diff_type(self, diff_type):
        """Sets the diff_type of this DpBlockSnapshotJob.


        :param diff_type: The diff_type of this DpBlockSnapshotJob.  # noqa: E501
        :type: str
        """

        self._diff_type = diff_type

    @property
    def dp_block_snapshot_policy(self):
        """Gets the dp_block_snapshot_policy of this DpBlockSnapshotJob.  # noqa: E501


        :return: The dp_block_snapshot_policy of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: DpBlockSnapshotPolicyNestview
        """
        return self._dp_block_snapshot_policy

    @dp_block_snapshot_policy.setter
    def dp_block_snapshot_policy(self, dp_block_snapshot_policy):
        """Sets the dp_block_snapshot_policy of this DpBlockSnapshotJob.


        :param dp_block_snapshot_policy: The dp_block_snapshot_policy of this DpBlockSnapshotJob.  # noqa: E501
        :type: DpBlockSnapshotPolicyNestview
        """

        self._dp_block_snapshot_policy = dp_block_snapshot_policy

    @property
    def finished_at(self):
        """Gets the finished_at of this DpBlockSnapshotJob.  # noqa: E501


        :return: The finished_at of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this DpBlockSnapshotJob.


        :param finished_at: The finished_at of this DpBlockSnapshotJob.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this DpBlockSnapshotJob.  # noqa: E501


        :return: The id of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DpBlockSnapshotJob.


        :param id: The id of this DpBlockSnapshotJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def progress(self):
        """Gets the progress of this DpBlockSnapshotJob.  # noqa: E501


        :return: The progress of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DpBlockSnapshotJob.


        :param progress: The progress of this DpBlockSnapshotJob.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def size(self):
        """Gets the size of this DpBlockSnapshotJob.  # noqa: E501


        :return: The size of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DpBlockSnapshotJob.


        :param size: The size of this DpBlockSnapshotJob.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def started_at(self):
        """Gets the started_at of this DpBlockSnapshotJob.  # noqa: E501


        :return: The started_at of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this DpBlockSnapshotJob.


        :param started_at: The started_at of this DpBlockSnapshotJob.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this DpBlockSnapshotJob.  # noqa: E501


        :return: The status of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DpBlockSnapshotJob.


        :param status: The status of this DpBlockSnapshotJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this DpBlockSnapshotJob.  # noqa: E501


        :return: The updated_at of this DpBlockSnapshotJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DpBlockSnapshotJob.


        :param updated_at: The updated_at of this DpBlockSnapshotJob.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, DpBlockSnapshotJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
