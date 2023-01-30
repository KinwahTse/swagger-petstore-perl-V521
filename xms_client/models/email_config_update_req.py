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

# from xms_client.models.email_config_update_req_email_config import EmailConfigUpdateReqEmailConfig  # noqa: F401,E501


class EmailConfigUpdateReq(object):
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
        'email_config': 'EmailConfigUpdateReqEmailConfig'
    }

    attribute_map = {
        'email_config': 'email_config'
    }

    def __init__(self, email_config=None):  # noqa: E501
        """EmailConfigUpdateReq - a model defined in Swagger"""  # noqa: E501

        self._email_config = None
        self.discriminator = None

        if email_config is not None:
            self.email_config = email_config

    @property
    def email_config(self):
        """Gets the email_config of this EmailConfigUpdateReq.  # noqa: E501


        :return: The email_config of this EmailConfigUpdateReq.  # noqa: E501
        :rtype: EmailConfigUpdateReqEmailConfig
        """
        return self._email_config

    @email_config.setter
    def email_config(self, email_config):
        """Sets the email_config of this EmailConfigUpdateReq.


        :param email_config: The email_config of this EmailConfigUpdateReq.  # noqa: E501
        :type: EmailConfigUpdateReqEmailConfig
        """

        self._email_config = email_config

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
        if not isinstance(other, EmailConfigUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
