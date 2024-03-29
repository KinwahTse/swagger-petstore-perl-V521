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

# from xms_client.models.os_external_storage_class_create_req_external_storage_class_external_storage_platforms_elt import OSExternalStorageClassCreateReqExternalStorageClassExternalStoragePlatformsElt  # noqa: F401,E501
# from xms_client.models.slice_string_field import SliceStringField  # noqa: F401,E501


class OSExternalStorageClassCreateReqExternalStorageClass(object):
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
        'class_id': 'str',
        'description': 'str',
        'external_storage_platforms': 'list[OSExternalStorageClassCreateReqExternalStorageClassExternalStoragePlatformsElt]',
        'name': 'str',
        'os_policy_id': 'int',
        'platform': 'str',
        'platform_type': 'str',
        'prefix_enabled': 'bool',
        'storage_pattern': 'SliceStringField'
    }

    attribute_map = {
        'class_id': 'class_id',
        'description': 'description',
        'external_storage_platforms': 'external_storage_platforms',
        'name': 'name',
        'os_policy_id': 'os_policy_id',
        'platform': 'platform',
        'platform_type': 'platform_type',
        'prefix_enabled': 'prefix_enabled',
        'storage_pattern': 'storage_pattern'
    }

    def __init__(self, class_id=None, description=None, external_storage_platforms=None, name=None, os_policy_id=None, platform=None, platform_type=None, prefix_enabled=None, storage_pattern=None):  # noqa: E501
        """OSExternalStorageClassCreateReqExternalStorageClass - a model defined in Swagger"""  # noqa: E501

        self._class_id = None
        self._description = None
        self._external_storage_platforms = None
        self._name = None
        self._os_policy_id = None
        self._platform = None
        self._platform_type = None
        self._prefix_enabled = None
        self._storage_pattern = None
        self.discriminator = None

        self.class_id = class_id
        if description is not None:
            self.description = description
        self.external_storage_platforms = external_storage_platforms
        self.name = name
        self.os_policy_id = os_policy_id
        self.platform = platform
        self.platform_type = platform_type
        if prefix_enabled is not None:
            self.prefix_enabled = prefix_enabled
        if storage_pattern is not None:
            self.storage_pattern = storage_pattern

    @property
    def class_id(self):
        """Gets the class_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The class_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param class_id: The class_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: str
        """
        if class_id is None:
            raise ValueError("Invalid value for `class_id`, must not be `None`")  # noqa: E501

        self._class_id = class_id

    @property
    def description(self):
        """Gets the description of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The description of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param description: The description of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_storage_platforms(self):
        """Gets the external_storage_platforms of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The external_storage_platforms of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: list[OSExternalStorageClassCreateReqExternalStorageClassExternalStoragePlatformsElt]
        """
        return self._external_storage_platforms

    @external_storage_platforms.setter
    def external_storage_platforms(self, external_storage_platforms):
        """Sets the external_storage_platforms of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param external_storage_platforms: The external_storage_platforms of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: list[OSExternalStorageClassCreateReqExternalStorageClassExternalStoragePlatformsElt]
        """
        if external_storage_platforms is None:
            raise ValueError("Invalid value for `external_storage_platforms`, must not be `None`")  # noqa: E501

        self._external_storage_platforms = external_storage_platforms

    @property
    def name(self):
        """Gets the name of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The name of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param name: The name of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def os_policy_id(self):
        """Gets the os_policy_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The os_policy_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: int
        """
        return self._os_policy_id

    @os_policy_id.setter
    def os_policy_id(self, os_policy_id):
        """Sets the os_policy_id of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param os_policy_id: The os_policy_id of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: int
        """
        if os_policy_id is None:
            raise ValueError("Invalid value for `os_policy_id`, must not be `None`")  # noqa: E501

        self._os_policy_id = os_policy_id

    @property
    def platform(self):
        """Gets the platform of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The platform of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param platform: The platform of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: str
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def platform_type(self):
        """Gets the platform_type of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The platform_type of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param platform_type: The platform_type of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: str
        """
        if platform_type is None:
            raise ValueError("Invalid value for `platform_type`, must not be `None`")  # noqa: E501

        self._platform_type = platform_type

    @property
    def prefix_enabled(self):
        """Gets the prefix_enabled of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The prefix_enabled of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: bool
        """
        return self._prefix_enabled

    @prefix_enabled.setter
    def prefix_enabled(self, prefix_enabled):
        """Sets the prefix_enabled of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param prefix_enabled: The prefix_enabled of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: bool
        """

        self._prefix_enabled = prefix_enabled

    @property
    def storage_pattern(self):
        """Gets the storage_pattern of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501


        :return: The storage_pattern of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :rtype: SliceStringField
        """
        return self._storage_pattern

    @storage_pattern.setter
    def storage_pattern(self, storage_pattern):
        """Sets the storage_pattern of this OSExternalStorageClassCreateReqExternalStorageClass.


        :param storage_pattern: The storage_pattern of this OSExternalStorageClassCreateReqExternalStorageClass.  # noqa: E501
        :type: SliceStringField
        """

        self._storage_pattern = storage_pattern

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
        if not isinstance(other, OSExternalStorageClassCreateReqExternalStorageClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
