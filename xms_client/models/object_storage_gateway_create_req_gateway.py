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


class ObjectStorageGatewayCreateReqGateway(object):
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
        'description': 'str',
        'gateway_ip': 'str',
        'host_id': 'int',
        'name': 'str',
        'port': 'int',
        'role': 'str'
    }

    attribute_map = {
        'description': 'description',
        'gateway_ip': 'gateway_ip',
        'host_id': 'host_id',
        'name': 'name',
        'port': 'port',
        'role': 'role'
    }

    def __init__(self, description=None, gateway_ip=None, host_id=None, name=None, port=None, role=None):  # noqa: E501
        """ObjectStorageGatewayCreateReqGateway - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._gateway_ip = None
        self._host_id = None
        self._name = None
        self._port = None
        self._role = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        self.host_id = host_id
        self.name = name
        self.port = port
        if role is not None:
            self.role = role

    @property
    def description(self):
        """Gets the description of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The description of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ObjectStorageGatewayCreateReqGateway.


        :param description: The description of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The gateway_ip of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this ObjectStorageGatewayCreateReqGateway.


        :param gateway_ip: The gateway_ip of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

    @property
    def host_id(self):
        """Gets the host_id of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The host_id of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: int
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ObjectStorageGatewayCreateReqGateway.


        :param host_id: The host_id of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: int
        """
        if host_id is None:
            raise ValueError("Invalid value for `host_id`, must not be `None`")  # noqa: E501

        self._host_id = host_id

    @property
    def name(self):
        """Gets the name of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The name of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectStorageGatewayCreateReqGateway.


        :param name: The name of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The port of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ObjectStorageGatewayCreateReqGateway.


        :param port: The port of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def role(self):
        """Gets the role of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501


        :return: The role of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ObjectStorageGatewayCreateReqGateway.


        :param role: The role of this ObjectStorageGatewayCreateReqGateway.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if not isinstance(other, ObjectStorageGatewayCreateReqGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
