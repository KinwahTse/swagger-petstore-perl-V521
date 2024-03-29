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

# from xms_client.models.alert_rule_update_req import AlertRuleUpdateReq  # noqa: F401,E501
# from xms_client.models.alert_rule_update_req_rule import AlertRuleUpdateReqRule  # noqa: F401,E501


class AlertRuleGroupDetailUpdateReqRulesElt(object):
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
        'alert_rule': 'AlertRuleUpdateReqRule',
        'id': 'int'
    }

    attribute_map = {
        'alert_rule': 'alert_rule',
        'id': 'id'
    }

    def __init__(self, alert_rule=None, id=None):  # noqa: E501
        """AlertRuleGroupDetailUpdateReqRulesElt - a model defined in Swagger"""  # noqa: E501

        self._alert_rule = None
        self._id = None
        self.discriminator = None

        self.alert_rule = alert_rule
        if id is not None:
            self.id = id

    @property
    def alert_rule(self):
        """Gets the alert_rule of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501


        :return: The alert_rule of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501
        :rtype: AlertRuleUpdateReqRule
        """
        return self._alert_rule

    @alert_rule.setter
    def alert_rule(self, alert_rule):
        """Sets the alert_rule of this AlertRuleGroupDetailUpdateReqRulesElt.


        :param alert_rule: The alert_rule of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501
        :type: AlertRuleUpdateReqRule
        """
        if alert_rule is None:
            raise ValueError("Invalid value for `alert_rule`, must not be `None`")  # noqa: E501

        self._alert_rule = alert_rule

    @property
    def id(self):
        """Gets the id of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501


        :return: The id of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRuleGroupDetailUpdateReqRulesElt.


        :param id: The id of this AlertRuleGroupDetailUpdateReqRulesElt.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, AlertRuleGroupDetailUpdateReqRulesElt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
