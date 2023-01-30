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


class DfsPathNestviewDfsPathStat(object):
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
        'access': 'datetime',
        'change': 'datetime',
        'dp_dfs_snapshot_policies': 'list[str]',
        'dp_snapshot_num': 'int',
        'files': 'int',
        'last_snapshot_time': 'datetime',
        'modify': 'datetime',
        'quota_num': 'int',
        'shared': 'bool',
        'size': 'int',
        'snapshot_num': 'int',
        'total_snapshot_num': 'int'
    }

    attribute_map = {
        'access': 'access',
        'change': 'change',
        'dp_dfs_snapshot_policies': 'dp_dfs_snapshot_policies',
        'dp_snapshot_num': 'dp_snapshot_num',
        'files': 'files',
        'last_snapshot_time': 'last_snapshot_time',
        'modify': 'modify',
        'quota_num': 'quota_num',
        'shared': 'shared',
        'size': 'size',
        'snapshot_num': 'snapshot_num',
        'total_snapshot_num': 'total_snapshot_num'
    }

    def __init__(self, access=None, change=None, dp_dfs_snapshot_policies=None, dp_snapshot_num=None, files=None, last_snapshot_time=None, modify=None, quota_num=None, shared=None, size=None, snapshot_num=None, total_snapshot_num=None):  # noqa: E501
        """DfsPathNestviewDfsPathStat - a model defined in Swagger"""  # noqa: E501

        self._access = None
        self._change = None
        self._dp_dfs_snapshot_policies = None
        self._dp_snapshot_num = None
        self._files = None
        self._last_snapshot_time = None
        self._modify = None
        self._quota_num = None
        self._shared = None
        self._size = None
        self._snapshot_num = None
        self._total_snapshot_num = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if change is not None:
            self.change = change
        if dp_dfs_snapshot_policies is not None:
            self.dp_dfs_snapshot_policies = dp_dfs_snapshot_policies
        if dp_snapshot_num is not None:
            self.dp_snapshot_num = dp_snapshot_num
        if files is not None:
            self.files = files
        if last_snapshot_time is not None:
            self.last_snapshot_time = last_snapshot_time
        if modify is not None:
            self.modify = modify
        if quota_num is not None:
            self.quota_num = quota_num
        if shared is not None:
            self.shared = shared
        if size is not None:
            self.size = size
        if snapshot_num is not None:
            self.snapshot_num = snapshot_num
        if total_snapshot_num is not None:
            self.total_snapshot_num = total_snapshot_num

    @property
    def access(self):
        """Gets the access of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The access of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: datetime
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this DfsPathNestviewDfsPathStat.


        :param access: The access of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: datetime
        """

        self._access = access

    @property
    def change(self):
        """Gets the change of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The change of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: datetime
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this DfsPathNestviewDfsPathStat.


        :param change: The change of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: datetime
        """

        self._change = change

    @property
    def dp_dfs_snapshot_policies(self):
        """Gets the dp_dfs_snapshot_policies of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The dp_dfs_snapshot_policies of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: list[str]
        """
        return self._dp_dfs_snapshot_policies

    @dp_dfs_snapshot_policies.setter
    def dp_dfs_snapshot_policies(self, dp_dfs_snapshot_policies):
        """Sets the dp_dfs_snapshot_policies of this DfsPathNestviewDfsPathStat.


        :param dp_dfs_snapshot_policies: The dp_dfs_snapshot_policies of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: list[str]
        """

        self._dp_dfs_snapshot_policies = dp_dfs_snapshot_policies

    @property
    def dp_snapshot_num(self):
        """Gets the dp_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The dp_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._dp_snapshot_num

    @dp_snapshot_num.setter
    def dp_snapshot_num(self, dp_snapshot_num):
        """Sets the dp_snapshot_num of this DfsPathNestviewDfsPathStat.


        :param dp_snapshot_num: The dp_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._dp_snapshot_num = dp_snapshot_num

    @property
    def files(self):
        """Gets the files of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The files of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this DfsPathNestviewDfsPathStat.


        :param files: The files of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._files = files

    @property
    def last_snapshot_time(self):
        """Gets the last_snapshot_time of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The last_snapshot_time of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: datetime
        """
        return self._last_snapshot_time

    @last_snapshot_time.setter
    def last_snapshot_time(self, last_snapshot_time):
        """Sets the last_snapshot_time of this DfsPathNestviewDfsPathStat.


        :param last_snapshot_time: The last_snapshot_time of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: datetime
        """

        self._last_snapshot_time = last_snapshot_time

    @property
    def modify(self):
        """Gets the modify of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The modify of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: datetime
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        """Sets the modify of this DfsPathNestviewDfsPathStat.


        :param modify: The modify of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: datetime
        """

        self._modify = modify

    @property
    def quota_num(self):
        """Gets the quota_num of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The quota_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._quota_num

    @quota_num.setter
    def quota_num(self, quota_num):
        """Sets the quota_num of this DfsPathNestviewDfsPathStat.


        :param quota_num: The quota_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._quota_num = quota_num

    @property
    def shared(self):
        """Gets the shared of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The shared of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this DfsPathNestviewDfsPathStat.


        :param shared: The shared of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def size(self):
        """Gets the size of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The size of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DfsPathNestviewDfsPathStat.


        :param size: The size of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def snapshot_num(self):
        """Gets the snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_num

    @snapshot_num.setter
    def snapshot_num(self, snapshot_num):
        """Sets the snapshot_num of this DfsPathNestviewDfsPathStat.


        :param snapshot_num: The snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._snapshot_num = snapshot_num

    @property
    def total_snapshot_num(self):
        """Gets the total_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501


        :return: The total_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :rtype: int
        """
        return self._total_snapshot_num

    @total_snapshot_num.setter
    def total_snapshot_num(self, total_snapshot_num):
        """Sets the total_snapshot_num of this DfsPathNestviewDfsPathStat.


        :param total_snapshot_num: The total_snapshot_num of this DfsPathNestviewDfsPathStat.  # noqa: E501
        :type: int
        """

        self._total_snapshot_num = total_snapshot_num

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
        if not isinstance(other, DfsPathNestviewDfsPathStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other