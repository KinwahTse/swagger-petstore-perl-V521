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


class DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster(object):
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
        'fs_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'fs_id': 'fs_id',
        'name': 'name'
    }

    def __init__(self, fs_id=None, name=None):  # noqa: E501
        """DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster - a model defined in Swagger"""  # noqa: E501

        self._fs_id = None
        self._name = None
        self.discriminator = None

        self.fs_id = fs_id
        self.name = name

    @property
    def fs_id(self):
        """Gets the fs_id of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501


        :return: The fs_id of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501
        :rtype: str
        """
        return self._fs_id

    @fs_id.setter
    def fs_id(self, fs_id):
        """Sets the fs_id of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.


        :param fs_id: The fs_id of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501
        :type: str
        """
        if fs_id is None:
            raise ValueError("Invalid value for `fs_id`, must not be `None`")  # noqa: E501

        self._fs_id = fs_id

    @property
    def name(self):
        """Gets the name of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501


        :return: The name of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.


        :param name: The name of this DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, DpBlockSnapshotRecoveryJobCreateReqJobBackupCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
