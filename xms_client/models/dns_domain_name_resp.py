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

# from xms_client.models.dns_domain_name import DNSDomainName  # noqa: F401,E501


class DNSDomainNameResp(object):
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
        'dns_domain_name': 'DNSDomainName'
    }

    attribute_map = {
        'dns_domain_name': 'dns_domain_name'
    }

    def __init__(self, dns_domain_name=None):  # noqa: E501
        """DNSDomainNameResp - a model defined in Swagger"""  # noqa: E501

        self._dns_domain_name = None
        self.discriminator = None

        if dns_domain_name is not None:
            self.dns_domain_name = dns_domain_name

    @property
    def dns_domain_name(self):
        """Gets the dns_domain_name of this DNSDomainNameResp.  # noqa: E501

        dns domain name  # noqa: E501

        :return: The dns_domain_name of this DNSDomainNameResp.  # noqa: E501
        :rtype: DNSDomainName
        """
        return self._dns_domain_name

    @dns_domain_name.setter
    def dns_domain_name(self, dns_domain_name):
        """Sets the dns_domain_name of this DNSDomainNameResp.

        dns domain name  # noqa: E501

        :param dns_domain_name: The dns_domain_name of this DNSDomainNameResp.  # noqa: E501
        :type: DNSDomainName
        """

        self._dns_domain_name = dns_domain_name

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
        if not isinstance(other, DNSDomainNameResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
