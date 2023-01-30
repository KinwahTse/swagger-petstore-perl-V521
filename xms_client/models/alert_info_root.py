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


class AlertInfoRoot(object):
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
        'create': 'datetime',
        'id': 'int',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'create': 'create',
        'id': 'id',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, create=None, id=None, status=None, update=None):  # noqa: E501
        """AlertInfoRoot - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._id = None
        self._status = None
        self._update = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def create(self):
        """Gets the create of this AlertInfoRoot.  # noqa: E501


        :return: The create of this AlertInfoRoot.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this AlertInfoRoot.


        :param create: The create of this AlertInfoRoot.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this AlertInfoRoot.  # noqa: E501


        :return: The id of this AlertInfoRoot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertInfoRoot.


        :param id: The id of this AlertInfoRoot.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this AlertInfoRoot.  # noqa: E501


        :return: The status of this AlertInfoRoot.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertInfoRoot.


        :param status: The status of this AlertInfoRoot.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this AlertInfoRoot.  # noqa: E501


        :return: The update of this AlertInfoRoot.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this AlertInfoRoot.


        :param update: The update of this AlertInfoRoot.  # noqa: E501
        :type: datetime
        """

        self._update = update

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
        if not isinstance(other, AlertInfoRoot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
