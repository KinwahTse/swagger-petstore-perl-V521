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


class DpBlockSnapshotPolicyUpdateReqPolicy(object):
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
        'cron_expr': 'str',
        'name': 'str',
        'retained_max': 'int'
    }

    attribute_map = {
        'cron_expr': 'cron_expr',
        'name': 'name',
        'retained_max': 'retained_max'
    }

    def __init__(self, cron_expr=None, name=None, retained_max=None):  # noqa: E501
        """DpBlockSnapshotPolicyUpdateReqPolicy - a model defined in Swagger"""  # noqa: E501

        self._cron_expr = None
        self._name = None
        self._retained_max = None
        self.discriminator = None

        if cron_expr is not None:
            self.cron_expr = cron_expr
        if name is not None:
            self.name = name
        if retained_max is not None:
            self.retained_max = retained_max

    @property
    def cron_expr(self):
        """Gets the cron_expr of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501

        cron expression  # noqa: E501

        :return: The cron_expr of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :rtype: str
        """
        return self._cron_expr

    @cron_expr.setter
    def cron_expr(self, cron_expr):
        """Sets the cron_expr of this DpBlockSnapshotPolicyUpdateReqPolicy.

        cron expression  # noqa: E501

        :param cron_expr: The cron_expr of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :type: str
        """

        self._cron_expr = cron_expr

    @property
    def name(self):
        """Gets the name of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501

        name  # noqa: E501

        :return: The name of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DpBlockSnapshotPolicyUpdateReqPolicy.

        name  # noqa: E501

        :param name: The name of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def retained_max(self):
        """Gets the retained_max of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501

        retained max number of snapshots  # noqa: E501

        :return: The retained_max of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :rtype: int
        """
        return self._retained_max

    @retained_max.setter
    def retained_max(self, retained_max):
        """Sets the retained_max of this DpBlockSnapshotPolicyUpdateReqPolicy.

        retained max number of snapshots  # noqa: E501

        :param retained_max: The retained_max of this DpBlockSnapshotPolicyUpdateReqPolicy.  # noqa: E501
        :type: int
        """

        self._retained_max = retained_max

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
        if not isinstance(other, DpBlockSnapshotPolicyUpdateReqPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other