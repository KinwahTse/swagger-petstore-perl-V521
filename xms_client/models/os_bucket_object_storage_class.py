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

# from xms_client.models.rule_matching_info import RuleMatchingInfo  # noqa: F401,E501


class OSBucketObjectStorageClass(object):
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
        'matching_info': 'RuleMatchingInfo',
        'type': 'str',
        'x_amz_storage_class_enabled': 'bool'
    }

    attribute_map = {
        'matching_info': 'matching_info',
        'type': 'type',
        'x_amz_storage_class_enabled': 'x_amz_storage_class_enabled'
    }

    def __init__(self, matching_info=None, type=None, x_amz_storage_class_enabled=None):  # noqa: E501
        """OSBucketObjectStorageClass - a model defined in Swagger"""  # noqa: E501

        self._matching_info = None
        self._type = None
        self._x_amz_storage_class_enabled = None
        self.discriminator = None

        if matching_info is not None:
            self.matching_info = matching_info
        if type is not None:
            self.type = type
        if x_amz_storage_class_enabled is not None:
            self.x_amz_storage_class_enabled = x_amz_storage_class_enabled

    @property
    def matching_info(self):
        """Gets the matching_info of this OSBucketObjectStorageClass.  # noqa: E501


        :return: The matching_info of this OSBucketObjectStorageClass.  # noqa: E501
        :rtype: RuleMatchingInfo
        """
        return self._matching_info

    @matching_info.setter
    def matching_info(self, matching_info):
        """Sets the matching_info of this OSBucketObjectStorageClass.


        :param matching_info: The matching_info of this OSBucketObjectStorageClass.  # noqa: E501
        :type: RuleMatchingInfo
        """

        self._matching_info = matching_info

    @property
    def type(self):
        """Gets the type of this OSBucketObjectStorageClass.  # noqa: E501


        :return: The type of this OSBucketObjectStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OSBucketObjectStorageClass.


        :param type: The type of this OSBucketObjectStorageClass.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def x_amz_storage_class_enabled(self):
        """Gets the x_amz_storage_class_enabled of this OSBucketObjectStorageClass.  # noqa: E501


        :return: The x_amz_storage_class_enabled of this OSBucketObjectStorageClass.  # noqa: E501
        :rtype: bool
        """
        return self._x_amz_storage_class_enabled

    @x_amz_storage_class_enabled.setter
    def x_amz_storage_class_enabled(self, x_amz_storage_class_enabled):
        """Sets the x_amz_storage_class_enabled of this OSBucketObjectStorageClass.


        :param x_amz_storage_class_enabled: The x_amz_storage_class_enabled of this OSBucketObjectStorageClass.  # noqa: E501
        :type: bool
        """

        self._x_amz_storage_class_enabled = x_amz_storage_class_enabled

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
        if not isinstance(other, OSBucketObjectStorageClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
