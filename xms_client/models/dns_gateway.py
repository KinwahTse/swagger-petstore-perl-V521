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

# from xms_client.models.dns_gateway_group_nestview import DNSGatewayGroupNestview  # noqa: F401,E501
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501


class DNSGateway(object):
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
        'dns_gateway_group': 'DNSGatewayGroupNestview',
        'host': 'HostNestview',
        'id': 'int',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'action_status': 'action_status',
        'create': 'create',
        'dns_gateway_group': 'dns_gateway_group',
        'host': 'host',
        'id': 'id',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, action_status=None, create=None, dns_gateway_group=None, host=None, id=None, status=None, update=None):  # noqa: E501
        """DNSGateway - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._create = None
        self._dns_gateway_group = None
        self._host = None
        self._id = None
        self._status = None
        self._update = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if create is not None:
            self.create = create
        if dns_gateway_group is not None:
            self.dns_gateway_group = dns_gateway_group
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def action_status(self):
        """Gets the action_status of this DNSGateway.  # noqa: E501


        :return: The action_status of this DNSGateway.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this DNSGateway.


        :param action_status: The action_status of this DNSGateway.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def create(self):
        """Gets the create of this DNSGateway.  # noqa: E501


        :return: The create of this DNSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DNSGateway.


        :param create: The create of this DNSGateway.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dns_gateway_group(self):
        """Gets the dns_gateway_group of this DNSGateway.  # noqa: E501


        :return: The dns_gateway_group of this DNSGateway.  # noqa: E501
        :rtype: DNSGatewayGroupNestview
        """
        return self._dns_gateway_group

    @dns_gateway_group.setter
    def dns_gateway_group(self, dns_gateway_group):
        """Sets the dns_gateway_group of this DNSGateway.


        :param dns_gateway_group: The dns_gateway_group of this DNSGateway.  # noqa: E501
        :type: DNSGatewayGroupNestview
        """

        self._dns_gateway_group = dns_gateway_group

    @property
    def host(self):
        """Gets the host of this DNSGateway.  # noqa: E501


        :return: The host of this DNSGateway.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DNSGateway.


        :param host: The host of this DNSGateway.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this DNSGateway.  # noqa: E501


        :return: The id of this DNSGateway.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DNSGateway.


        :param id: The id of this DNSGateway.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this DNSGateway.  # noqa: E501


        :return: The status of this DNSGateway.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DNSGateway.


        :param status: The status of this DNSGateway.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this DNSGateway.  # noqa: E501


        :return: The update of this DNSGateway.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DNSGateway.


        :param update: The update of this DNSGateway.  # noqa: E501
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
        if not isinstance(other, DNSGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
