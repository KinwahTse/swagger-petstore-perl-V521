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

# from xms_client.models.placement_node_record import PlacementNodeRecord  # noqa: F401,E501


class PlacementNodesResp(object):
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
        'placement_nodes': 'list[PlacementNodeRecord]'
    }

    attribute_map = {
        'placement_nodes': 'placement_nodes'
    }

    def __init__(self, placement_nodes=None):  # noqa: E501
        """PlacementNodesResp - a model defined in Swagger"""  # noqa: E501

        self._placement_nodes = None
        self.discriminator = None

        self.placement_nodes = placement_nodes

    @property
    def placement_nodes(self):
        """Gets the placement_nodes of this PlacementNodesResp.  # noqa: E501

        placement nodes  # noqa: E501

        :return: The placement_nodes of this PlacementNodesResp.  # noqa: E501
        :rtype: list[PlacementNodeRecord]
        """
        return self._placement_nodes

    @placement_nodes.setter
    def placement_nodes(self, placement_nodes):
        """Sets the placement_nodes of this PlacementNodesResp.

        placement nodes  # noqa: E501

        :param placement_nodes: The placement_nodes of this PlacementNodesResp.  # noqa: E501
        :type: list[PlacementNodeRecord]
        """
        if placement_nodes is None:
            raise ValueError("Invalid value for `placement_nodes`, must not be `None`")  # noqa: E501

        self._placement_nodes = placement_nodes

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
        if not isinstance(other, PlacementNodesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
