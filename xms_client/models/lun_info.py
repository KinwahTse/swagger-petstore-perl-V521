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


class LunInfo(object):
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
        'alua_value': 'int',
        'dc_name': 'str',
        'lun_cfg': 'str',
        'lun_id': 'int',
        'lun_name': 'str',
        'lun_size': 'int',
        'lun_sn': 'str'
    }

    attribute_map = {
        'alua_value': 'alua_value',
        'dc_name': 'dc_name',
        'lun_cfg': 'lun_cfg',
        'lun_id': 'lun_id',
        'lun_name': 'lun_name',
        'lun_size': 'lun_size',
        'lun_sn': 'lun_sn'
    }

    def __init__(self, alua_value=None, dc_name=None, lun_cfg=None, lun_id=None, lun_name=None, lun_size=None, lun_sn=None):  # noqa: E501
        """LunInfo - a model defined in Swagger"""  # noqa: E501

        self._alua_value = None
        self._dc_name = None
        self._lun_cfg = None
        self._lun_id = None
        self._lun_name = None
        self._lun_size = None
        self._lun_sn = None
        self.discriminator = None

        if alua_value is not None:
            self.alua_value = alua_value
        if dc_name is not None:
            self.dc_name = dc_name
        if lun_cfg is not None:
            self.lun_cfg = lun_cfg
        if lun_id is not None:
            self.lun_id = lun_id
        if lun_name is not None:
            self.lun_name = lun_name
        if lun_size is not None:
            self.lun_size = lun_size
        if lun_sn is not None:
            self.lun_sn = lun_sn

    @property
    def alua_value(self):
        """Gets the alua_value of this LunInfo.  # noqa: E501


        :return: The alua_value of this LunInfo.  # noqa: E501
        :rtype: int
        """
        return self._alua_value

    @alua_value.setter
    def alua_value(self, alua_value):
        """Sets the alua_value of this LunInfo.


        :param alua_value: The alua_value of this LunInfo.  # noqa: E501
        :type: int
        """

        self._alua_value = alua_value

    @property
    def dc_name(self):
        """Gets the dc_name of this LunInfo.  # noqa: E501


        :return: The dc_name of this LunInfo.  # noqa: E501
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """Sets the dc_name of this LunInfo.


        :param dc_name: The dc_name of this LunInfo.  # noqa: E501
        :type: str
        """

        self._dc_name = dc_name

    @property
    def lun_cfg(self):
        """Gets the lun_cfg of this LunInfo.  # noqa: E501


        :return: The lun_cfg of this LunInfo.  # noqa: E501
        :rtype: str
        """
        return self._lun_cfg

    @lun_cfg.setter
    def lun_cfg(self, lun_cfg):
        """Sets the lun_cfg of this LunInfo.


        :param lun_cfg: The lun_cfg of this LunInfo.  # noqa: E501
        :type: str
        """

        self._lun_cfg = lun_cfg

    @property
    def lun_id(self):
        """Gets the lun_id of this LunInfo.  # noqa: E501


        :return: The lun_id of this LunInfo.  # noqa: E501
        :rtype: int
        """
        return self._lun_id

    @lun_id.setter
    def lun_id(self, lun_id):
        """Sets the lun_id of this LunInfo.


        :param lun_id: The lun_id of this LunInfo.  # noqa: E501
        :type: int
        """

        self._lun_id = lun_id

    @property
    def lun_name(self):
        """Gets the lun_name of this LunInfo.  # noqa: E501


        :return: The lun_name of this LunInfo.  # noqa: E501
        :rtype: str
        """
        return self._lun_name

    @lun_name.setter
    def lun_name(self, lun_name):
        """Sets the lun_name of this LunInfo.


        :param lun_name: The lun_name of this LunInfo.  # noqa: E501
        :type: str
        """

        self._lun_name = lun_name

    @property
    def lun_size(self):
        """Gets the lun_size of this LunInfo.  # noqa: E501


        :return: The lun_size of this LunInfo.  # noqa: E501
        :rtype: int
        """
        return self._lun_size

    @lun_size.setter
    def lun_size(self, lun_size):
        """Sets the lun_size of this LunInfo.


        :param lun_size: The lun_size of this LunInfo.  # noqa: E501
        :type: int
        """

        self._lun_size = lun_size

    @property
    def lun_sn(self):
        """Gets the lun_sn of this LunInfo.  # noqa: E501


        :return: The lun_sn of this LunInfo.  # noqa: E501
        :rtype: str
        """
        return self._lun_sn

    @lun_sn.setter
    def lun_sn(self, lun_sn):
        """Sets the lun_sn of this LunInfo.


        :param lun_sn: The lun_sn of this LunInfo.  # noqa: E501
        :type: str
        """

        self._lun_sn = lun_sn

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
        if not isinstance(other, LunInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
