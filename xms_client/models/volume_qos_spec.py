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


class VolumeQosSpec(object):
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
        'burst_total_bw': 'int',
        'burst_total_iops': 'int',
        'max_total_bw': 'int',
        'max_total_iops': 'int'
    }

    attribute_map = {
        'burst_total_bw': 'burst_total_bw',
        'burst_total_iops': 'burst_total_iops',
        'max_total_bw': 'max_total_bw',
        'max_total_iops': 'max_total_iops'
    }

    def __init__(self, burst_total_bw=None, burst_total_iops=None, max_total_bw=None, max_total_iops=None):  # noqa: E501
        """VolumeQosSpec - a model defined in Swagger"""  # noqa: E501

        self._burst_total_bw = None
        self._burst_total_iops = None
        self._max_total_bw = None
        self._max_total_iops = None
        self.discriminator = None

        if burst_total_bw is not None:
            self.burst_total_bw = burst_total_bw
        if burst_total_iops is not None:
            self.burst_total_iops = burst_total_iops
        if max_total_bw is not None:
            self.max_total_bw = max_total_bw
        if max_total_iops is not None:
            self.max_total_iops = max_total_iops

    @property
    def burst_total_bw(self):
        """Gets the burst_total_bw of this VolumeQosSpec.  # noqa: E501


        :return: The burst_total_bw of this VolumeQosSpec.  # noqa: E501
        :rtype: int
        """
        return self._burst_total_bw

    @burst_total_bw.setter
    def burst_total_bw(self, burst_total_bw):
        """Sets the burst_total_bw of this VolumeQosSpec.


        :param burst_total_bw: The burst_total_bw of this VolumeQosSpec.  # noqa: E501
        :type: int
        """

        self._burst_total_bw = burst_total_bw

    @property
    def burst_total_iops(self):
        """Gets the burst_total_iops of this VolumeQosSpec.  # noqa: E501


        :return: The burst_total_iops of this VolumeQosSpec.  # noqa: E501
        :rtype: int
        """
        return self._burst_total_iops

    @burst_total_iops.setter
    def burst_total_iops(self, burst_total_iops):
        """Sets the burst_total_iops of this VolumeQosSpec.


        :param burst_total_iops: The burst_total_iops of this VolumeQosSpec.  # noqa: E501
        :type: int
        """

        self._burst_total_iops = burst_total_iops

    @property
    def max_total_bw(self):
        """Gets the max_total_bw of this VolumeQosSpec.  # noqa: E501


        :return: The max_total_bw of this VolumeQosSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_total_bw

    @max_total_bw.setter
    def max_total_bw(self, max_total_bw):
        """Sets the max_total_bw of this VolumeQosSpec.


        :param max_total_bw: The max_total_bw of this VolumeQosSpec.  # noqa: E501
        :type: int
        """

        self._max_total_bw = max_total_bw

    @property
    def max_total_iops(self):
        """Gets the max_total_iops of this VolumeQosSpec.  # noqa: E501


        :return: The max_total_iops of this VolumeQosSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_total_iops

    @max_total_iops.setter
    def max_total_iops(self, max_total_iops):
        """Sets the max_total_iops of this VolumeQosSpec.


        :param max_total_iops: The max_total_iops of this VolumeQosSpec.  # noqa: E501
        :type: int
        """

        self._max_total_iops = max_total_iops

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
        if not isinstance(other, VolumeQosSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
