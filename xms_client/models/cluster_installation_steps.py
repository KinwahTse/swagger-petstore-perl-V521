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


class ClusterInstallationSteps(object):
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
        'bootnode': 'bool',
        'license': 'bool',
        'user': 'bool'
    }

    attribute_map = {
        'bootnode': 'bootnode',
        'license': 'license',
        'user': 'user'
    }

    def __init__(self, bootnode=None, license=None, user=None):  # noqa: E501
        """ClusterInstallationSteps - a model defined in Swagger"""  # noqa: E501

        self._bootnode = None
        self._license = None
        self._user = None
        self.discriminator = None

        if bootnode is not None:
            self.bootnode = bootnode
        if license is not None:
            self.license = license
        if user is not None:
            self.user = user

    @property
    def bootnode(self):
        """Gets the bootnode of this ClusterInstallationSteps.  # noqa: E501

        step of setting boot node  # noqa: E501

        :return: The bootnode of this ClusterInstallationSteps.  # noqa: E501
        :rtype: bool
        """
        return self._bootnode

    @bootnode.setter
    def bootnode(self, bootnode):
        """Sets the bootnode of this ClusterInstallationSteps.

        step of setting boot node  # noqa: E501

        :param bootnode: The bootnode of this ClusterInstallationSteps.  # noqa: E501
        :type: bool
        """

        self._bootnode = bootnode

    @property
    def license(self):
        """Gets the license of this ClusterInstallationSteps.  # noqa: E501

        step of registering license  # noqa: E501

        :return: The license of this ClusterInstallationSteps.  # noqa: E501
        :rtype: bool
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ClusterInstallationSteps.

        step of registering license  # noqa: E501

        :param license: The license of this ClusterInstallationSteps.  # noqa: E501
        :type: bool
        """

        self._license = license

    @property
    def user(self):
        """Gets the user of this ClusterInstallationSteps.  # noqa: E501

        step of creating user  # noqa: E501

        :return: The user of this ClusterInstallationSteps.  # noqa: E501
        :rtype: bool
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ClusterInstallationSteps.

        step of creating user  # noqa: E501

        :param user: The user of this ClusterInstallationSteps.  # noqa: E501
        :type: bool
        """

        self._user = user

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
        if not isinstance(other, ClusterInstallationSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
