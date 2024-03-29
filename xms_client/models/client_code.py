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


class ClientCode(object):
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
        'code': 'str',
        'create': 'datetime',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'create': 'create',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, code=None, create=None, id=None, type=None):  # noqa: E501
        """ClientCode - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._create = None
        self._id = None
        self._type = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def code(self):
        """Gets the code of this ClientCode.  # noqa: E501


        :return: The code of this ClientCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ClientCode.


        :param code: The code of this ClientCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def create(self):
        """Gets the create of this ClientCode.  # noqa: E501


        :return: The create of this ClientCode.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ClientCode.


        :param create: The create of this ClientCode.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this ClientCode.  # noqa: E501


        :return: The id of this ClientCode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientCode.


        :param id: The id of this ClientCode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ClientCode.  # noqa: E501


        :return: The type of this ClientCode.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientCode.


        :param type: The type of this ClientCode.  # noqa: E501
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
        if not isinstance(other, ClientCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
