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

# from xms_client.models.dfs_path import DfsPath  # noqa: F401,E501
# from xms_client.models.dfs_snapshot_nestview import DfsSnapshotNestview  # noqa: F401,E501
# from xms_client.models.dp_dfs_snapshot_nestview import DpDfsSnapshotNestview  # noqa: F401,E501
# from xms_client.models.dp_dfs_snapshot_policy import DpDfsSnapshotPolicy  # noqa: F401,E501


class DpDfsSnapshotJob(object):
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
        'dfs_path': 'DfsPath',
        'dfs_snapshot': 'DfsSnapshotNestview',
        'dp_dfs_snapshot': 'DpDfsSnapshotNestview',
        'dp_dfs_snapshot_policy': 'DpDfsSnapshotPolicy',
        'finished_at': 'datetime',
        'id': 'int',
        'started_at': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'dfs_path': 'dfs_path',
        'dfs_snapshot': 'dfs_snapshot',
        'dp_dfs_snapshot': 'dp_dfs_snapshot',
        'dp_dfs_snapshot_policy': 'dp_dfs_snapshot_policy',
        'finished_at': 'finished_at',
        'id': 'id',
        'started_at': 'started_at',
        'status': 'status'
    }

    def __init__(self, dfs_path=None, dfs_snapshot=None, dp_dfs_snapshot=None, dp_dfs_snapshot_policy=None, finished_at=None, id=None, started_at=None, status=None):  # noqa: E501
        """DpDfsSnapshotJob - a model defined in Swagger"""  # noqa: E501

        self._dfs_path = None
        self._dfs_snapshot = None
        self._dp_dfs_snapshot = None
        self._dp_dfs_snapshot_policy = None
        self._finished_at = None
        self._id = None
        self._started_at = None
        self._status = None
        self.discriminator = None

        if dfs_path is not None:
            self.dfs_path = dfs_path
        if dfs_snapshot is not None:
            self.dfs_snapshot = dfs_snapshot
        if dp_dfs_snapshot is not None:
            self.dp_dfs_snapshot = dp_dfs_snapshot
        if dp_dfs_snapshot_policy is not None:
            self.dp_dfs_snapshot_policy = dp_dfs_snapshot_policy
        if finished_at is not None:
            self.finished_at = finished_at
        if id is not None:
            self.id = id
        if started_at is not None:
            self.started_at = started_at
        if status is not None:
            self.status = status

    @property
    def dfs_path(self):
        """Gets the dfs_path of this DpDfsSnapshotJob.  # noqa: E501


        :return: The dfs_path of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: DfsPath
        """
        return self._dfs_path

    @dfs_path.setter
    def dfs_path(self, dfs_path):
        """Sets the dfs_path of this DpDfsSnapshotJob.


        :param dfs_path: The dfs_path of this DpDfsSnapshotJob.  # noqa: E501
        :type: DfsPath
        """

        self._dfs_path = dfs_path

    @property
    def dfs_snapshot(self):
        """Gets the dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501


        :return: The dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: DfsSnapshotNestview
        """
        return self._dfs_snapshot

    @dfs_snapshot.setter
    def dfs_snapshot(self, dfs_snapshot):
        """Sets the dfs_snapshot of this DpDfsSnapshotJob.


        :param dfs_snapshot: The dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501
        :type: DfsSnapshotNestview
        """

        self._dfs_snapshot = dfs_snapshot

    @property
    def dp_dfs_snapshot(self):
        """Gets the dp_dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501


        :return: The dp_dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: DpDfsSnapshotNestview
        """
        return self._dp_dfs_snapshot

    @dp_dfs_snapshot.setter
    def dp_dfs_snapshot(self, dp_dfs_snapshot):
        """Sets the dp_dfs_snapshot of this DpDfsSnapshotJob.


        :param dp_dfs_snapshot: The dp_dfs_snapshot of this DpDfsSnapshotJob.  # noqa: E501
        :type: DpDfsSnapshotNestview
        """

        self._dp_dfs_snapshot = dp_dfs_snapshot

    @property
    def dp_dfs_snapshot_policy(self):
        """Gets the dp_dfs_snapshot_policy of this DpDfsSnapshotJob.  # noqa: E501


        :return: The dp_dfs_snapshot_policy of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: DpDfsSnapshotPolicy
        """
        return self._dp_dfs_snapshot_policy

    @dp_dfs_snapshot_policy.setter
    def dp_dfs_snapshot_policy(self, dp_dfs_snapshot_policy):
        """Sets the dp_dfs_snapshot_policy of this DpDfsSnapshotJob.


        :param dp_dfs_snapshot_policy: The dp_dfs_snapshot_policy of this DpDfsSnapshotJob.  # noqa: E501
        :type: DpDfsSnapshotPolicy
        """

        self._dp_dfs_snapshot_policy = dp_dfs_snapshot_policy

    @property
    def finished_at(self):
        """Gets the finished_at of this DpDfsSnapshotJob.  # noqa: E501


        :return: The finished_at of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this DpDfsSnapshotJob.


        :param finished_at: The finished_at of this DpDfsSnapshotJob.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this DpDfsSnapshotJob.  # noqa: E501


        :return: The id of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DpDfsSnapshotJob.


        :param id: The id of this DpDfsSnapshotJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def started_at(self):
        """Gets the started_at of this DpDfsSnapshotJob.  # noqa: E501


        :return: The started_at of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this DpDfsSnapshotJob.


        :param started_at: The started_at of this DpDfsSnapshotJob.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this DpDfsSnapshotJob.  # noqa: E501


        :return: The status of this DpDfsSnapshotJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DpDfsSnapshotJob.


        :param status: The status of this DpDfsSnapshotJob.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, DpDfsSnapshotJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
