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


class OSBucketSetAccessLoggingReqBucket(object):
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
        'logging_grants': 'list[object]',
        'logging_owner_id': 'int',
        'logging_prefix': 'str',
        'logging_target_bucket_id': 'int'
    }

    attribute_map = {
        'logging_grants': 'logging_grants',
        'logging_owner_id': 'logging_owner_id',
        'logging_prefix': 'logging_prefix',
        'logging_target_bucket_id': 'logging_target_bucket_id'
    }

    def __init__(self, logging_grants=None, logging_owner_id=None, logging_prefix=None, logging_target_bucket_id=None):  # noqa: E501
        """OSBucketSetAccessLoggingReqBucket - a model defined in Swagger"""  # noqa: E501

        self._logging_grants = None
        self._logging_owner_id = None
        self._logging_prefix = None
        self._logging_target_bucket_id = None
        self.discriminator = None

        if logging_grants is not None:
            self.logging_grants = logging_grants
        if logging_owner_id is not None:
            self.logging_owner_id = logging_owner_id
        if logging_prefix is not None:
            self.logging_prefix = logging_prefix
        if logging_target_bucket_id is not None:
            self.logging_target_bucket_id = logging_target_bucket_id

    @property
    def logging_grants(self):
        """Gets the logging_grants of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501


        :return: The logging_grants of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :rtype: list[object]
        """
        return self._logging_grants

    @logging_grants.setter
    def logging_grants(self, logging_grants):
        """Sets the logging_grants of this OSBucketSetAccessLoggingReqBucket.


        :param logging_grants: The logging_grants of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :type: list[object]
        """

        self._logging_grants = logging_grants

    @property
    def logging_owner_id(self):
        """Gets the logging_owner_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501


        :return: The logging_owner_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._logging_owner_id

    @logging_owner_id.setter
    def logging_owner_id(self, logging_owner_id):
        """Sets the logging_owner_id of this OSBucketSetAccessLoggingReqBucket.


        :param logging_owner_id: The logging_owner_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :type: int
        """

        self._logging_owner_id = logging_owner_id

    @property
    def logging_prefix(self):
        """Gets the logging_prefix of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501


        :return: The logging_prefix of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._logging_prefix

    @logging_prefix.setter
    def logging_prefix(self, logging_prefix):
        """Sets the logging_prefix of this OSBucketSetAccessLoggingReqBucket.


        :param logging_prefix: The logging_prefix of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :type: str
        """

        self._logging_prefix = logging_prefix

    @property
    def logging_target_bucket_id(self):
        """Gets the logging_target_bucket_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501


        :return: The logging_target_bucket_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._logging_target_bucket_id

    @logging_target_bucket_id.setter
    def logging_target_bucket_id(self, logging_target_bucket_id):
        """Sets the logging_target_bucket_id of this OSBucketSetAccessLoggingReqBucket.


        :param logging_target_bucket_id: The logging_target_bucket_id of this OSBucketSetAccessLoggingReqBucket.  # noqa: E501
        :type: int
        """

        self._logging_target_bucket_id = logging_target_bucket_id

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
        if not isinstance(other, OSBucketSetAccessLoggingReqBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
