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


class AlertRuleUpdateReqRule(object):
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
        'enabled': 'bool',
        'trigger_period': 'int',
        'trigger_value': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'trigger_period': 'trigger_period',
        'trigger_value': 'trigger_value'
    }

    def __init__(self, enabled=None, trigger_period=None, trigger_value=None):  # noqa: E501
        """AlertRuleUpdateReqRule - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._trigger_period = None
        self._trigger_value = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if trigger_period is not None:
            self.trigger_period = trigger_period
        if trigger_value is not None:
            self.trigger_value = trigger_value

    @property
    def enabled(self):
        """Gets the enabled of this AlertRuleUpdateReqRule.  # noqa: E501

        enable the alert rule or not  # noqa: E501

        :return: The enabled of this AlertRuleUpdateReqRule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AlertRuleUpdateReqRule.

        enable the alert rule or not  # noqa: E501

        :param enabled: The enabled of this AlertRuleUpdateReqRule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def trigger_period(self):
        """Gets the trigger_period of this AlertRuleUpdateReqRule.  # noqa: E501

        trigger period of alert rule  # noqa: E501

        :return: The trigger_period of this AlertRuleUpdateReqRule.  # noqa: E501
        :rtype: int
        """
        return self._trigger_period

    @trigger_period.setter
    def trigger_period(self, trigger_period):
        """Sets the trigger_period of this AlertRuleUpdateReqRule.

        trigger period of alert rule  # noqa: E501

        :param trigger_period: The trigger_period of this AlertRuleUpdateReqRule.  # noqa: E501
        :type: int
        """

        self._trigger_period = trigger_period

    @property
    def trigger_value(self):
        """Gets the trigger_value of this AlertRuleUpdateReqRule.  # noqa: E501

        trigger value of alert rule  # noqa: E501

        :return: The trigger_value of this AlertRuleUpdateReqRule.  # noqa: E501
        :rtype: str
        """
        return self._trigger_value

    @trigger_value.setter
    def trigger_value(self, trigger_value):
        """Sets the trigger_value of this AlertRuleUpdateReqRule.

        trigger value of alert rule  # noqa: E501

        :param trigger_value: The trigger_value of this AlertRuleUpdateReqRule.  # noqa: E501
        :type: str
        """

        self._trigger_value = trigger_value

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
        if not isinstance(other, AlertRuleUpdateReqRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
