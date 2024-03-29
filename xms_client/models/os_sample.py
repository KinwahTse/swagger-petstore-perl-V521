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

# from xms_client.models.os_bucket_usage_category import OSBucketUsageCategory  # noqa: F401,E501


class OSSample(object):
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
        'delete_obj_category': 'OSBucketUsageCategory',
        'get_obj_category': 'OSBucketUsageCategory',
        'list_bucket_category': 'OSBucketUsageCategory',
        'objects': 'int',
        'post_obj_category': 'OSBucketUsageCategory',
        'put_obj_category': 'OSBucketUsageCategory',
        'used_capacity_bytes': 'dict(str, int)'
    }

    attribute_map = {
        'delete_obj_category': 'delete_obj_category',
        'get_obj_category': 'get_obj_category',
        'list_bucket_category': 'list_bucket_category',
        'objects': 'objects',
        'post_obj_category': 'post_obj_category',
        'put_obj_category': 'put_obj_category',
        'used_capacity_bytes': 'used_capacity_bytes'
    }

    def __init__(self, delete_obj_category=None, get_obj_category=None, list_bucket_category=None, objects=None, post_obj_category=None, put_obj_category=None, used_capacity_bytes=None):  # noqa: E501
        """OSSample - a model defined in Swagger"""  # noqa: E501

        self._delete_obj_category = None
        self._get_obj_category = None
        self._list_bucket_category = None
        self._objects = None
        self._post_obj_category = None
        self._put_obj_category = None
        self._used_capacity_bytes = None
        self.discriminator = None

        if delete_obj_category is not None:
            self.delete_obj_category = delete_obj_category
        if get_obj_category is not None:
            self.get_obj_category = get_obj_category
        if list_bucket_category is not None:
            self.list_bucket_category = list_bucket_category
        if objects is not None:
            self.objects = objects
        if post_obj_category is not None:
            self.post_obj_category = post_obj_category
        if put_obj_category is not None:
            self.put_obj_category = put_obj_category
        if used_capacity_bytes is not None:
            self.used_capacity_bytes = used_capacity_bytes

    @property
    def delete_obj_category(self):
        """Gets the delete_obj_category of this OSSample.  # noqa: E501


        :return: The delete_obj_category of this OSSample.  # noqa: E501
        :rtype: OSBucketUsageCategory
        """
        return self._delete_obj_category

    @delete_obj_category.setter
    def delete_obj_category(self, delete_obj_category):
        """Sets the delete_obj_category of this OSSample.


        :param delete_obj_category: The delete_obj_category of this OSSample.  # noqa: E501
        :type: OSBucketUsageCategory
        """

        self._delete_obj_category = delete_obj_category

    @property
    def get_obj_category(self):
        """Gets the get_obj_category of this OSSample.  # noqa: E501


        :return: The get_obj_category of this OSSample.  # noqa: E501
        :rtype: OSBucketUsageCategory
        """
        return self._get_obj_category

    @get_obj_category.setter
    def get_obj_category(self, get_obj_category):
        """Sets the get_obj_category of this OSSample.


        :param get_obj_category: The get_obj_category of this OSSample.  # noqa: E501
        :type: OSBucketUsageCategory
        """

        self._get_obj_category = get_obj_category

    @property
    def list_bucket_category(self):
        """Gets the list_bucket_category of this OSSample.  # noqa: E501


        :return: The list_bucket_category of this OSSample.  # noqa: E501
        :rtype: OSBucketUsageCategory
        """
        return self._list_bucket_category

    @list_bucket_category.setter
    def list_bucket_category(self, list_bucket_category):
        """Sets the list_bucket_category of this OSSample.


        :param list_bucket_category: The list_bucket_category of this OSSample.  # noqa: E501
        :type: OSBucketUsageCategory
        """

        self._list_bucket_category = list_bucket_category

    @property
    def objects(self):
        """Gets the objects of this OSSample.  # noqa: E501


        :return: The objects of this OSSample.  # noqa: E501
        :rtype: int
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this OSSample.


        :param objects: The objects of this OSSample.  # noqa: E501
        :type: int
        """

        self._objects = objects

    @property
    def post_obj_category(self):
        """Gets the post_obj_category of this OSSample.  # noqa: E501


        :return: The post_obj_category of this OSSample.  # noqa: E501
        :rtype: OSBucketUsageCategory
        """
        return self._post_obj_category

    @post_obj_category.setter
    def post_obj_category(self, post_obj_category):
        """Sets the post_obj_category of this OSSample.


        :param post_obj_category: The post_obj_category of this OSSample.  # noqa: E501
        :type: OSBucketUsageCategory
        """

        self._post_obj_category = post_obj_category

    @property
    def put_obj_category(self):
        """Gets the put_obj_category of this OSSample.  # noqa: E501


        :return: The put_obj_category of this OSSample.  # noqa: E501
        :rtype: OSBucketUsageCategory
        """
        return self._put_obj_category

    @put_obj_category.setter
    def put_obj_category(self, put_obj_category):
        """Sets the put_obj_category of this OSSample.


        :param put_obj_category: The put_obj_category of this OSSample.  # noqa: E501
        :type: OSBucketUsageCategory
        """

        self._put_obj_category = put_obj_category

    @property
    def used_capacity_bytes(self):
        """Gets the used_capacity_bytes of this OSSample.  # noqa: E501


        :return: The used_capacity_bytes of this OSSample.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._used_capacity_bytes

    @used_capacity_bytes.setter
    def used_capacity_bytes(self, used_capacity_bytes):
        """Sets the used_capacity_bytes of this OSSample.


        :param used_capacity_bytes: The used_capacity_bytes of this OSSample.  # noqa: E501
        :type: dict(str, int)
        """

        self._used_capacity_bytes = used_capacity_bytes

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
        if not isinstance(other, OSSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
