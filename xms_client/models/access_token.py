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

# from xms_client.models.user_nestview import UserNestview  # noqa: F401,E501


class AccessToken(object):
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
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'roles': 'list[str]',
        'update': 'datetime',
        'used': 'bool',
        'user': 'UserNestview'
    }

    attribute_map = {
        'create': 'create',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'roles': 'roles',
        'update': 'update',
        'used': 'used',
        'user': 'user'
    }

    def __init__(self, create=None, description=None, id=None, name=None, roles=None, update=None, used=None, user=None):  # noqa: E501
        """AccessToken - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._description = None
        self._id = None
        self._name = None
        self._roles = None
        self._update = None
        self._used = None
        self._user = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if roles is not None:
            self.roles = roles
        if update is not None:
            self.update = update
        if used is not None:
            self.used = used
        if user is not None:
            self.user = user

    @property
    def create(self):
        """Gets the create of this AccessToken.  # noqa: E501


        :return: The create of this AccessToken.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this AccessToken.


        :param create: The create of this AccessToken.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this AccessToken.  # noqa: E501


        :return: The description of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessToken.


        :param description: The description of this AccessToken.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AccessToken.  # noqa: E501


        :return: The id of this AccessToken.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessToken.


        :param id: The id of this AccessToken.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AccessToken.  # noqa: E501


        :return: The name of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessToken.


        :param name: The name of this AccessToken.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def roles(self):
        """Gets the roles of this AccessToken.  # noqa: E501


        :return: The roles of this AccessToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessToken.


        :param roles: The roles of this AccessToken.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def update(self):
        """Gets the update of this AccessToken.  # noqa: E501


        :return: The update of this AccessToken.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this AccessToken.


        :param update: The update of this AccessToken.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def used(self):
        """Gets the used of this AccessToken.  # noqa: E501


        :return: The used of this AccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this AccessToken.


        :param used: The used of this AccessToken.  # noqa: E501
        :type: bool
        """

        self._used = used

    @property
    def user(self):
        """Gets the user of this AccessToken.  # noqa: E501


        :return: The user of this AccessToken.  # noqa: E501
        :rtype: UserNestview
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessToken.


        :param user: The user of this AccessToken.  # noqa: E501
        :type: UserNestview
        """

        self._user = user

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
        if not isinstance(other, AccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
