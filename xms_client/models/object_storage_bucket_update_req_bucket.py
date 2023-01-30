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

# from xms_client.models.bucket_flag_req import BucketFlagReq  # noqa: F401,E501
# from xms_client.models.os_bucket_qos import OSBucketQos  # noqa: F401,E501


class ObjectStorageBucketUpdateReqBucket(object):
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
        'all_user_permission': 'str',
        'auth_user_permission': 'str',
        'delete_archive_storage_class': 'str',
        'description': 'str',
        'external_quota_max_objects': 'int',
        'external_quota_max_size': 'int',
        'flag': 'BucketFlagReq',
        'local_quota_max_objects': 'int',
        'local_quota_max_size': 'int',
        'log_delivery_permission': 'str',
        'owner_id': 'int',
        'owner_permission': 'str',
        'qos': 'OSBucketQos',
        'quota_max_objects': 'int',
        'quota_max_size': 'int',
        'restore_days': 'int'
    }

    attribute_map = {
        'all_user_permission': 'all_user_permission',
        'auth_user_permission': 'auth_user_permission',
        'delete_archive_storage_class': 'delete_archive_storage_class',
        'description': 'description',
        'external_quota_max_objects': 'external_quota_max_objects',
        'external_quota_max_size': 'external_quota_max_size',
        'flag': 'flag',
        'local_quota_max_objects': 'local_quota_max_objects',
        'local_quota_max_size': 'local_quota_max_size',
        'log_delivery_permission': 'log_delivery_permission',
        'owner_id': 'owner_id',
        'owner_permission': 'owner_permission',
        'qos': 'qos',
        'quota_max_objects': 'quota_max_objects',
        'quota_max_size': 'quota_max_size',
        'restore_days': 'restore_days'
    }

    def __init__(self, all_user_permission=None, auth_user_permission=None, delete_archive_storage_class=None, description=None, external_quota_max_objects=None, external_quota_max_size=None, flag=None, local_quota_max_objects=None, local_quota_max_size=None, log_delivery_permission=None, owner_id=None, owner_permission=None, qos=None, quota_max_objects=None, quota_max_size=None, restore_days=None):  # noqa: E501
        """ObjectStorageBucketUpdateReqBucket - a model defined in Swagger"""  # noqa: E501

        self._all_user_permission = None
        self._auth_user_permission = None
        self._delete_archive_storage_class = None
        self._description = None
        self._external_quota_max_objects = None
        self._external_quota_max_size = None
        self._flag = None
        self._local_quota_max_objects = None
        self._local_quota_max_size = None
        self._log_delivery_permission = None
        self._owner_id = None
        self._owner_permission = None
        self._qos = None
        self._quota_max_objects = None
        self._quota_max_size = None
        self._restore_days = None
        self.discriminator = None

        if all_user_permission is not None:
            self.all_user_permission = all_user_permission
        if auth_user_permission is not None:
            self.auth_user_permission = auth_user_permission
        if delete_archive_storage_class is not None:
            self.delete_archive_storage_class = delete_archive_storage_class
        if description is not None:
            self.description = description
        if external_quota_max_objects is not None:
            self.external_quota_max_objects = external_quota_max_objects
        if external_quota_max_size is not None:
            self.external_quota_max_size = external_quota_max_size
        if flag is not None:
            self.flag = flag
        if local_quota_max_objects is not None:
            self.local_quota_max_objects = local_quota_max_objects
        if local_quota_max_size is not None:
            self.local_quota_max_size = local_quota_max_size
        if log_delivery_permission is not None:
            self.log_delivery_permission = log_delivery_permission
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_permission is not None:
            self.owner_permission = owner_permission
        if qos is not None:
            self.qos = qos
        if quota_max_objects is not None:
            self.quota_max_objects = quota_max_objects
        if quota_max_size is not None:
            self.quota_max_size = quota_max_size
        if restore_days is not None:
            self.restore_days = restore_days

    @property
    def all_user_permission(self):
        """Gets the all_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The all_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._all_user_permission

    @all_user_permission.setter
    def all_user_permission(self, all_user_permission):
        """Sets the all_user_permission of this ObjectStorageBucketUpdateReqBucket.


        :param all_user_permission: The all_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._all_user_permission = all_user_permission

    @property
    def auth_user_permission(self):
        """Gets the auth_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The auth_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._auth_user_permission

    @auth_user_permission.setter
    def auth_user_permission(self, auth_user_permission):
        """Sets the auth_user_permission of this ObjectStorageBucketUpdateReqBucket.


        :param auth_user_permission: The auth_user_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._auth_user_permission = auth_user_permission

    @property
    def delete_archive_storage_class(self):
        """Gets the delete_archive_storage_class of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The delete_archive_storage_class of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._delete_archive_storage_class

    @delete_archive_storage_class.setter
    def delete_archive_storage_class(self, delete_archive_storage_class):
        """Sets the delete_archive_storage_class of this ObjectStorageBucketUpdateReqBucket.


        :param delete_archive_storage_class: The delete_archive_storage_class of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._delete_archive_storage_class = delete_archive_storage_class

    @property
    def description(self):
        """Gets the description of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The description of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ObjectStorageBucketUpdateReqBucket.


        :param description: The description of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_quota_max_objects(self):
        """Gets the external_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The external_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._external_quota_max_objects

    @external_quota_max_objects.setter
    def external_quota_max_objects(self, external_quota_max_objects):
        """Sets the external_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.


        :param external_quota_max_objects: The external_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._external_quota_max_objects = external_quota_max_objects

    @property
    def external_quota_max_size(self):
        """Gets the external_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The external_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._external_quota_max_size

    @external_quota_max_size.setter
    def external_quota_max_size(self, external_quota_max_size):
        """Sets the external_quota_max_size of this ObjectStorageBucketUpdateReqBucket.


        :param external_quota_max_size: The external_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._external_quota_max_size = external_quota_max_size

    @property
    def flag(self):
        """Gets the flag of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The flag of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: BucketFlagReq
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this ObjectStorageBucketUpdateReqBucket.


        :param flag: The flag of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: BucketFlagReq
        """

        self._flag = flag

    @property
    def local_quota_max_objects(self):
        """Gets the local_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The local_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._local_quota_max_objects

    @local_quota_max_objects.setter
    def local_quota_max_objects(self, local_quota_max_objects):
        """Sets the local_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.


        :param local_quota_max_objects: The local_quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._local_quota_max_objects = local_quota_max_objects

    @property
    def local_quota_max_size(self):
        """Gets the local_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The local_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._local_quota_max_size

    @local_quota_max_size.setter
    def local_quota_max_size(self, local_quota_max_size):
        """Sets the local_quota_max_size of this ObjectStorageBucketUpdateReqBucket.


        :param local_quota_max_size: The local_quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._local_quota_max_size = local_quota_max_size

    @property
    def log_delivery_permission(self):
        """Gets the log_delivery_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The log_delivery_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._log_delivery_permission

    @log_delivery_permission.setter
    def log_delivery_permission(self, log_delivery_permission):
        """Sets the log_delivery_permission of this ObjectStorageBucketUpdateReqBucket.


        :param log_delivery_permission: The log_delivery_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._log_delivery_permission = log_delivery_permission

    @property
    def owner_id(self):
        """Gets the owner_id of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The owner_id of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ObjectStorageBucketUpdateReqBucket.


        :param owner_id: The owner_id of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def owner_permission(self):
        """Gets the owner_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The owner_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: str
        """
        return self._owner_permission

    @owner_permission.setter
    def owner_permission(self, owner_permission):
        """Sets the owner_permission of this ObjectStorageBucketUpdateReqBucket.


        :param owner_permission: The owner_permission of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: str
        """

        self._owner_permission = owner_permission

    @property
    def qos(self):
        """Gets the qos of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The qos of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: OSBucketQos
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """Sets the qos of this ObjectStorageBucketUpdateReqBucket.


        :param qos: The qos of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: OSBucketQos
        """

        self._qos = qos

    @property
    def quota_max_objects(self):
        """Gets the quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._quota_max_objects

    @quota_max_objects.setter
    def quota_max_objects(self, quota_max_objects):
        """Sets the quota_max_objects of this ObjectStorageBucketUpdateReqBucket.


        :param quota_max_objects: The quota_max_objects of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._quota_max_objects = quota_max_objects

    @property
    def quota_max_size(self):
        """Gets the quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._quota_max_size

    @quota_max_size.setter
    def quota_max_size(self, quota_max_size):
        """Sets the quota_max_size of this ObjectStorageBucketUpdateReqBucket.


        :param quota_max_size: The quota_max_size of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._quota_max_size = quota_max_size

    @property
    def restore_days(self):
        """Gets the restore_days of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501


        :return: The restore_days of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :rtype: int
        """
        return self._restore_days

    @restore_days.setter
    def restore_days(self, restore_days):
        """Sets the restore_days of this ObjectStorageBucketUpdateReqBucket.


        :param restore_days: The restore_days of this ObjectStorageBucketUpdateReqBucket.  # noqa: E501
        :type: int
        """

        self._restore_days = restore_days

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
        if not isinstance(other, ObjectStorageBucketUpdateReqBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other