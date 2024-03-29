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

# from xms_client.models.event_log import EventLog  # noqa: F401,E501


class EventLogsResp(object):
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
        'event_logs': 'list[EventLog]'
    }

    attribute_map = {
        'event_logs': 'event_logs'
    }

    def __init__(self, event_logs=None):  # noqa: E501
        """EventLogsResp - a model defined in Swagger"""  # noqa: E501

        self._event_logs = None
        self.discriminator = None

        self.event_logs = event_logs

    @property
    def event_logs(self):
        """Gets the event_logs of this EventLogsResp.  # noqa: E501


        :return: The event_logs of this EventLogsResp.  # noqa: E501
        :rtype: list[EventLog]
        """
        return self._event_logs

    @event_logs.setter
    def event_logs(self, event_logs):
        """Sets the event_logs of this EventLogsResp.


        :param event_logs: The event_logs of this EventLogsResp.  # noqa: E501
        :type: list[EventLog]
        """
        if event_logs is None:
            raise ValueError("Invalid value for `event_logs`, must not be `None`")  # noqa: E501

        self._event_logs = event_logs

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
        if not isinstance(other, EventLogsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
