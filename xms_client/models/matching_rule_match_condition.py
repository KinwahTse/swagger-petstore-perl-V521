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

# from xms_client.models.condition import Condition  # noqa: F401,E501


class MatchingRuleMatchCondition(object):
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
        'cond_operator': 'str',
        'conditions': 'list[Condition]'
    }

    attribute_map = {
        'cond_operator': 'cond_operator',
        'conditions': 'conditions'
    }

    def __init__(self, cond_operator=None, conditions=None):  # noqa: E501
        """MatchingRuleMatchCondition - a model defined in Swagger"""  # noqa: E501

        self._cond_operator = None
        self._conditions = None
        self.discriminator = None

        if cond_operator is not None:
            self.cond_operator = cond_operator
        if conditions is not None:
            self.conditions = conditions

    @property
    def cond_operator(self):
        """Gets the cond_operator of this MatchingRuleMatchCondition.  # noqa: E501


        :return: The cond_operator of this MatchingRuleMatchCondition.  # noqa: E501
        :rtype: str
        """
        return self._cond_operator

    @cond_operator.setter
    def cond_operator(self, cond_operator):
        """Sets the cond_operator of this MatchingRuleMatchCondition.


        :param cond_operator: The cond_operator of this MatchingRuleMatchCondition.  # noqa: E501
        :type: str
        """

        self._cond_operator = cond_operator

    @property
    def conditions(self):
        """Gets the conditions of this MatchingRuleMatchCondition.  # noqa: E501


        :return: The conditions of this MatchingRuleMatchCondition.  # noqa: E501
        :rtype: list[Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this MatchingRuleMatchCondition.


        :param conditions: The conditions of this MatchingRuleMatchCondition.  # noqa: E501
        :type: list[Condition]
        """

        self._conditions = conditions

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
        if not isinstance(other, MatchingRuleMatchCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
