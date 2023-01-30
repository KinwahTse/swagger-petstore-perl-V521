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


class VolumeGroupSnapshotNestview(object):
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
        'group_snapshot_name': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'group_snapshot_name': 'group_snapshot_name',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, group_snapshot_name=None, id=None, name=None):  # noqa: E501
        """VolumeGroupSnapshotNestview - a model defined in Swagger"""  # noqa: E501

        self._group_snapshot_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        if group_snapshot_name is not None:
            self.group_snapshot_name = group_snapshot_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def group_snapshot_name(self):
        """Gets the group_snapshot_name of this VolumeGroupSnapshotNestview.  # noqa: E501


        :return: The group_snapshot_name of this VolumeGroupSnapshotNestview.  # noqa: E501
        :rtype: str
        """
        return self._group_snapshot_name

    @group_snapshot_name.setter
    def group_snapshot_name(self, group_snapshot_name):
        """Sets the group_snapshot_name of this VolumeGroupSnapshotNestview.


        :param group_snapshot_name: The group_snapshot_name of this VolumeGroupSnapshotNestview.  # noqa: E501
        :type: str
        """

        self._group_snapshot_name = group_snapshot_name

    @property
    def id(self):
        """Gets the id of this VolumeGroupSnapshotNestview.  # noqa: E501


        :return: The id of this VolumeGroupSnapshotNestview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeGroupSnapshotNestview.


        :param id: The id of this VolumeGroupSnapshotNestview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeGroupSnapshotNestview.  # noqa: E501


        :return: The name of this VolumeGroupSnapshotNestview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroupSnapshotNestview.


        :param name: The name of this VolumeGroupSnapshotNestview.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, VolumeGroupSnapshotNestview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
