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


class DfsSnapshotCreateReqDfsSnapshot(object):
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
        'description': 'str',
        'name': 'str',
        'path': 'str',
        'retention': 'str',
        'rootfs_id': 'int'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'path': 'path',
        'retention': 'retention',
        'rootfs_id': 'rootfs_id'
    }

    def __init__(self, description=None, name=None, path=None, retention=None, rootfs_id=None):  # noqa: E501
        """DfsSnapshotCreateReqDfsSnapshot - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._path = None
        self._retention = None
        self._rootfs_id = None
        self.discriminator = None

        self.description = description
        self.name = name
        self.path = path
        self.retention = retention
        self.rootfs_id = rootfs_id

    @property
    def description(self):
        """Gets the description of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501

        description  # noqa: E501

        :return: The description of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DfsSnapshotCreateReqDfsSnapshot.

        description  # noqa: E501

        :param description: The description of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501

        snapshot name  # noqa: E501

        :return: The name of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DfsSnapshotCreateReqDfsSnapshot.

        snapshot name  # noqa: E501

        :param name: The name of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501

        path  # noqa: E501

        :return: The path of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsSnapshotCreateReqDfsSnapshot.

        path  # noqa: E501

        :param path: The path of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def retention(self):
        """Gets the retention of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501

        retention time  # noqa: E501

        :return: The retention of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this DfsSnapshotCreateReqDfsSnapshot.

        retention time  # noqa: E501

        :param retention: The retention of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :type: str
        """
        if retention is None:
            raise ValueError("Invalid value for `retention`, must not be `None`")  # noqa: E501

        self._retention = retention

    @property
    def rootfs_id(self):
        """Gets the rootfs_id of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501

        id of dfs rootfs  # noqa: E501

        :return: The rootfs_id of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._rootfs_id

    @rootfs_id.setter
    def rootfs_id(self, rootfs_id):
        """Sets the rootfs_id of this DfsSnapshotCreateReqDfsSnapshot.

        id of dfs rootfs  # noqa: E501

        :param rootfs_id: The rootfs_id of this DfsSnapshotCreateReqDfsSnapshot.  # noqa: E501
        :type: int
        """
        if rootfs_id is None:
            raise ValueError("Invalid value for `rootfs_id`, must not be `None`")  # noqa: E501

        self._rootfs_id = rootfs_id

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
        if not isinstance(other, DfsSnapshotCreateReqDfsSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other