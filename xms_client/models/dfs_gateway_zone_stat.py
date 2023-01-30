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


class DfsGatewayZoneStat(object):
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
        'create': 'datetime',
        'read_bandwidth_kbyte': 'float',
        'read_iops': 'float',
        'read_latency_us': 'float',
        'write_bandwidth_kbyte': 'float',
        'write_iops': 'float',
        'write_latency_us': 'float'
    }

    attribute_map = {
        'create': 'create',
        'read_bandwidth_kbyte': 'read_bandwidth_kbyte',
        'read_iops': 'read_iops',
        'read_latency_us': 'read_latency_us',
        'write_bandwidth_kbyte': 'write_bandwidth_kbyte',
        'write_iops': 'write_iops',
        'write_latency_us': 'write_latency_us'
    }

    def __init__(self, create=None, read_bandwidth_kbyte=None, read_iops=None, read_latency_us=None, write_bandwidth_kbyte=None, write_iops=None, write_latency_us=None):  # noqa: E501
        """DfsGatewayZoneStat - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._read_bandwidth_kbyte = None
        self._read_iops = None
        self._read_latency_us = None
        self._write_bandwidth_kbyte = None
        self._write_iops = None
        self._write_latency_us = None
        self.discriminator = None

        if create is not None:
            self.create = create
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
    def create(self):
        """Gets the create of this DfsGatewayZoneStat.  # noqa: E501


        :return: The create of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsGatewayZoneStat.


        :param create: The create of this DfsGatewayZoneStat.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def read_bandwidth_kbyte(self):
        """Gets the read_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501


        :return: The read_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth_kbyte

    @read_bandwidth_kbyte.setter
    def read_bandwidth_kbyte(self, read_bandwidth_kbyte):
        """Sets the read_bandwidth_kbyte of this DfsGatewayZoneStat.


        :param read_bandwidth_kbyte: The read_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501
        :type: float
        """

        self._read_bandwidth_kbyte = read_bandwidth_kbyte

    @property
    def read_iops(self):
        """Gets the read_iops of this DfsGatewayZoneStat.  # noqa: E501


        :return: The read_iops of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this DfsGatewayZoneStat.


        :param read_iops: The read_iops of this DfsGatewayZoneStat.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def read_latency_us(self):
        """Gets the read_latency_us of this DfsGatewayZoneStat.  # noqa: E501


        :return: The read_latency_us of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._read_latency_us

    @read_latency_us.setter
    def read_latency_us(self, read_latency_us):
        """Sets the read_latency_us of this DfsGatewayZoneStat.


        :param read_latency_us: The read_latency_us of this DfsGatewayZoneStat.  # noqa: E501
        :type: float
        """

        self._read_latency_us = read_latency_us

    @property
    def write_bandwidth_kbyte(self):
        """Gets the write_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501


        :return: The write_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth_kbyte

    @write_bandwidth_kbyte.setter
    def write_bandwidth_kbyte(self, write_bandwidth_kbyte):
        """Sets the write_bandwidth_kbyte of this DfsGatewayZoneStat.


        :param write_bandwidth_kbyte: The write_bandwidth_kbyte of this DfsGatewayZoneStat.  # noqa: E501
        :type: float
        """

        self._write_bandwidth_kbyte = write_bandwidth_kbyte

    @property
    def write_iops(self):
        """Gets the write_iops of this DfsGatewayZoneStat.  # noqa: E501


        :return: The write_iops of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this DfsGatewayZoneStat.


        :param write_iops: The write_iops of this DfsGatewayZoneStat.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def write_latency_us(self):
        """Gets the write_latency_us of this DfsGatewayZoneStat.  # noqa: E501


        :return: The write_latency_us of this DfsGatewayZoneStat.  # noqa: E501
        :rtype: float
        """
        return self._write_latency_us

    @write_latency_us.setter
    def write_latency_us(self, write_latency_us):
        """Sets the write_latency_us of this DfsGatewayZoneStat.


        :param write_latency_us: The write_latency_us of this DfsGatewayZoneStat.  # noqa: E501
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
        if not isinstance(other, DfsGatewayZoneStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
