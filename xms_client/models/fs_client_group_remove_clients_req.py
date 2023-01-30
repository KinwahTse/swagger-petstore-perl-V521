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

# from xms_client.models.fs_client_group_remove_clients_req_client_group import FSClientGroupRemoveClientsReqClientGroup  # noqa: F401,E501


class FSClientGroupRemoveClientsReq(object):
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
        'fs_client_group': 'FSClientGroupRemoveClientsReqClientGroup'
    }

    attribute_map = {
        'fs_client_group': 'fs_client_group'
    }

    def __init__(self, fs_client_group=None):  # noqa: E501
        """FSClientGroupRemoveClientsReq - a model defined in Swagger"""  # noqa: E501

        self._fs_client_group = None
        self.discriminator = None

        self.fs_client_group = fs_client_group

    @property
    def fs_client_group(self):
        """Gets the fs_client_group of this FSClientGroupRemoveClientsReq.  # noqa: E501


        :return: The fs_client_group of this FSClientGroupRemoveClientsReq.  # noqa: E501
        :rtype: FSClientGroupRemoveClientsReqClientGroup
        """
        return self._fs_client_group

    @fs_client_group.setter
    def fs_client_group(self, fs_client_group):
        """Sets the fs_client_group of this FSClientGroupRemoveClientsReq.


        :param fs_client_group: The fs_client_group of this FSClientGroupRemoveClientsReq.  # noqa: E501
        :type: FSClientGroupRemoveClientsReqClientGroup
        """
        if fs_client_group is None:
            raise ValueError("Invalid value for `fs_client_group`, must not be `None`")  # noqa: E501

        self._fs_client_group = fs_client_group

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
        if not isinstance(other, FSClientGroupRemoveClientsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
