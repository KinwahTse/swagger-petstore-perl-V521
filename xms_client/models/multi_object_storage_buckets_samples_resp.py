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

# from xms_client.models.object_storage_bucket_samples_elem import ObjectStorageBucketSamplesElem  # noqa: F401,E501


class MultiObjectStorageBucketsSamplesResp(object):
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
        'os_buckets_samples': 'list[ObjectStorageBucketSamplesElem]'
    }

    attribute_map = {
        'os_buckets_samples': 'os_buckets_samples'
    }

    def __init__(self, os_buckets_samples=None):  # noqa: E501
        """MultiObjectStorageBucketsSamplesResp - a model defined in Swagger"""  # noqa: E501

        self._os_buckets_samples = None
        self.discriminator = None

        if os_buckets_samples is not None:
            self.os_buckets_samples = os_buckets_samples

    @property
    def os_buckets_samples(self):
        """Gets the os_buckets_samples of this MultiObjectStorageBucketsSamplesResp.  # noqa: E501


        :return: The os_buckets_samples of this MultiObjectStorageBucketsSamplesResp.  # noqa: E501
        :rtype: list[ObjectStorageBucketSamplesElem]
        """
        return self._os_buckets_samples

    @os_buckets_samples.setter
    def os_buckets_samples(self, os_buckets_samples):
        """Sets the os_buckets_samples of this MultiObjectStorageBucketsSamplesResp.


        :param os_buckets_samples: The os_buckets_samples of this MultiObjectStorageBucketsSamplesResp.  # noqa: E501
        :type: list[ObjectStorageBucketSamplesElem]
        """

        self._os_buckets_samples = os_buckets_samples

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
        if not isinstance(other, MultiObjectStorageBucketsSamplesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
