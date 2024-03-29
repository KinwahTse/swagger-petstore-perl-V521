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


class FSFolderAddQuotaTreesReqFolderQuotaTreesElt(object):
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
        'name': 'str',
        'size': 'int',
        'soft_quota_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'soft_quota_size': 'soft_quota_size'
    }

    def __init__(self, name=None, size=None, soft_quota_size=None):  # noqa: E501
        """FSFolderAddQuotaTreesReqFolderQuotaTreesElt - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._size = None
        self._soft_quota_size = None
        self.discriminator = None

        self.name = name
        if size is not None:
            self.size = size
        if soft_quota_size is not None:
            self.soft_quota_size = soft_quota_size

    @property
    def name(self):
        """Gets the name of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501

        name of quota tree  # noqa: E501

        :return: The name of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.

        name of quota tree  # noqa: E501

        :param name: The name of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501

        size of quota tree  # noqa: E501

        :return: The size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.

        size of quota tree  # noqa: E501

        :param size: The size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def soft_quota_size(self):
        """Gets the soft_quota_size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501

        soft quota size of quota tree  # noqa: E501

        :return: The soft_quota_size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :rtype: int
        """
        return self._soft_quota_size

    @soft_quota_size.setter
    def soft_quota_size(self, soft_quota_size):
        """Sets the soft_quota_size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.

        soft quota size of quota tree  # noqa: E501

        :param soft_quota_size: The soft_quota_size of this FSFolderAddQuotaTreesReqFolderQuotaTreesElt.  # noqa: E501
        :type: int
        """

        self._soft_quota_size = soft_quota_size

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
        if not isinstance(other, FSFolderAddQuotaTreesReqFolderQuotaTreesElt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
