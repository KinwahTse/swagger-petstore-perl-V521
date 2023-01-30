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


class DfsHdfsACLReq(object):
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
        'fs_user_group_id': 'int',
        'fs_user_id': 'int',
        'permission': 'str',
        'security': 'str',
        'type': 'str'
    }

    attribute_map = {
        'fs_user_group_id': 'fs_user_group_id',
        'fs_user_id': 'fs_user_id',
        'permission': 'permission',
        'security': 'security',
        'type': 'type'
    }

    def __init__(self, fs_user_group_id=None, fs_user_id=None, permission=None, security=None, type=None):  # noqa: E501
        """DfsHdfsACLReq - a model defined in Swagger"""  # noqa: E501

        self._fs_user_group_id = None
        self._fs_user_id = None
        self._permission = None
        self._security = None
        self._type = None
        self.discriminator = None

        if fs_user_group_id is not None:
            self.fs_user_group_id = fs_user_group_id
        if fs_user_id is not None:
            self.fs_user_id = fs_user_id
        if permission is not None:
            self.permission = permission
        if security is not None:
            self.security = security
        if type is not None:
            self.type = type

    @property
    def fs_user_group_id(self):
        """Gets the fs_user_group_id of this DfsHdfsACLReq.  # noqa: E501

        fs user group id  # noqa: E501

        :return: The fs_user_group_id of this DfsHdfsACLReq.  # noqa: E501
        :rtype: int
        """
        return self._fs_user_group_id

    @fs_user_group_id.setter
    def fs_user_group_id(self, fs_user_group_id):
        """Sets the fs_user_group_id of this DfsHdfsACLReq.

        fs user group id  # noqa: E501

        :param fs_user_group_id: The fs_user_group_id of this DfsHdfsACLReq.  # noqa: E501
        :type: int
        """

        self._fs_user_group_id = fs_user_group_id

    @property
    def fs_user_id(self):
        """Gets the fs_user_id of this DfsHdfsACLReq.  # noqa: E501

        fs user id  # noqa: E501

        :return: The fs_user_id of this DfsHdfsACLReq.  # noqa: E501
        :rtype: int
        """
        return self._fs_user_id

    @fs_user_id.setter
    def fs_user_id(self, fs_user_id):
        """Sets the fs_user_id of this DfsHdfsACLReq.

        fs user id  # noqa: E501

        :param fs_user_id: The fs_user_id of this DfsHdfsACLReq.  # noqa: E501
        :type: int
        """

        self._fs_user_id = fs_user_id

    @property
    def permission(self):
        """Gets the permission of this DfsHdfsACLReq.  # noqa: E501

        permission of user or group  # noqa: E501

        :return: The permission of this DfsHdfsACLReq.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DfsHdfsACLReq.

        permission of user or group  # noqa: E501

        :param permission: The permission of this DfsHdfsACLReq.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def security(self):
        """Gets the security of this DfsHdfsACLReq.  # noqa: E501

        acl security type  # noqa: E501

        :return: The security of this DfsHdfsACLReq.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this DfsHdfsACLReq.

        acl security type  # noqa: E501

        :param security: The security of this DfsHdfsACLReq.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def type(self):
        """Gets the type of this DfsHdfsACLReq.  # noqa: E501

        acl type  # noqa: E501

        :return: The type of this DfsHdfsACLReq.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DfsHdfsACLReq.

        acl type  # noqa: E501

        :param type: The type of this DfsHdfsACLReq.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, DfsHdfsACLReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other