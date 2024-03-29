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


class ObjectStorageGatewayStat(object):
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
        'cpu_util': 'float',
        'create': 'datetime',
        'down_bandwidth_kbyte': 'float',
        'down_ops': 'float',
        'mem_usage_percent': 'float',
        'merge_speed': 'int',
        'requests': 'int',
        'sync_down_bandwidth_kbyte': 'float',
        'sync_down_ops': 'float',
        'up_bandwidth_kbyte': 'float',
        'up_ops': 'float'
    }

    attribute_map = {
        'cpu_util': 'cpu_util',
        'create': 'create',
        'down_bandwidth_kbyte': 'down_bandwidth_kbyte',
        'down_ops': 'down_ops',
        'mem_usage_percent': 'mem_usage_percent',
        'merge_speed': 'merge_speed',
        'requests': 'requests',
        'sync_down_bandwidth_kbyte': 'sync_down_bandwidth_kbyte',
        'sync_down_ops': 'sync_down_ops',
        'up_bandwidth_kbyte': 'up_bandwidth_kbyte',
        'up_ops': 'up_ops'
    }

    def __init__(self, cpu_util=None, create=None, down_bandwidth_kbyte=None, down_ops=None, mem_usage_percent=None, merge_speed=None, requests=None, sync_down_bandwidth_kbyte=None, sync_down_ops=None, up_bandwidth_kbyte=None, up_ops=None):  # noqa: E501
        """ObjectStorageGatewayStat - a model defined in Swagger"""  # noqa: E501

        self._cpu_util = None
        self._create = None
        self._down_bandwidth_kbyte = None
        self._down_ops = None
        self._mem_usage_percent = None
        self._merge_speed = None
        self._requests = None
        self._sync_down_bandwidth_kbyte = None
        self._sync_down_ops = None
        self._up_bandwidth_kbyte = None
        self._up_ops = None
        self.discriminator = None

        if cpu_util is not None:
            self.cpu_util = cpu_util
        if create is not None:
            self.create = create
        if down_bandwidth_kbyte is not None:
            self.down_bandwidth_kbyte = down_bandwidth_kbyte
        if down_ops is not None:
            self.down_ops = down_ops
        if mem_usage_percent is not None:
            self.mem_usage_percent = mem_usage_percent
        if merge_speed is not None:
            self.merge_speed = merge_speed
        if requests is not None:
            self.requests = requests
        if sync_down_bandwidth_kbyte is not None:
            self.sync_down_bandwidth_kbyte = sync_down_bandwidth_kbyte
        if sync_down_ops is not None:
            self.sync_down_ops = sync_down_ops
        if up_bandwidth_kbyte is not None:
            self.up_bandwidth_kbyte = up_bandwidth_kbyte
        if up_ops is not None:
            self.up_ops = up_ops

    @property
    def cpu_util(self):
        """Gets the cpu_util of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The cpu_util of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._cpu_util

    @cpu_util.setter
    def cpu_util(self, cpu_util):
        """Sets the cpu_util of this ObjectStorageGatewayStat.


        :param cpu_util: The cpu_util of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._cpu_util = cpu_util

    @property
    def create(self):
        """Gets the create of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The create of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ObjectStorageGatewayStat.


        :param create: The create of this ObjectStorageGatewayStat.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def down_bandwidth_kbyte(self):
        """Gets the down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._down_bandwidth_kbyte

    @down_bandwidth_kbyte.setter
    def down_bandwidth_kbyte(self, down_bandwidth_kbyte):
        """Sets the down_bandwidth_kbyte of this ObjectStorageGatewayStat.


        :param down_bandwidth_kbyte: The down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._down_bandwidth_kbyte = down_bandwidth_kbyte

    @property
    def down_ops(self):
        """Gets the down_ops of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The down_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._down_ops

    @down_ops.setter
    def down_ops(self, down_ops):
        """Sets the down_ops of this ObjectStorageGatewayStat.


        :param down_ops: The down_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._down_ops = down_ops

    @property
    def mem_usage_percent(self):
        """Gets the mem_usage_percent of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The mem_usage_percent of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._mem_usage_percent

    @mem_usage_percent.setter
    def mem_usage_percent(self, mem_usage_percent):
        """Sets the mem_usage_percent of this ObjectStorageGatewayStat.


        :param mem_usage_percent: The mem_usage_percent of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._mem_usage_percent = mem_usage_percent

    @property
    def merge_speed(self):
        """Gets the merge_speed of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The merge_speed of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: int
        """
        return self._merge_speed

    @merge_speed.setter
    def merge_speed(self, merge_speed):
        """Sets the merge_speed of this ObjectStorageGatewayStat.


        :param merge_speed: The merge_speed of this ObjectStorageGatewayStat.  # noqa: E501
        :type: int
        """

        self._merge_speed = merge_speed

    @property
    def requests(self):
        """Gets the requests of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The requests of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this ObjectStorageGatewayStat.


        :param requests: The requests of this ObjectStorageGatewayStat.  # noqa: E501
        :type: int
        """

        self._requests = requests

    @property
    def sync_down_bandwidth_kbyte(self):
        """Gets the sync_down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The sync_down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._sync_down_bandwidth_kbyte

    @sync_down_bandwidth_kbyte.setter
    def sync_down_bandwidth_kbyte(self, sync_down_bandwidth_kbyte):
        """Sets the sync_down_bandwidth_kbyte of this ObjectStorageGatewayStat.


        :param sync_down_bandwidth_kbyte: The sync_down_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._sync_down_bandwidth_kbyte = sync_down_bandwidth_kbyte

    @property
    def sync_down_ops(self):
        """Gets the sync_down_ops of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The sync_down_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._sync_down_ops

    @sync_down_ops.setter
    def sync_down_ops(self, sync_down_ops):
        """Sets the sync_down_ops of this ObjectStorageGatewayStat.


        :param sync_down_ops: The sync_down_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._sync_down_ops = sync_down_ops

    @property
    def up_bandwidth_kbyte(self):
        """Gets the up_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The up_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._up_bandwidth_kbyte

    @up_bandwidth_kbyte.setter
    def up_bandwidth_kbyte(self, up_bandwidth_kbyte):
        """Sets the up_bandwidth_kbyte of this ObjectStorageGatewayStat.


        :param up_bandwidth_kbyte: The up_bandwidth_kbyte of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._up_bandwidth_kbyte = up_bandwidth_kbyte

    @property
    def up_ops(self):
        """Gets the up_ops of this ObjectStorageGatewayStat.  # noqa: E501


        :return: The up_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._up_ops

    @up_ops.setter
    def up_ops(self, up_ops):
        """Sets the up_ops of this ObjectStorageGatewayStat.


        :param up_ops: The up_ops of this ObjectStorageGatewayStat.  # noqa: E501
        :type: float
        """

        self._up_ops = up_ops

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
        if not isinstance(other, ObjectStorageGatewayStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
