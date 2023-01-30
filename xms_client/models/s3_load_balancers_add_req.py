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

# from xms_client.models.s3_load_balancers_add_req_load_balancers_elt import S3LoadBalancersAddReqLoadBalancersElt  # noqa: F401,E501


class S3LoadBalancersAddReq(object):
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
        's3_load_balancers': 'list[S3LoadBalancersAddReqLoadBalancersElt]'
    }

    attribute_map = {
        's3_load_balancers': 's3_load_balancers'
    }

    def __init__(self, s3_load_balancers=None):  # noqa: E501
        """S3LoadBalancersAddReq - a model defined in Swagger"""  # noqa: E501

        self._s3_load_balancers = None
        self.discriminator = None

        self.s3_load_balancers = s3_load_balancers

    @property
    def s3_load_balancers(self):
        """Gets the s3_load_balancers of this S3LoadBalancersAddReq.  # noqa: E501


        :return: The s3_load_balancers of this S3LoadBalancersAddReq.  # noqa: E501
        :rtype: list[S3LoadBalancersAddReqLoadBalancersElt]
        """
        return self._s3_load_balancers

    @s3_load_balancers.setter
    def s3_load_balancers(self, s3_load_balancers):
        """Sets the s3_load_balancers of this S3LoadBalancersAddReq.


        :param s3_load_balancers: The s3_load_balancers of this S3LoadBalancersAddReq.  # noqa: E501
        :type: list[S3LoadBalancersAddReqLoadBalancersElt]
        """
        if s3_load_balancers is None:
            raise ValueError("Invalid value for `s3_load_balancers`, must not be `None`")  # noqa: E501

        self._s3_load_balancers = s3_load_balancers

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
        if not isinstance(other, S3LoadBalancersAddReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other