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

# from xms_client.models.product_function import ProductFunction  # noqa: F401,E501
# from xms_client.models.product_info import ProductInfo  # noqa: F401,E501
# from xms_client.models.product_limits import ProductLimits  # noqa: F401,E501
# from xms_client.models.storage_protocol import StorageProtocol  # noqa: F401,E501
# from xms_client.models.used_quota import UsedQuota  # noqa: F401,E501


class LicenseSummary(object):
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
        'capacity_base': 'int',
        'expired_features': 'list[ProductFunction]',
        'expired_protocols': 'list[StorageProtocol]',
        'features': 'list[ProductFunction]',
        'limits': 'ProductLimits',
        'product_info': 'ProductInfo',
        'protocols': 'list[StorageProtocol]',
        'used_quota': 'UsedQuota'
    }

    attribute_map = {
        'capacity_base': 'capacity_base',
        'expired_features': 'expired_features',
        'expired_protocols': 'expired_protocols',
        'features': 'features',
        'limits': 'limits',
        'product_info': 'product_info',
        'protocols': 'protocols',
        'used_quota': 'used_quota'
    }

    def __init__(self, capacity_base=None, expired_features=None, expired_protocols=None, features=None, limits=None, product_info=None, protocols=None, used_quota=None):  # noqa: E501
        """LicenseSummary - a model defined in Swagger"""  # noqa: E501

        self._capacity_base = None
        self._expired_features = None
        self._expired_protocols = None
        self._features = None
        self._limits = None
        self._product_info = None
        self._protocols = None
        self._used_quota = None
        self.discriminator = None

        self.capacity_base = capacity_base
        self.expired_features = expired_features
        self.expired_protocols = expired_protocols
        self.features = features
        self.limits = limits
        self.product_info = product_info
        self.protocols = protocols
        self.used_quota = used_quota

    @property
    def capacity_base(self):
        """Gets the capacity_base of this LicenseSummary.  # noqa: E501


        :return: The capacity_base of this LicenseSummary.  # noqa: E501
        :rtype: int
        """
        return self._capacity_base

    @capacity_base.setter
    def capacity_base(self, capacity_base):
        """Sets the capacity_base of this LicenseSummary.


        :param capacity_base: The capacity_base of this LicenseSummary.  # noqa: E501
        :type: int
        """
        if capacity_base is None:
            raise ValueError("Invalid value for `capacity_base`, must not be `None`")  # noqa: E501

        self._capacity_base = capacity_base

    @property
    def expired_features(self):
        """Gets the expired_features of this LicenseSummary.  # noqa: E501


        :return: The expired_features of this LicenseSummary.  # noqa: E501
        :rtype: list[ProductFunction]
        """
        return self._expired_features

    @expired_features.setter
    def expired_features(self, expired_features):
        """Sets the expired_features of this LicenseSummary.


        :param expired_features: The expired_features of this LicenseSummary.  # noqa: E501
        :type: list[ProductFunction]
        """
        if expired_features is None:
            raise ValueError("Invalid value for `expired_features`, must not be `None`")  # noqa: E501

        self._expired_features = expired_features

    @property
    def expired_protocols(self):
        """Gets the expired_protocols of this LicenseSummary.  # noqa: E501


        :return: The expired_protocols of this LicenseSummary.  # noqa: E501
        :rtype: list[StorageProtocol]
        """
        return self._expired_protocols

    @expired_protocols.setter
    def expired_protocols(self, expired_protocols):
        """Sets the expired_protocols of this LicenseSummary.


        :param expired_protocols: The expired_protocols of this LicenseSummary.  # noqa: E501
        :type: list[StorageProtocol]
        """
        if expired_protocols is None:
            raise ValueError("Invalid value for `expired_protocols`, must not be `None`")  # noqa: E501

        self._expired_protocols = expired_protocols

    @property
    def features(self):
        """Gets the features of this LicenseSummary.  # noqa: E501


        :return: The features of this LicenseSummary.  # noqa: E501
        :rtype: list[ProductFunction]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this LicenseSummary.


        :param features: The features of this LicenseSummary.  # noqa: E501
        :type: list[ProductFunction]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def limits(self):
        """Gets the limits of this LicenseSummary.  # noqa: E501


        :return: The limits of this LicenseSummary.  # noqa: E501
        :rtype: ProductLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this LicenseSummary.


        :param limits: The limits of this LicenseSummary.  # noqa: E501
        :type: ProductLimits
        """
        if limits is None:
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def product_info(self):
        """Gets the product_info of this LicenseSummary.  # noqa: E501


        :return: The product_info of this LicenseSummary.  # noqa: E501
        :rtype: ProductInfo
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this LicenseSummary.


        :param product_info: The product_info of this LicenseSummary.  # noqa: E501
        :type: ProductInfo
        """
        if product_info is None:
            raise ValueError("Invalid value for `product_info`, must not be `None`")  # noqa: E501

        self._product_info = product_info

    @property
    def protocols(self):
        """Gets the protocols of this LicenseSummary.  # noqa: E501


        :return: The protocols of this LicenseSummary.  # noqa: E501
        :rtype: list[StorageProtocol]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this LicenseSummary.


        :param protocols: The protocols of this LicenseSummary.  # noqa: E501
        :type: list[StorageProtocol]
        """
        if protocols is None:
            raise ValueError("Invalid value for `protocols`, must not be `None`")  # noqa: E501

        self._protocols = protocols

    @property
    def used_quota(self):
        """Gets the used_quota of this LicenseSummary.  # noqa: E501


        :return: The used_quota of this LicenseSummary.  # noqa: E501
        :rtype: UsedQuota
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        """Sets the used_quota of this LicenseSummary.


        :param used_quota: The used_quota of this LicenseSummary.  # noqa: E501
        :type: UsedQuota
        """
        if used_quota is None:
            raise ValueError("Invalid value for `used_quota`, must not be `None`")  # noqa: E501

        self._used_quota = used_quota

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
        if not isinstance(other, LicenseSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
