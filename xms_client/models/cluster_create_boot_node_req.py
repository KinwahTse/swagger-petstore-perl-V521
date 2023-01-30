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


class ClusterCreateBootNodeReq(object):
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
        'gateway_network': 'str',
        'host_id': 'int',
        'private_network': 'str',
        'public_network': 'str'
    }

    attribute_map = {
        'gateway_network': 'gateway_network',
        'host_id': 'host_id',
        'private_network': 'private_network',
        'public_network': 'public_network'
    }

    def __init__(self, gateway_network=None, host_id=None, private_network=None, public_network=None):  # noqa: E501
        """ClusterCreateBootNodeReq - a model defined in Swagger"""  # noqa: E501

        self._gateway_network = None
        self._host_id = None
        self._private_network = None
        self._public_network = None
        self.discriminator = None

        if gateway_network is not None:
            self.gateway_network = gateway_network
        self.host_id = host_id
        self.private_network = private_network
        self.public_network = public_network

    @property
    def gateway_network(self):
        """Gets the gateway_network of this ClusterCreateBootNodeReq.  # noqa: E501

        gateway network  # noqa: E501

        :return: The gateway_network of this ClusterCreateBootNodeReq.  # noqa: E501
        :rtype: str
        """
        return self._gateway_network

    @gateway_network.setter
    def gateway_network(self, gateway_network):
        """Sets the gateway_network of this ClusterCreateBootNodeReq.

        gateway network  # noqa: E501

        :param gateway_network: The gateway_network of this ClusterCreateBootNodeReq.  # noqa: E501
        :type: str
        """

        self._gateway_network = gateway_network

    @property
    def host_id(self):
        """Gets the host_id of this ClusterCreateBootNodeReq.  # noqa: E501

        boot node host id  # noqa: E501

        :return: The host_id of this ClusterCreateBootNodeReq.  # noqa: E501
        :rtype: int
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ClusterCreateBootNodeReq.

        boot node host id  # noqa: E501

        :param host_id: The host_id of this ClusterCreateBootNodeReq.  # noqa: E501
        :type: int
        """
        if host_id is None:
            raise ValueError("Invalid value for `host_id`, must not be `None`")  # noqa: E501

        self._host_id = host_id

    @property
    def private_network(self):
        """Gets the private_network of this ClusterCreateBootNodeReq.  # noqa: E501

        private network  # noqa: E501

        :return: The private_network of this ClusterCreateBootNodeReq.  # noqa: E501
        :rtype: str
        """
        return self._private_network

    @private_network.setter
    def private_network(self, private_network):
        """Sets the private_network of this ClusterCreateBootNodeReq.

        private network  # noqa: E501

        :param private_network: The private_network of this ClusterCreateBootNodeReq.  # noqa: E501
        :type: str
        """
        if private_network is None:
            raise ValueError("Invalid value for `private_network`, must not be `None`")  # noqa: E501

        self._private_network = private_network

    @property
    def public_network(self):
        """Gets the public_network of this ClusterCreateBootNodeReq.  # noqa: E501

        public network  # noqa: E501

        :return: The public_network of this ClusterCreateBootNodeReq.  # noqa: E501
        :rtype: str
        """
        return self._public_network

    @public_network.setter
    def public_network(self, public_network):
        """Sets the public_network of this ClusterCreateBootNodeReq.

        public network  # noqa: E501

        :param public_network: The public_network of this ClusterCreateBootNodeReq.  # noqa: E501
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
        if not isinstance(other, ClusterCreateBootNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
