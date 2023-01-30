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

# from xms_client.models.alert_rule import AlertRule  # noqa: F401,E501


class AlertRulesResp(object):
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
        'alert_rules': 'list[AlertRule]'
    }

    attribute_map = {
        'alert_rules': 'alert_rules'
    }

    def __init__(self, alert_rules=None):  # noqa: E501
        """AlertRulesResp - a model defined in Swagger"""  # noqa: E501

        self._alert_rules = None
        self.discriminator = None

        self.alert_rules = alert_rules

    @property
    def alert_rules(self):
        """Gets the alert_rules of this AlertRulesResp.  # noqa: E501

        alert rules  # noqa: E501

        :return: The alert_rules of this AlertRulesResp.  # noqa: E501
        :rtype: list[AlertRule]
        """
        return self._alert_rules

    @alert_rules.setter
    def alert_rules(self, alert_rules):
        """Sets the alert_rules of this AlertRulesResp.

        alert rules  # noqa: E501

        :param alert_rules: The alert_rules of this AlertRulesResp.  # noqa: E501
        :type: list[AlertRule]
        """
        if alert_rules is None:
            raise ValueError("Invalid value for `alert_rules`, must not be `None`")  # noqa: E501

        self._alert_rules = alert_rules

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
        if not isinstance(other, AlertRulesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
