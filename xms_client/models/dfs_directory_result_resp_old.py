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


class DfsDirectoryResultRespOld(object):
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
        'path': 'str',
        'result': 'str'
    }

    attribute_map = {
        'path': 'path',
        'result': 'result'
    }

    def __init__(self, path=None, result=None):  # noqa: E501
        """DfsDirectoryResultRespOld - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._result = None
        self.discriminator = None

        self.path = path
        self.result = result

    @property
    def path(self):
        """Gets the path of this DfsDirectoryResultRespOld.  # noqa: E501

        directory path  # noqa: E501

        :return: The path of this DfsDirectoryResultRespOld.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsDirectoryResultRespOld.

        directory path  # noqa: E501

        :param path: The path of this DfsDirectoryResultRespOld.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def result(self):
        """Gets the result of this DfsDirectoryResultRespOld.  # noqa: E501

        operation result  # noqa: E501

        :return: The result of this DfsDirectoryResultRespOld.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DfsDirectoryResultRespOld.

        operation result  # noqa: E501

        :param result: The result of this DfsDirectoryResultRespOld.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

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
        if not isinstance(other, DfsDirectoryResultRespOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other