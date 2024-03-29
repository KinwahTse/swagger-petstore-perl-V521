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

# from xms_client.models.pool_rule_req import PoolRuleReq  # noqa: F401,E501


class EmptyPoolInitializeReqPoolCache(object):
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
        'osd_ids': 'list[int]',
        'primary_placement_node_id': 'int',
        'ruleset': 'list[PoolRuleReq]'
    }

    attribute_map = {
        'osd_ids': 'osd_ids',
        'primary_placement_node_id': 'primary_placement_node_id',
        'ruleset': 'ruleset'
    }

    def __init__(self, osd_ids=None, primary_placement_node_id=None, ruleset=None):  # noqa: E501
        """EmptyPoolInitializeReqPoolCache - a model defined in Swagger"""  # noqa: E501

        self._osd_ids = None
        self._primary_placement_node_id = None
        self._ruleset = None
        self.discriminator = None

        if osd_ids is not None:
            self.osd_ids = osd_ids
        if primary_placement_node_id is not None:
            self.primary_placement_node_id = primary_placement_node_id
        if ruleset is not None:
            self.ruleset = ruleset

    @property
    def osd_ids(self):
        """Gets the osd_ids of this EmptyPoolInitializeReqPoolCache.  # noqa: E501


        :return: The osd_ids of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :rtype: list[int]
        """
        return self._osd_ids

    @osd_ids.setter
    def osd_ids(self, osd_ids):
        """Sets the osd_ids of this EmptyPoolInitializeReqPoolCache.


        :param osd_ids: The osd_ids of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :type: list[int]
        """

        self._osd_ids = osd_ids

    @property
    def primary_placement_node_id(self):
        """Gets the primary_placement_node_id of this EmptyPoolInitializeReqPoolCache.  # noqa: E501


        :return: The primary_placement_node_id of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :rtype: int
        """
        return self._primary_placement_node_id

    @primary_placement_node_id.setter
    def primary_placement_node_id(self, primary_placement_node_id):
        """Sets the primary_placement_node_id of this EmptyPoolInitializeReqPoolCache.


        :param primary_placement_node_id: The primary_placement_node_id of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :type: int
        """

        self._primary_placement_node_id = primary_placement_node_id

    @property
    def ruleset(self):
        """Gets the ruleset of this EmptyPoolInitializeReqPoolCache.  # noqa: E501


        :return: The ruleset of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :rtype: list[PoolRuleReq]
        """
        return self._ruleset

    @ruleset.setter
    def ruleset(self, ruleset):
        """Sets the ruleset of this EmptyPoolInitializeReqPoolCache.


        :param ruleset: The ruleset of this EmptyPoolInitializeReqPoolCache.  # noqa: E501
        :type: list[PoolRuleReq]
        """

        self._ruleset = ruleset

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
        if not isinstance(other, EmptyPoolInitializeReqPoolCache):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
