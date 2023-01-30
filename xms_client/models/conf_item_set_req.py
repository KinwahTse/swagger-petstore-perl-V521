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

# from xms_client.models.conf_item_set_req_conf_item import ConfItemSetReqConfItem  # noqa: F401,E501


class ConfItemSetReq(object):
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
        'conf': 'ConfItemSetReqConfItem'
    }

    attribute_map = {
        'conf': 'conf'
    }

    def __init__(self, conf=None):  # noqa: E501
        """ConfItemSetReq - a model defined in Swagger"""  # noqa: E501

        self._conf = None
        self.discriminator = None

        self.conf = conf

    @property
    def conf(self):
        """Gets the conf of this ConfItemSetReq.  # noqa: E501


        :return: The conf of this ConfItemSetReq.  # noqa: E501
        :rtype: ConfItemSetReqConfItem
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this ConfItemSetReq.


        :param conf: The conf of this ConfItemSetReq.  # noqa: E501
        :type: ConfItemSetReqConfItem
        """
        if conf is None:
            raise ValueError("Invalid value for `conf`, must not be `None`")  # noqa: E501

        self._conf = conf

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
        if not isinstance(other, ConfItemSetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
