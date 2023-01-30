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

# from xms_client.models.disk_stat import DiskStat  # noqa: F401,E501
# from xms_client.models.partition_stat import PartitionStat  # noqa: F401,E501


class OsdStat(object):
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
        'avg_queue_len': 'float',
        'create': 'datetime',
        'io_util': 'float',
        'kbyte_per_io': 'float',
        'read_bandwidth_kbyte': 'float',
        'read_iops': 'float',
        'read_merged_ps': 'float',
        'read_wait_us': 'float',
        'total_bandwidth_kbyte': 'float',
        'total_io_wait_us': 'float',
        'total_iops': 'float',
        'total_kbyte': 'int',
        'used_kbyte': 'int',
        'used_percent': 'float',
        'write_bandwidth_kbyte': 'float',
        'write_iops': 'float',
        'write_merged_ps': 'float',
        'write_wait_us': 'float',
        'compressed_byte': 'int',
        'compressed_origin_byte': 'int',
        'degraded_percent': 'float',
        'healthy_percent': 'float',
        'omap_total_kbyte': 'float',
        'omap_used_kbyte': 'float',
        'omap_used_percent': 'float',
        'partition': 'PartitionStat',
        'recovery_percent': 'float',
        'unavailable_percent': 'float',
        'water_level': 'float'
    }

    attribute_map = {
        'avg_queue_len': 'avg_queue_len',
        'create': 'create',
        'io_util': 'io_util',
        'kbyte_per_io': 'kbyte_per_io',
        'read_bandwidth_kbyte': 'read_bandwidth_kbyte',
        'read_iops': 'read_iops',
        'read_merged_ps': 'read_merged_ps',
        'read_wait_us': 'read_wait_us',
        'total_bandwidth_kbyte': 'total_bandwidth_kbyte',
        'total_io_wait_us': 'total_io_wait_us',
        'total_iops': 'total_iops',
        'total_kbyte': 'total_kbyte',
        'used_kbyte': 'used_kbyte',
        'used_percent': 'used_percent',
        'write_bandwidth_kbyte': 'write_bandwidth_kbyte',
        'write_iops': 'write_iops',
        'write_merged_ps': 'write_merged_ps',
        'write_wait_us': 'write_wait_us',
        'compressed_byte': 'compressed_byte',
        'compressed_origin_byte': 'compressed_origin_byte',
        'degraded_percent': 'degraded_percent',
        'healthy_percent': 'healthy_percent',
        'omap_total_kbyte': 'omap_total_kbyte',
        'omap_used_kbyte': 'omap_used_kbyte',
        'omap_used_percent': 'omap_used_percent',
        'partition': 'partition',
        'recovery_percent': 'recovery_percent',
        'unavailable_percent': 'unavailable_percent',
        'water_level': 'water_level'
    }

    def __init__(self, avg_queue_len=None, create=None, io_util=None, kbyte_per_io=None, read_bandwidth_kbyte=None, read_iops=None, read_merged_ps=None, read_wait_us=None, total_bandwidth_kbyte=None, total_io_wait_us=None, total_iops=None, total_kbyte=None, used_kbyte=None, used_percent=None, write_bandwidth_kbyte=None, write_iops=None, write_merged_ps=None, write_wait_us=None, compressed_byte=None, compressed_origin_byte=None, degraded_percent=None, healthy_percent=None, omap_total_kbyte=None, omap_used_kbyte=None, omap_used_percent=None, partition=None, recovery_percent=None, unavailable_percent=None, water_level=None):  # noqa: E501
        """OsdStat - a model defined in Swagger"""  # noqa: E501

        self._avg_queue_len = None
        self._create = None
        self._io_util = None
        self._kbyte_per_io = None
        self._read_bandwidth_kbyte = None
        self._read_iops = None
        self._read_merged_ps = None
        self._read_wait_us = None
        self._total_bandwidth_kbyte = None
        self._total_io_wait_us = None
        self._total_iops = None
        self._total_kbyte = None
        self._used_kbyte = None
        self._used_percent = None
        self._write_bandwidth_kbyte = None
        self._write_iops = None
        self._write_merged_ps = None
        self._write_wait_us = None
        self._compressed_byte = None
        self._compressed_origin_byte = None
        self._degraded_percent = None
        self._healthy_percent = None
        self._omap_total_kbyte = None
        self._omap_used_kbyte = None
        self._omap_used_percent = None
        self._partition = None
        self._recovery_percent = None
        self._unavailable_percent = None
        self._water_level = None
        self.discriminator = None

        if avg_queue_len is not None:
            self.avg_queue_len = avg_queue_len
        if create is not None:
            self.create = create
        if io_util is not None:
            self.io_util = io_util
        if kbyte_per_io is not None:
            self.kbyte_per_io = kbyte_per_io
        if read_bandwidth_kbyte is not None:
            self.read_bandwidth_kbyte = read_bandwidth_kbyte
        if read_iops is not None:
            self.read_iops = read_iops
        if read_merged_ps is not None:
            self.read_merged_ps = read_merged_ps
        if read_wait_us is not None:
            self.read_wait_us = read_wait_us
        if total_bandwidth_kbyte is not None:
            self.total_bandwidth_kbyte = total_bandwidth_kbyte
        if total_io_wait_us is not None:
            self.total_io_wait_us = total_io_wait_us
        if total_iops is not None:
            self.total_iops = total_iops
        if total_kbyte is not None:
            self.total_kbyte = total_kbyte
        if used_kbyte is not None:
            self.used_kbyte = used_kbyte
        if used_percent is not None:
            self.used_percent = used_percent
        if write_bandwidth_kbyte is not None:
            self.write_bandwidth_kbyte = write_bandwidth_kbyte
        if write_iops is not None:
            self.write_iops = write_iops
        if write_merged_ps is not None:
            self.write_merged_ps = write_merged_ps
        if write_wait_us is not None:
            self.write_wait_us = write_wait_us
        if compressed_byte is not None:
            self.compressed_byte = compressed_byte
        if compressed_origin_byte is not None:
            self.compressed_origin_byte = compressed_origin_byte
        if degraded_percent is not None:
            self.degraded_percent = degraded_percent
        if healthy_percent is not None:
            self.healthy_percent = healthy_percent
        if omap_total_kbyte is not None:
            self.omap_total_kbyte = omap_total_kbyte
        if omap_used_kbyte is not None:
            self.omap_used_kbyte = omap_used_kbyte
        if omap_used_percent is not None:
            self.omap_used_percent = omap_used_percent
        if partition is not None:
            self.partition = partition
        if recovery_percent is not None:
            self.recovery_percent = recovery_percent
        if unavailable_percent is not None:
            self.unavailable_percent = unavailable_percent
        if water_level is not None:
            self.water_level = water_level

    @property
    def avg_queue_len(self):
        """Gets the avg_queue_len of this OsdStat.  # noqa: E501


        :return: The avg_queue_len of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._avg_queue_len

    @avg_queue_len.setter
    def avg_queue_len(self, avg_queue_len):
        """Sets the avg_queue_len of this OsdStat.


        :param avg_queue_len: The avg_queue_len of this OsdStat.  # noqa: E501
        :type: float
        """

        self._avg_queue_len = avg_queue_len

    @property
    def create(self):
        """Gets the create of this OsdStat.  # noqa: E501


        :return: The create of this OsdStat.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OsdStat.


        :param create: The create of this OsdStat.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def io_util(self):
        """Gets the io_util of this OsdStat.  # noqa: E501


        :return: The io_util of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._io_util

    @io_util.setter
    def io_util(self, io_util):
        """Sets the io_util of this OsdStat.


        :param io_util: The io_util of this OsdStat.  # noqa: E501
        :type: float
        """

        self._io_util = io_util

    @property
    def kbyte_per_io(self):
        """Gets the kbyte_per_io of this OsdStat.  # noqa: E501


        :return: The kbyte_per_io of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._kbyte_per_io

    @kbyte_per_io.setter
    def kbyte_per_io(self, kbyte_per_io):
        """Sets the kbyte_per_io of this OsdStat.


        :param kbyte_per_io: The kbyte_per_io of this OsdStat.  # noqa: E501
        :type: float
        """

        self._kbyte_per_io = kbyte_per_io

    @property
    def read_bandwidth_kbyte(self):
        """Gets the read_bandwidth_kbyte of this OsdStat.  # noqa: E501


        :return: The read_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth_kbyte

    @read_bandwidth_kbyte.setter
    def read_bandwidth_kbyte(self, read_bandwidth_kbyte):
        """Sets the read_bandwidth_kbyte of this OsdStat.


        :param read_bandwidth_kbyte: The read_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :type: float
        """

        self._read_bandwidth_kbyte = read_bandwidth_kbyte

    @property
    def read_iops(self):
        """Gets the read_iops of this OsdStat.  # noqa: E501


        :return: The read_iops of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this OsdStat.


        :param read_iops: The read_iops of this OsdStat.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def read_merged_ps(self):
        """Gets the read_merged_ps of this OsdStat.  # noqa: E501


        :return: The read_merged_ps of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._read_merged_ps

    @read_merged_ps.setter
    def read_merged_ps(self, read_merged_ps):
        """Sets the read_merged_ps of this OsdStat.


        :param read_merged_ps: The read_merged_ps of this OsdStat.  # noqa: E501
        :type: float
        """

        self._read_merged_ps = read_merged_ps

    @property
    def read_wait_us(self):
        """Gets the read_wait_us of this OsdStat.  # noqa: E501


        :return: The read_wait_us of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._read_wait_us

    @read_wait_us.setter
    def read_wait_us(self, read_wait_us):
        """Sets the read_wait_us of this OsdStat.


        :param read_wait_us: The read_wait_us of this OsdStat.  # noqa: E501
        :type: float
        """

        self._read_wait_us = read_wait_us

    @property
    def total_bandwidth_kbyte(self):
        """Gets the total_bandwidth_kbyte of this OsdStat.  # noqa: E501


        :return: The total_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._total_bandwidth_kbyte

    @total_bandwidth_kbyte.setter
    def total_bandwidth_kbyte(self, total_bandwidth_kbyte):
        """Sets the total_bandwidth_kbyte of this OsdStat.


        :param total_bandwidth_kbyte: The total_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :type: float
        """

        self._total_bandwidth_kbyte = total_bandwidth_kbyte

    @property
    def total_io_wait_us(self):
        """Gets the total_io_wait_us of this OsdStat.  # noqa: E501


        :return: The total_io_wait_us of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._total_io_wait_us

    @total_io_wait_us.setter
    def total_io_wait_us(self, total_io_wait_us):
        """Sets the total_io_wait_us of this OsdStat.


        :param total_io_wait_us: The total_io_wait_us of this OsdStat.  # noqa: E501
        :type: float
        """

        self._total_io_wait_us = total_io_wait_us

    @property
    def total_iops(self):
        """Gets the total_iops of this OsdStat.  # noqa: E501


        :return: The total_iops of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this OsdStat.


        :param total_iops: The total_iops of this OsdStat.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

    @property
    def total_kbyte(self):
        """Gets the total_kbyte of this OsdStat.  # noqa: E501


        :return: The total_kbyte of this OsdStat.  # noqa: E501
        :rtype: int
        """
        return self._total_kbyte

    @total_kbyte.setter
    def total_kbyte(self, total_kbyte):
        """Sets the total_kbyte of this OsdStat.


        :param total_kbyte: The total_kbyte of this OsdStat.  # noqa: E501
        :type: int
        """

        self._total_kbyte = total_kbyte

    @property
    def used_kbyte(self):
        """Gets the used_kbyte of this OsdStat.  # noqa: E501


        :return: The used_kbyte of this OsdStat.  # noqa: E501
        :rtype: int
        """
        return self._used_kbyte

    @used_kbyte.setter
    def used_kbyte(self, used_kbyte):
        """Sets the used_kbyte of this OsdStat.


        :param used_kbyte: The used_kbyte of this OsdStat.  # noqa: E501
        :type: int
        """

        self._used_kbyte = used_kbyte

    @property
    def used_percent(self):
        """Gets the used_percent of this OsdStat.  # noqa: E501


        :return: The used_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        """Sets the used_percent of this OsdStat.


        :param used_percent: The used_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._used_percent = used_percent

    @property
    def write_bandwidth_kbyte(self):
        """Gets the write_bandwidth_kbyte of this OsdStat.  # noqa: E501


        :return: The write_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth_kbyte

    @write_bandwidth_kbyte.setter
    def write_bandwidth_kbyte(self, write_bandwidth_kbyte):
        """Sets the write_bandwidth_kbyte of this OsdStat.


        :param write_bandwidth_kbyte: The write_bandwidth_kbyte of this OsdStat.  # noqa: E501
        :type: float
        """

        self._write_bandwidth_kbyte = write_bandwidth_kbyte

    @property
    def write_iops(self):
        """Gets the write_iops of this OsdStat.  # noqa: E501


        :return: The write_iops of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this OsdStat.


        :param write_iops: The write_iops of this OsdStat.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def write_merged_ps(self):
        """Gets the write_merged_ps of this OsdStat.  # noqa: E501


        :return: The write_merged_ps of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._write_merged_ps

    @write_merged_ps.setter
    def write_merged_ps(self, write_merged_ps):
        """Sets the write_merged_ps of this OsdStat.


        :param write_merged_ps: The write_merged_ps of this OsdStat.  # noqa: E501
        :type: float
        """

        self._write_merged_ps = write_merged_ps

    @property
    def write_wait_us(self):
        """Gets the write_wait_us of this OsdStat.  # noqa: E501


        :return: The write_wait_us of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._write_wait_us

    @write_wait_us.setter
    def write_wait_us(self, write_wait_us):
        """Sets the write_wait_us of this OsdStat.


        :param write_wait_us: The write_wait_us of this OsdStat.  # noqa: E501
        :type: float
        """

        self._write_wait_us = write_wait_us

    @property
    def compressed_byte(self):
        """Gets the compressed_byte of this OsdStat.  # noqa: E501


        :return: The compressed_byte of this OsdStat.  # noqa: E501
        :rtype: int
        """
        return self._compressed_byte

    @compressed_byte.setter
    def compressed_byte(self, compressed_byte):
        """Sets the compressed_byte of this OsdStat.


        :param compressed_byte: The compressed_byte of this OsdStat.  # noqa: E501
        :type: int
        """

        self._compressed_byte = compressed_byte

    @property
    def compressed_origin_byte(self):
        """Gets the compressed_origin_byte of this OsdStat.  # noqa: E501


        :return: The compressed_origin_byte of this OsdStat.  # noqa: E501
        :rtype: int
        """
        return self._compressed_origin_byte

    @compressed_origin_byte.setter
    def compressed_origin_byte(self, compressed_origin_byte):
        """Sets the compressed_origin_byte of this OsdStat.


        :param compressed_origin_byte: The compressed_origin_byte of this OsdStat.  # noqa: E501
        :type: int
        """

        self._compressed_origin_byte = compressed_origin_byte

    @property
    def degraded_percent(self):
        """Gets the degraded_percent of this OsdStat.  # noqa: E501


        :return: The degraded_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._degraded_percent

    @degraded_percent.setter
    def degraded_percent(self, degraded_percent):
        """Sets the degraded_percent of this OsdStat.


        :param degraded_percent: The degraded_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._degraded_percent = degraded_percent

    @property
    def healthy_percent(self):
        """Gets the healthy_percent of this OsdStat.  # noqa: E501


        :return: The healthy_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._healthy_percent

    @healthy_percent.setter
    def healthy_percent(self, healthy_percent):
        """Sets the healthy_percent of this OsdStat.


        :param healthy_percent: The healthy_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._healthy_percent = healthy_percent

    @property
    def omap_total_kbyte(self):
        """Gets the omap_total_kbyte of this OsdStat.  # noqa: E501


        :return: The omap_total_kbyte of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._omap_total_kbyte

    @omap_total_kbyte.setter
    def omap_total_kbyte(self, omap_total_kbyte):
        """Sets the omap_total_kbyte of this OsdStat.


        :param omap_total_kbyte: The omap_total_kbyte of this OsdStat.  # noqa: E501
        :type: float
        """

        self._omap_total_kbyte = omap_total_kbyte

    @property
    def omap_used_kbyte(self):
        """Gets the omap_used_kbyte of this OsdStat.  # noqa: E501


        :return: The omap_used_kbyte of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._omap_used_kbyte

    @omap_used_kbyte.setter
    def omap_used_kbyte(self, omap_used_kbyte):
        """Sets the omap_used_kbyte of this OsdStat.


        :param omap_used_kbyte: The omap_used_kbyte of this OsdStat.  # noqa: E501
        :type: float
        """

        self._omap_used_kbyte = omap_used_kbyte

    @property
    def omap_used_percent(self):
        """Gets the omap_used_percent of this OsdStat.  # noqa: E501


        :return: The omap_used_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._omap_used_percent

    @omap_used_percent.setter
    def omap_used_percent(self, omap_used_percent):
        """Sets the omap_used_percent of this OsdStat.


        :param omap_used_percent: The omap_used_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._omap_used_percent = omap_used_percent

    @property
    def partition(self):
        """Gets the partition of this OsdStat.  # noqa: E501


        :return: The partition of this OsdStat.  # noqa: E501
        :rtype: PartitionStat
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this OsdStat.


        :param partition: The partition of this OsdStat.  # noqa: E501
        :type: PartitionStat
        """

        self._partition = partition

    @property
    def recovery_percent(self):
        """Gets the recovery_percent of this OsdStat.  # noqa: E501


        :return: The recovery_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._recovery_percent

    @recovery_percent.setter
    def recovery_percent(self, recovery_percent):
        """Sets the recovery_percent of this OsdStat.


        :param recovery_percent: The recovery_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._recovery_percent = recovery_percent

    @property
    def unavailable_percent(self):
        """Gets the unavailable_percent of this OsdStat.  # noqa: E501


        :return: The unavailable_percent of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._unavailable_percent

    @unavailable_percent.setter
    def unavailable_percent(self, unavailable_percent):
        """Sets the unavailable_percent of this OsdStat.


        :param unavailable_percent: The unavailable_percent of this OsdStat.  # noqa: E501
        :type: float
        """

        self._unavailable_percent = unavailable_percent

    @property
    def water_level(self):
        """Gets the water_level of this OsdStat.  # noqa: E501


        :return: The water_level of this OsdStat.  # noqa: E501
        :rtype: float
        """
        return self._water_level

    @water_level.setter
    def water_level(self, water_level):
        """Sets the water_level of this OsdStat.


        :param water_level: The water_level of this OsdStat.  # noqa: E501
        :type: float
        """

        self._water_level = water_level

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
        if not isinstance(other, OsdStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
