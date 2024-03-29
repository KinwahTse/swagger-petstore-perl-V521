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


class DomainUser(object):
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
        'name': 'str',
        'security': 'str',
        'update': 'datetime',
        'user_id': 'int'
    }

    attribute_map = {
        'create': 'create',
        'id': 'id',
        'name': 'name',
        'security': 'security',
        'update': 'update',
        'user_id': 'user_id'
    }

    def __init__(self, create=None, id=None, name=None, security=None, update=None, user_id=None):  # noqa: E501
        """DomainUser - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._id = None
        self._name = None
        self._security = None
        self._update = None
        self._user_id = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if security is not None:
            self.security = security
        if update is not None:
            self.update = update
        if user_id is not None:
            self.user_id = user_id

    @property
    def create(self):
        """Gets the create of this DomainUser.  # noqa: E501


        :return: The create of this DomainUser.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DomainUser.


        :param create: The create of this DomainUser.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this DomainUser.  # noqa: E501


        :return: The id of this DomainUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainUser.


        :param id: The id of this DomainUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DomainUser.  # noqa: E501


        :return: The name of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainUser.


        :param name: The name of this DomainUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def security(self):
        """Gets the security of this DomainUser.  # noqa: E501


        :return: The security of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this DomainUser.


        :param security: The security of this DomainUser.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def update(self):
        """Gets the update of this DomainUser.  # noqa: E501


        :return: The update of this DomainUser.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DomainUser.


        :param update: The update of this DomainUser.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def user_id(self):
        """Gets the user_id of this DomainUser.  # noqa: E501


        :return: The user_id of this DomainUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DomainUser.


        :param user_id: The user_id of this DomainUser.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if not isinstance(other, DomainUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
