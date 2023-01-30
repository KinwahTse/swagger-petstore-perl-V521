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


class PartitionsCreateReqPartitions(object):
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
        'metadata_partition_num': 'int',
        'num': 'int',
        'omap_byte': 'int',
        'total_cache_bytes': 'int',
        'total_metadata_bytes': 'int'
    }

    attribute_map = {
        'metadata_partition_num': 'metadata_partition_num',
        'num': 'num',
        'omap_byte': 'omap_byte',
        'total_cache_bytes': 'total_cache_bytes',
        'total_metadata_bytes': 'total_metadata_bytes'
    }

    def __init__(self, metadata_partition_num=None, num=None, omap_byte=None, total_cache_bytes=None, total_metadata_bytes=None):  # noqa: E501
        """PartitionsCreateReqPartitions - a model defined in Swagger"""  # noqa: E501

        self._metadata_partition_num = None
        self._num = None
        self._omap_byte = None
        self._total_cache_bytes = None
        self._total_metadata_bytes = None
        self.discriminator = None

        if metadata_partition_num is not None:
            self.metadata_partition_num = metadata_partition_num
        if num is not None:
            self.num = num
        if omap_byte is not None:
            self.omap_byte = omap_byte
        if total_cache_bytes is not None:
            self.total_cache_bytes = total_cache_bytes
        if total_metadata_bytes is not None:
            self.total_metadata_bytes = total_metadata_bytes

    @property
    def metadata_partition_num(self):
        """Gets the metadata_partition_num of this PartitionsCreateReqPartitions.  # noqa: E501


        :return: The metadata_partition_num of this PartitionsCreateReqPartitions.  # noqa: E501
        :rtype: int
        """
        return self._metadata_partition_num

    @metadata_partition_num.setter
    def metadata_partition_num(self, metadata_partition_num):
        """Sets the metadata_partition_num of this PartitionsCreateReqPartitions.


        :param metadata_partition_num: The metadata_partition_num of this PartitionsCreateReqPartitions.  # noqa: E501
        :type: int
        """

        self._metadata_partition_num = metadata_partition_num

    @property
    def num(self):
        """Gets the num of this PartitionsCreateReqPartitions.  # noqa: E501


        :return: The num of this PartitionsCreateReqPartitions.  # noqa: E501
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this PartitionsCreateReqPartitions.


        :param num: The num of this PartitionsCreateReqPartitions.  # noqa: E501
        :type: int
        """

        self._num = num

    @property
    def omap_byte(self):
        """Gets the omap_byte of this PartitionsCreateReqPartitions.  # noqa: E501


        :return: The omap_byte of this PartitionsCreateReqPartitions.  # noqa: E501
        :rtype: int
        """
        return self._omap_byte

    @omap_byte.setter
    def omap_byte(self, omap_byte):
        """Sets the omap_byte of this PartitionsCreateReqPartitions.


        :param omap_byte: The omap_byte of this PartitionsCreateReqPartitions.  # noqa: E501
        :type: int
        """

        self._omap_byte = omap_byte

    @property
    def total_cache_bytes(self):
        """Gets the total_cache_bytes of this PartitionsCreateReqPartitions.  # noqa: E501


        :return: The total_cache_bytes of this PartitionsCreateReqPartitions.  # noqa: E501
        :rtype: int
        """
        return self._total_cache_bytes

    @total_cache_bytes.setter
    def total_cache_bytes(self, total_cache_bytes):
        """Sets the total_cache_bytes of this PartitionsCreateReqPartitions.


        :param total_cache_bytes: The total_cache_bytes of this PartitionsCreateReqPartitions.  # noqa: E501
        :type: int
        """

        self._total_cache_bytes = total_cache_bytes

    @property
    def total_metadata_bytes(self):
        """Gets the total_metadata_bytes of this PartitionsCreateReqPartitions.  # noqa: E501


        :return: The total_metadata_bytes of this PartitionsCreateReqPartitions.  # noqa: E501
        :rtype: int
        """
        return self._total_metadata_bytes

    @total_metadata_bytes.setter
    def total_metadata_bytes(self, total_metadata_bytes):
        """Sets the total_metadata_bytes of this PartitionsCreateReqPartitions.


        :param total_metadata_bytes: The total_metadata_bytes of this PartitionsCreateReqPartitions.  # noqa: E501
        :type: int
        """

        self._total_metadata_bytes = total_metadata_bytes

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
        if not isinstance(other, PartitionsCreateReqPartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
