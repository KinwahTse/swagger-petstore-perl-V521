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

# from xms_client.models.dfs_policy import DfsPolicy  # noqa: F401,E501


class DfsPoliciesResp(object):
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
        'dfs_policies': 'list[DfsPolicy]'
    }

    attribute_map = {
        'dfs_policies': 'dfs_policies'
    }

    def __init__(self, dfs_policies=None):  # noqa: E501
        """DfsPoliciesResp - a model defined in Swagger"""  # noqa: E501

        self._dfs_policies = None
        self.discriminator = None

        self.dfs_policies = dfs_policies

    @property
    def dfs_policies(self):
        """Gets the dfs_policies of this DfsPoliciesResp.  # noqa: E501

        dfs Policies  # noqa: E501

        :return: The dfs_policies of this DfsPoliciesResp.  # noqa: E501
        :rtype: list[DfsPolicy]
        """
        return self._dfs_policies

    @dfs_policies.setter
    def dfs_policies(self, dfs_policies):
        """Sets the dfs_policies of this DfsPoliciesResp.

        dfs Policies  # noqa: E501

        :param dfs_policies: The dfs_policies of this DfsPoliciesResp.  # noqa: E501
        :type: list[DfsPolicy]
        """
        if dfs_policies is None:
            raise ValueError("Invalid value for `dfs_policies`, must not be `None`")  # noqa: E501

        self._dfs_policies = dfs_policies

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
        if not isinstance(other, DfsPoliciesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
