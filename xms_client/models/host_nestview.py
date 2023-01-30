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


class HostNestview(object):
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
        'admin_ip': 'str',
        'id': 'int',
        'name': 'str',
        'numa_nodes': 'str',
        'up': 'bool'
    }

    attribute_map = {
        'admin_ip': 'admin_ip',
        'id': 'id',
        'name': 'name',
        'numa_nodes': 'numa_nodes',
        'up': 'up'
    }

    def __init__(self, admin_ip=None, id=None, name=None, numa_nodes=None, up=None):  # noqa: E501
        """HostNestview - a model defined in Swagger"""  # noqa: E501

        self._admin_ip = None
        self._id = None
        self._name = None
        self._numa_nodes = None
        self._up = None
        self.discriminator = None

        self.admin_ip = admin_ip
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if numa_nodes is not None:
            self.numa_nodes = numa_nodes
        if up is not None:
            self.up = up

    @property
    def admin_ip(self):
        """Gets the admin_ip of this HostNestview.  # noqa: E501


        :return: The admin_ip of this HostNestview.  # noqa: E501
        :rtype: str
        """
        return self._admin_ip

    @admin_ip.setter
    def admin_ip(self, admin_ip):
        """Sets the admin_ip of this HostNestview.


        :param admin_ip: The admin_ip of this HostNestview.  # noqa: E501
        :type: str
        """
        if admin_ip is None:
            raise ValueError("Invalid value for `admin_ip`, must not be `None`")  # noqa: E501

        self._admin_ip = admin_ip

    @property
    def id(self):
        """Gets the id of this HostNestview.  # noqa: E501


        :return: The id of this HostNestview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostNestview.


        :param id: The id of this HostNestview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HostNestview.  # noqa: E501


        :return: The name of this HostNestview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostNestview.


        :param name: The name of this HostNestview.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def numa_nodes(self):
        """Gets the numa_nodes of this HostNestview.  # noqa: E501


        :return: The numa_nodes of this HostNestview.  # noqa: E501
        :rtype: str
        """
        return self._numa_nodes

    @numa_nodes.setter
    def numa_nodes(self, numa_nodes):
        """Sets the numa_nodes of this HostNestview.


        :param numa_nodes: The numa_nodes of this HostNestview.  # noqa: E501
        :type: str
        """

        self._numa_nodes = numa_nodes

    @property
    def up(self):
        """Gets the up of this HostNestview.  # noqa: E501


        :return: The up of this HostNestview.  # noqa: E501
        :rtype: bool
        """
        return self._up

    @up.setter
    def up(self, up):
        """Sets the up of this HostNestview.


        :param up: The up of this HostNestview.  # noqa: E501
        :type: bool
        """

        self._up = up

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
        if not isinstance(other, HostNestview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
