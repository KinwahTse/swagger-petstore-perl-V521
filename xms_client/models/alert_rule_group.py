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


class AlertRuleGroup(object):
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
        'auto_resolve': 'bool',
        'create': 'datetime',
        'enabled': 'bool',
        'id': 'int',
        'levels': 'list[str]',
        'name': 'str',
        'resource_type': 'str',
        'trigger_time_seconds': 'int',
        'update': 'datetime'
    }

    attribute_map = {
        'auto_resolve': 'auto_resolve',
        'create': 'create',
        'enabled': 'enabled',
        'id': 'id',
        'levels': 'levels',
        'name': 'name',
        'resource_type': 'resource_type',
        'trigger_time_seconds': 'trigger_time_seconds',
        'update': 'update'
    }

    def __init__(self, auto_resolve=None, create=None, enabled=None, id=None, levels=None, name=None, resource_type=None, trigger_time_seconds=None, update=None):  # noqa: E501
        """AlertRuleGroup - a model defined in Swagger"""  # noqa: E501

        self._auto_resolve = None
        self._create = None
        self._enabled = None
        self._id = None
        self._levels = None
        self._name = None
        self._resource_type = None
        self._trigger_time_seconds = None
        self._update = None
        self.discriminator = None

        if auto_resolve is not None:
            self.auto_resolve = auto_resolve
        if create is not None:
            self.create = create
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if levels is not None:
            self.levels = levels
        if name is not None:
            self.name = name
        if resource_type is not None:
            self.resource_type = resource_type
        if trigger_time_seconds is not None:
            self.trigger_time_seconds = trigger_time_seconds
        if update is not None:
            self.update = update

    @property
    def auto_resolve(self):
        """Gets the auto_resolve of this AlertRuleGroup.  # noqa: E501


        :return: The auto_resolve of this AlertRuleGroup.  # noqa: E501
        :rtype: bool
        """
        return self._auto_resolve

    @auto_resolve.setter
    def auto_resolve(self, auto_resolve):
        """Sets the auto_resolve of this AlertRuleGroup.


        :param auto_resolve: The auto_resolve of this AlertRuleGroup.  # noqa: E501
        :type: bool
        """

        self._auto_resolve = auto_resolve

    @property
    def create(self):
        """Gets the create of this AlertRuleGroup.  # noqa: E501


        :return: The create of this AlertRuleGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this AlertRuleGroup.


        :param create: The create of this AlertRuleGroup.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def enabled(self):
        """Gets the enabled of this AlertRuleGroup.  # noqa: E501


        :return: The enabled of this AlertRuleGroup.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AlertRuleGroup.


        :param enabled: The enabled of this AlertRuleGroup.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AlertRuleGroup.  # noqa: E501


        :return: The id of this AlertRuleGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRuleGroup.


        :param id: The id of this AlertRuleGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def levels(self):
        """Gets the levels of this AlertRuleGroup.  # noqa: E501


        :return: The levels of this AlertRuleGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this AlertRuleGroup.


        :param levels: The levels of this AlertRuleGroup.  # noqa: E501
        :type: list[str]
        """

        self._levels = levels

    @property
    def name(self):
        """Gets the name of this AlertRuleGroup.  # noqa: E501


        :return: The name of this AlertRuleGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertRuleGroup.


        :param name: The name of this AlertRuleGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_type(self):
        """Gets the resource_type of this AlertRuleGroup.  # noqa: E501


        :return: The resource_type of this AlertRuleGroup.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AlertRuleGroup.


        :param resource_type: The resource_type of this AlertRuleGroup.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def trigger_time_seconds(self):
        """Gets the trigger_time_seconds of this AlertRuleGroup.  # noqa: E501


        :return: The trigger_time_seconds of this AlertRuleGroup.  # noqa: E501
        :rtype: int
        """
        return self._trigger_time_seconds

    @trigger_time_seconds.setter
    def trigger_time_seconds(self, trigger_time_seconds):
        """Sets the trigger_time_seconds of this AlertRuleGroup.


        :param trigger_time_seconds: The trigger_time_seconds of this AlertRuleGroup.  # noqa: E501
        :type: int
        """

        self._trigger_time_seconds = trigger_time_seconds

    @property
    def update(self):
        """Gets the update of this AlertRuleGroup.  # noqa: E501


        :return: The update of this AlertRuleGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this AlertRuleGroup.


        :param update: The update of this AlertRuleGroup.  # noqa: E501
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
        if not isinstance(other, AlertRuleGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other