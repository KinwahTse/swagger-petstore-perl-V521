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


class VolumePairInfo(object):
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
        'dest_pool_id': 'int',
        'dest_pool_name': 'str',
        'dest_volume_name': 'str',
        'src_volume_id': 'int'
    }

    attribute_map = {
        'dest_pool_id': 'dest_pool_id',
        'dest_pool_name': 'dest_pool_name',
        'dest_volume_name': 'dest_volume_name',
        'src_volume_id': 'src_volume_id'
    }

    def __init__(self, dest_pool_id=None, dest_pool_name=None, dest_volume_name=None, src_volume_id=None):  # noqa: E501
        """VolumePairInfo - a model defined in Swagger"""  # noqa: E501

        self._dest_pool_id = None
        self._dest_pool_name = None
        self._dest_volume_name = None
        self._src_volume_id = None
        self.discriminator = None

        self.dest_pool_id = dest_pool_id
        self.dest_pool_name = dest_pool_name
        self.dest_volume_name = dest_volume_name
        self.src_volume_id = src_volume_id

    @property
    def dest_pool_id(self):
        """Gets the dest_pool_id of this VolumePairInfo.  # noqa: E501

        destination pool id  # noqa: E501

        :return: The dest_pool_id of this VolumePairInfo.  # noqa: E501
        :rtype: int
        """
        return self._dest_pool_id

    @dest_pool_id.setter
    def dest_pool_id(self, dest_pool_id):
        """Sets the dest_pool_id of this VolumePairInfo.

        destination pool id  # noqa: E501

        :param dest_pool_id: The dest_pool_id of this VolumePairInfo.  # noqa: E501
        :type: int
        """
        if dest_pool_id is None:
            raise ValueError("Invalid value for `dest_pool_id`, must not be `None`")  # noqa: E501

        self._dest_pool_id = dest_pool_id

    @property
    def dest_pool_name(self):
        """Gets the dest_pool_name of this VolumePairInfo.  # noqa: E501

        destination pool name  # noqa: E501

        :return: The dest_pool_name of this VolumePairInfo.  # noqa: E501
        :rtype: str
        """
        return self._dest_pool_name

    @dest_pool_name.setter
    def dest_pool_name(self, dest_pool_name):
        """Sets the dest_pool_name of this VolumePairInfo.

        destination pool name  # noqa: E501

        :param dest_pool_name: The dest_pool_name of this VolumePairInfo.  # noqa: E501
        :type: str
        """
        if dest_pool_name is None:
            raise ValueError("Invalid value for `dest_pool_name`, must not be `None`")  # noqa: E501

        self._dest_pool_name = dest_pool_name

    @property
    def dest_volume_name(self):
        """Gets the dest_volume_name of this VolumePairInfo.  # noqa: E501

        destination volume name  # noqa: E501

        :return: The dest_volume_name of this VolumePairInfo.  # noqa: E501
        :rtype: str
        """
        return self._dest_volume_name

    @dest_volume_name.setter
    def dest_volume_name(self, dest_volume_name):
        """Sets the dest_volume_name of this VolumePairInfo.

        destination volume name  # noqa: E501

        :param dest_volume_name: The dest_volume_name of this VolumePairInfo.  # noqa: E501
        :type: str
        """
        if dest_volume_name is None:
            raise ValueError("Invalid value for `dest_volume_name`, must not be `None`")  # noqa: E501

        self._dest_volume_name = dest_volume_name

    @property
    def src_volume_id(self):
        """Gets the src_volume_id of this VolumePairInfo.  # noqa: E501

        source volume id  # noqa: E501

        :return: The src_volume_id of this VolumePairInfo.  # noqa: E501
        :rtype: int
        """
        return self._src_volume_id

    @src_volume_id.setter
    def src_volume_id(self, src_volume_id):
        """Sets the src_volume_id of this VolumePairInfo.

        source volume id  # noqa: E501

        :param src_volume_id: The src_volume_id of this VolumePairInfo.  # noqa: E501
        :type: int
        """
        if src_volume_id is None:
            raise ValueError("Invalid value for `src_volume_id`, must not be `None`")  # noqa: E501

        self._src_volume_id = src_volume_id

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
        if not isinstance(other, VolumePairInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
