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


class ExtCompatConf(object):
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
        'data': 'str',
        'ext_name': 'str',
        'func_name': 'str',
        'host_id': 'int',
        'policy': 'str'
    }

    attribute_map = {
        'data': 'data',
        'ext_name': 'ext_name',
        'func_name': 'func_name',
        'host_id': 'host_id',
        'policy': 'policy'
    }

    def __init__(self, data=None, ext_name=None, func_name=None, host_id=None, policy=None):  # noqa: E501
        """ExtCompatConf - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._ext_name = None
        self._func_name = None
        self._host_id = None
        self._policy = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if ext_name is not None:
            self.ext_name = ext_name
        if func_name is not None:
            self.func_name = func_name
        if host_id is not None:
            self.host_id = host_id
        if policy is not None:
            self.policy = policy

    @property
    def data(self):
        """Gets the data of this ExtCompatConf.  # noqa: E501

        script or fake data content  # noqa: E501

        :return: The data of this ExtCompatConf.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ExtCompatConf.

        script or fake data content  # noqa: E501

        :param data: The data of this ExtCompatConf.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def ext_name(self):
        """Gets the ext_name of this ExtCompatConf.  # noqa: E501


        :return: The ext_name of this ExtCompatConf.  # noqa: E501
        :rtype: str
        """
        return self._ext_name

    @ext_name.setter
    def ext_name(self, ext_name):
        """Sets the ext_name of this ExtCompatConf.


        :param ext_name: The ext_name of this ExtCompatConf.  # noqa: E501
        :type: str
        """

        self._ext_name = ext_name

    @property
    def func_name(self):
        """Gets the func_name of this ExtCompatConf.  # noqa: E501


        :return: The func_name of this ExtCompatConf.  # noqa: E501
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this ExtCompatConf.


        :param func_name: The func_name of this ExtCompatConf.  # noqa: E501
        :type: str
        """

        self._func_name = func_name

    @property
    def host_id(self):
        """Gets the host_id of this ExtCompatConf.  # noqa: E501

        0 for all hosts  # noqa: E501

        :return: The host_id of this ExtCompatConf.  # noqa: E501
        :rtype: int
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ExtCompatConf.

        0 for all hosts  # noqa: E501

        :param host_id: The host_id of this ExtCompatConf.  # noqa: E501
        :type: int
        """

        self._host_id = host_id

    @property
    def policy(self):
        """Gets the policy of this ExtCompatConf.  # noqa: E501


        :return: The policy of this ExtCompatConf.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ExtCompatConf.


        :param policy: The policy of this ExtCompatConf.  # noqa: E501
        :type: str
        """

        self._policy = policy

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
        if not isinstance(other, ExtCompatConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other