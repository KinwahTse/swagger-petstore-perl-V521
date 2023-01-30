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

# from xms_client.models.dfs_gateway_record import DfsGatewayRecord  # noqa: F401,E501


class DfsGatewayResp(object):
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
        'dfs_gateway': 'DfsGatewayRecord'
    }

    attribute_map = {
        'dfs_gateway': 'dfs_gateway'
    }

    def __init__(self, dfs_gateway=None):  # noqa: E501
        """DfsGatewayResp - a model defined in Swagger"""  # noqa: E501

        self._dfs_gateway = None
        self.discriminator = None

        self.dfs_gateway = dfs_gateway

    @property
    def dfs_gateway(self):
        """Gets the dfs_gateway of this DfsGatewayResp.  # noqa: E501

        dfs gateway  # noqa: E501

        :return: The dfs_gateway of this DfsGatewayResp.  # noqa: E501
        :rtype: DfsGatewayRecord
        """
        return self._dfs_gateway

    @dfs_gateway.setter
    def dfs_gateway(self, dfs_gateway):
        """Sets the dfs_gateway of this DfsGatewayResp.

        dfs gateway  # noqa: E501

        :param dfs_gateway: The dfs_gateway of this DfsGatewayResp.  # noqa: E501
        :type: DfsGatewayRecord
        """
        if dfs_gateway is None:
            raise ValueError("Invalid value for `dfs_gateway`, must not be `None`")  # noqa: E501

        self._dfs_gateway = dfs_gateway

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
        if not isinstance(other, DfsGatewayResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
