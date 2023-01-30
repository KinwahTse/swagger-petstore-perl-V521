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


class VIPGroup(object):
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
        'action_status': 'str',
        'create': 'datetime',
        'id': 'int',
        'name': 'str',
        'network': 'str',
        'preempt': 'bool',
        'resource_id': 'int',
        'resource_type': 'str',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'action_status': 'action_status',
        'create': 'create',
        'id': 'id',
        'name': 'name',
        'network': 'network',
        'preempt': 'preempt',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, action_status=None, create=None, id=None, name=None, network=None, preempt=None, resource_id=None, resource_type=None, status=None, update=None):  # noqa: E501
        """VIPGroup - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._create = None
        self._id = None
        self._name = None
        self._network = None
        self._preempt = None
        self._resource_id = None
        self._resource_type = None
        self._status = None
        self._update = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network is not None:
            self.network = network
        if preempt is not None:
            self.preempt = preempt
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def action_status(self):
        """Gets the action_status of this VIPGroup.  # noqa: E501


        :return: The action_status of this VIPGroup.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this VIPGroup.


        :param action_status: The action_status of this VIPGroup.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def create(self):
        """Gets the create of this VIPGroup.  # noqa: E501


        :return: The create of this VIPGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this VIPGroup.


        :param create: The create of this VIPGroup.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this VIPGroup.  # noqa: E501


        :return: The id of this VIPGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VIPGroup.


        :param id: The id of this VIPGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VIPGroup.  # noqa: E501


        :return: The name of this VIPGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VIPGroup.


        :param name: The name of this VIPGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network(self):
        """Gets the network of this VIPGroup.  # noqa: E501


        :return: The network of this VIPGroup.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this VIPGroup.


        :param network: The network of this VIPGroup.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def preempt(self):
        """Gets the preempt of this VIPGroup.  # noqa: E501


        :return: The preempt of this VIPGroup.  # noqa: E501
        :rtype: bool
        """
        return self._preempt

    @preempt.setter
    def preempt(self, preempt):
        """Sets the preempt of this VIPGroup.


        :param preempt: The preempt of this VIPGroup.  # noqa: E501
        :type: bool
        """

        self._preempt = preempt

    @property
    def resource_id(self):
        """Gets the resource_id of this VIPGroup.  # noqa: E501


        :return: The resource_id of this VIPGroup.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this VIPGroup.


        :param resource_id: The resource_id of this VIPGroup.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this VIPGroup.  # noqa: E501


        :return: The resource_type of this VIPGroup.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this VIPGroup.


        :param resource_type: The resource_type of this VIPGroup.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this VIPGroup.  # noqa: E501


        :return: The status of this VIPGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VIPGroup.


        :param status: The status of this VIPGroup.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this VIPGroup.  # noqa: E501


        :return: The update of this VIPGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this VIPGroup.


        :param update: The update of this VIPGroup.  # noqa: E501
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
        if not isinstance(other, VIPGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other