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

# from xms_client.models.volume_update_req_volume import VolumeUpdateReqVolume  # noqa: F401,E501


class VolumeUpdateReq(object):
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
        'block_volume': 'VolumeUpdateReqVolume'
    }

    attribute_map = {
        'block_volume': 'block_volume'
    }

    def __init__(self, block_volume=None):  # noqa: E501
        """VolumeUpdateReq - a model defined in Swagger"""  # noqa: E501

        self._block_volume = None
        self.discriminator = None

        self.block_volume = block_volume

    @property
    def block_volume(self):
        """Gets the block_volume of this VolumeUpdateReq.  # noqa: E501


        :return: The block_volume of this VolumeUpdateReq.  # noqa: E501
        :rtype: VolumeUpdateReqVolume
        """
        return self._block_volume

    @block_volume.setter
    def block_volume(self, block_volume):
        """Sets the block_volume of this VolumeUpdateReq.


        :param block_volume: The block_volume of this VolumeUpdateReq.  # noqa: E501
        :type: VolumeUpdateReqVolume
        """
        if block_volume is None:
            raise ValueError("Invalid value for `block_volume`, must not be `None`")  # noqa: E501

        self._block_volume = block_volume

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
        if not isinstance(other, VolumeUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
