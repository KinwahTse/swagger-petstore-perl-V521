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


class BootNodeReqBootNode(object):
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
        'admin_network': 'str',
        'gateway_network': 'str',
        'private_network': 'str',
        'public_network': 'str'
    }

    attribute_map = {
        'admin_network': 'admin_network',
        'gateway_network': 'gateway_network',
        'private_network': 'private_network',
        'public_network': 'public_network'
    }

    def __init__(self, admin_network=None, gateway_network=None, private_network=None, public_network=None):  # noqa: E501
        """BootNodeReqBootNode - a model defined in Swagger"""  # noqa: E501

        self._admin_network = None
        self._gateway_network = None
        self._private_network = None
        self._public_network = None
        self.discriminator = None

        if admin_network is not None:
            self.admin_network = admin_network
        if gateway_network is not None:
            self.gateway_network = gateway_network
        self.private_network = private_network
        self.public_network = public_network

    @property
    def admin_network(self):
        """Gets the admin_network of this BootNodeReqBootNode.  # noqa: E501

        admin network: 10.0.0.0/24  # noqa: E501

        :return: The admin_network of this BootNodeReqBootNode.  # noqa: E501
        :rtype: str
        """
        return self._admin_network

    @admin_network.setter
    def admin_network(self, admin_network):
        """Sets the admin_network of this BootNodeReqBootNode.

        admin network: 10.0.0.0/24  # noqa: E501

        :param admin_network: The admin_network of this BootNodeReqBootNode.  # noqa: E501
        :type: str
        """

        self._admin_network = admin_network

    @property
    def gateway_network(self):
        """Gets the gateway_network of this BootNodeReqBootNode.  # noqa: E501

        gateway networks, multiple networks splited by comma: 10.0.3.0/24,10.0.4.0/24  # noqa: E501

        :return: The gateway_network of this BootNodeReqBootNode.  # noqa: E501
        :rtype: str
        """
        return self._gateway_network

    @gateway_network.setter
    def gateway_network(self, gateway_network):
        """Sets the gateway_network of this BootNodeReqBootNode.

        gateway networks, multiple networks splited by comma: 10.0.3.0/24,10.0.4.0/24  # noqa: E501

        :param gateway_network: The gateway_network of this BootNodeReqBootNode.  # noqa: E501
        :type: str
        """

        self._gateway_network = gateway_network

    @property
    def private_network(self):
        """Gets the private_network of this BootNodeReqBootNode.  # noqa: E501

        private network : 10.0.2.0/24  # noqa: E501

        :return: The private_network of this BootNodeReqBootNode.  # noqa: E501
        :rtype: str
        """
        return self._private_network

    @private_network.setter
    def private_network(self, private_network):
        """Sets the private_network of this BootNodeReqBootNode.

        private network : 10.0.2.0/24  # noqa: E501

        :param private_network: The private_network of this BootNodeReqBootNode.  # noqa: E501
        :type: str
        """
        if private_network is None:
            raise ValueError("Invalid value for `private_network`, must not be `None`")  # noqa: E501

        self._private_network = private_network

    @property
    def public_network(self):
        """Gets the public_network of this BootNodeReqBootNode.  # noqa: E501

        public network: 10.0.1.0/24  # noqa: E501

        :return: The public_network of this BootNodeReqBootNode.  # noqa: E501
        :rtype: str
        """
        return self._public_network

    @public_network.setter
    def public_network(self, public_network):
        """Sets the public_network of this BootNodeReqBootNode.

        public network: 10.0.1.0/24  # noqa: E501

        :param public_network: The public_network of this BootNodeReqBootNode.  # noqa: E501
        :type: str
        """
        if public_network is None:
            raise ValueError("Invalid value for `public_network`, must not be `None`")  # noqa: E501

        self._public_network = public_network

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
        if not isinstance(other, BootNodeReqBootNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
