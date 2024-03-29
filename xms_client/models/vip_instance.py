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

# from xms_client.models.network_address_nestview import NetworkAddressNestview  # noqa: F401,E501
# from xms_client.models.vip_nestview import VIPNestview  # noqa: F401,E501


class VIPInstance(object):
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
        'network_address': 'NetworkAddressNestview',
        'priority': 'int',
        'status': 'str',
        'update': 'datetime',
        'vip': 'VIPNestview'
    }

    attribute_map = {
        'action_status': 'action_status',
        'create': 'create',
        'id': 'id',
        'network_address': 'network_address',
        'priority': 'priority',
        'status': 'status',
        'update': 'update',
        'vip': 'vip'
    }

    def __init__(self, action_status=None, create=None, id=None, network_address=None, priority=None, status=None, update=None, vip=None):  # noqa: E501
        """VIPInstance - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._create = None
        self._id = None
        self._network_address = None
        self._priority = None
        self._status = None
        self._update = None
        self._vip = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if network_address is not None:
            self.network_address = network_address
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if vip is not None:
            self.vip = vip

    @property
    def action_status(self):
        """Gets the action_status of this VIPInstance.  # noqa: E501


        :return: The action_status of this VIPInstance.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this VIPInstance.


        :param action_status: The action_status of this VIPInstance.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def create(self):
        """Gets the create of this VIPInstance.  # noqa: E501


        :return: The create of this VIPInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this VIPInstance.


        :param create: The create of this VIPInstance.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this VIPInstance.  # noqa: E501


        :return: The id of this VIPInstance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VIPInstance.


        :param id: The id of this VIPInstance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def network_address(self):
        """Gets the network_address of this VIPInstance.  # noqa: E501


        :return: The network_address of this VIPInstance.  # noqa: E501
        :rtype: NetworkAddressNestview
        """
        return self._network_address

    @network_address.setter
    def network_address(self, network_address):
        """Sets the network_address of this VIPInstance.


        :param network_address: The network_address of this VIPInstance.  # noqa: E501
        :type: NetworkAddressNestview
        """

        self._network_address = network_address

    @property
    def priority(self):
        """Gets the priority of this VIPInstance.  # noqa: E501


        :return: The priority of this VIPInstance.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this VIPInstance.


        :param priority: The priority of this VIPInstance.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this VIPInstance.  # noqa: E501


        :return: The status of this VIPInstance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VIPInstance.


        :param status: The status of this VIPInstance.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this VIPInstance.  # noqa: E501


        :return: The update of this VIPInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this VIPInstance.


        :param update: The update of this VIPInstance.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def vip(self):
        """Gets the vip of this VIPInstance.  # noqa: E501


        :return: The vip of this VIPInstance.  # noqa: E501
        :rtype: VIPNestview
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this VIPInstance.


        :param vip: The vip of this VIPInstance.  # noqa: E501
        :type: VIPNestview
        """

        self._vip = vip

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
        if not isinstance(other, VIPInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
