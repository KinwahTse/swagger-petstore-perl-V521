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

# from xms_client.models.dfs_path_nestview_dfs_path_stat import DfsPathNestviewDfsPathStat  # noqa: F401,E501


class DfsPathNestview(object):
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
        'dfs_path_stat': 'DfsPathNestviewDfsPathStat',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'dfs_path_stat': 'dfs_path_stat',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, dfs_path_stat=None, id=None, name=None):  # noqa: E501
        """DfsPathNestview - a model defined in Swagger"""  # noqa: E501

        self._dfs_path_stat = None
        self._id = None
        self._name = None
        self.discriminator = None

        if dfs_path_stat is not None:
            self.dfs_path_stat = dfs_path_stat
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def dfs_path_stat(self):
        """Gets the dfs_path_stat of this DfsPathNestview.  # noqa: E501


        :return: The dfs_path_stat of this DfsPathNestview.  # noqa: E501
        :rtype: DfsPathNestviewDfsPathStat
        """
        return self._dfs_path_stat

    @dfs_path_stat.setter
    def dfs_path_stat(self, dfs_path_stat):
        """Sets the dfs_path_stat of this DfsPathNestview.


        :param dfs_path_stat: The dfs_path_stat of this DfsPathNestview.  # noqa: E501
        :type: DfsPathNestviewDfsPathStat
        """

        self._dfs_path_stat = dfs_path_stat

    @property
    def id(self):
        """Gets the id of this DfsPathNestview.  # noqa: E501


        :return: The id of this DfsPathNestview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsPathNestview.


        :param id: The id of this DfsPathNestview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DfsPathNestview.  # noqa: E501


        :return: The name of this DfsPathNestview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DfsPathNestview.


        :param name: The name of this DfsPathNestview.  # noqa: E501
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
        if not isinstance(other, DfsPathNestview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other