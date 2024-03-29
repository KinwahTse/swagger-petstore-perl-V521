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


class OSSearchGatewayStat(object):
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
        'mem_usage_percent': 'float',
        'read_bandwidth_kbyte': 'float',
        'read_iops': 'float',
        'read_latency_us': 'float',
        'write_bandwidth_kbyte': 'float',
        'write_iops': 'float',
        'write_latency_us': 'float'
    }

    attribute_map = {
        'cpu_util': 'cpu_util',
        'create': 'create',
        'mem_usage_percent': 'mem_usage_percent',
        'read_bandwidth_kbyte': 'read_bandwidth_kbyte',
        'read_iops': 'read_iops',
        'read_latency_us': 'read_latency_us',
        'write_bandwidth_kbyte': 'write_bandwidth_kbyte',
        'write_iops': 'write_iops',
        'write_latency_us': 'write_latency_us'
    }

    def __init__(self, cpu_util=None, create=None, mem_usage_percent=None, read_bandwidth_kbyte=None, read_iops=None, read_latency_us=None, write_bandwidth_kbyte=None, write_iops=None, write_latency_us=None):  # noqa: E501
        """OSSearchGatewayStat - a model defined in Swagger"""  # noqa: E501

        self._cpu_util = None
        self._create = None
        self._mem_usage_percent = None
        self._read_bandwidth_kbyte = None
        self._read_iops = None
        self._read_latency_us = None
        self._write_bandwidth_kbyte = None
        self._write_iops = None
        self._write_latency_us = None
        self.discriminator = None

        if cpu_util is not None:
            self.cpu_util = cpu_util
        if create is not None:
            self.create = create
        if mem_usage_percent is not None:
            self.mem_usage_percent = mem_usage_percent
        if read_bandwidth_kbyte is not None:
            self.read_bandwidth_kbyte = read_bandwidth_kbyte
        if read_iops is not None:
            self.read_iops = read_iops
        if read_latency_us is not None:
            self.read_latency_us = read_latency_us
        if write_bandwidth_kbyte is not None:
            self.write_bandwidth_kbyte = write_bandwidth_kbyte
        if write_iops is not None:
            self.write_iops = write_iops
        if write_latency_us is not None:
            self.write_latency_us = write_latency_us

    @property
    def cpu_util(self):
        """Gets the cpu_util of this OSSearchGatewayStat.  # noqa: E501


        :return: The cpu_util of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._cpu_util

    @cpu_util.setter
    def cpu_util(self, cpu_util):
        """Sets the cpu_util of this OSSearchGatewayStat.


        :param cpu_util: The cpu_util of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._cpu_util = cpu_util

    @property
    def create(self):
        """Gets the create of this OSSearchGatewayStat.  # noqa: E501


        :return: The create of this OSSearchGatewayStat.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OSSearchGatewayStat.


        :param create: The create of this OSSearchGatewayStat.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def mem_usage_percent(self):
        """Gets the mem_usage_percent of this OSSearchGatewayStat.  # noqa: E501


        :return: The mem_usage_percent of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._mem_usage_percent

    @mem_usage_percent.setter
    def mem_usage_percent(self, mem_usage_percent):
        """Sets the mem_usage_percent of this OSSearchGatewayStat.


        :param mem_usage_percent: The mem_usage_percent of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._mem_usage_percent = mem_usage_percent

    @property
    def read_bandwidth_kbyte(self):
        """Gets the read_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501


        :return: The read_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth_kbyte

    @read_bandwidth_kbyte.setter
    def read_bandwidth_kbyte(self, read_bandwidth_kbyte):
        """Sets the read_bandwidth_kbyte of this OSSearchGatewayStat.


        :param read_bandwidth_kbyte: The read_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._read_bandwidth_kbyte = read_bandwidth_kbyte

    @property
    def read_iops(self):
        """Gets the read_iops of this OSSearchGatewayStat.  # noqa: E501


        :return: The read_iops of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this OSSearchGatewayStat.


        :param read_iops: The read_iops of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def read_latency_us(self):
        """Gets the read_latency_us of this OSSearchGatewayStat.  # noqa: E501


        :return: The read_latency_us of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._read_latency_us

    @read_latency_us.setter
    def read_latency_us(self, read_latency_us):
        """Sets the read_latency_us of this OSSearchGatewayStat.


        :param read_latency_us: The read_latency_us of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._read_latency_us = read_latency_us

    @property
    def write_bandwidth_kbyte(self):
        """Gets the write_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501


        :return: The write_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth_kbyte

    @write_bandwidth_kbyte.setter
    def write_bandwidth_kbyte(self, write_bandwidth_kbyte):
        """Sets the write_bandwidth_kbyte of this OSSearchGatewayStat.


        :param write_bandwidth_kbyte: The write_bandwidth_kbyte of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._write_bandwidth_kbyte = write_bandwidth_kbyte

    @property
    def write_iops(self):
        """Gets the write_iops of this OSSearchGatewayStat.  # noqa: E501


        :return: The write_iops of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this OSSearchGatewayStat.


        :param write_iops: The write_iops of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def write_latency_us(self):
        """Gets the write_latency_us of this OSSearchGatewayStat.  # noqa: E501


        :return: The write_latency_us of this OSSearchGatewayStat.  # noqa: E501
        :rtype: float
        """
        return self._write_latency_us

    @write_latency_us.setter
    def write_latency_us(self, write_latency_us):
        """Sets the write_latency_us of this OSSearchGatewayStat.


        :param write_latency_us: The write_latency_us of this OSSearchGatewayStat.  # noqa: E501
        :type: float
        """

        self._write_latency_us = write_latency_us

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
        if not isinstance(other, OSSearchGatewayStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
