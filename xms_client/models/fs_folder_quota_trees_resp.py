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

# from xms_client.models.fs_folder_record import FSFolderRecord  # noqa: F401,E501
# from xms_client.models.fs_quota_tree import FSQuotaTree  # noqa: F401,E501


class FSFolderQuotaTreesResp(object):
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
        'fs_folder': 'FSFolderRecord',
        'fs_quota_trees': 'list[FSQuotaTree]'
    }

    attribute_map = {
        'fs_folder': 'fs_folder',
        'fs_quota_trees': 'fs_quota_trees'
    }

    def __init__(self, fs_folder=None, fs_quota_trees=None):  # noqa: E501
        """FSFolderQuotaTreesResp - a model defined in Swagger"""  # noqa: E501

        self._fs_folder = None
        self._fs_quota_trees = None
        self.discriminator = None

        self.fs_folder = fs_folder
        self.fs_quota_trees = fs_quota_trees

    @property
    def fs_folder(self):
        """Gets the fs_folder of this FSFolderQuotaTreesResp.  # noqa: E501

        file storage folder records  # noqa: E501

        :return: The fs_folder of this FSFolderQuotaTreesResp.  # noqa: E501
        :rtype: FSFolderRecord
        """
        return self._fs_folder

    @fs_folder.setter
    def fs_folder(self, fs_folder):
        """Sets the fs_folder of this FSFolderQuotaTreesResp.

        file storage folder records  # noqa: E501

        :param fs_folder: The fs_folder of this FSFolderQuotaTreesResp.  # noqa: E501
        :type: FSFolderRecord
        """
        if fs_folder is None:
            raise ValueError("Invalid value for `fs_folder`, must not be `None`")  # noqa: E501

        self._fs_folder = fs_folder

    @property
    def fs_quota_trees(self):
        """Gets the fs_quota_trees of this FSFolderQuotaTreesResp.  # noqa: E501


        :return: The fs_quota_trees of this FSFolderQuotaTreesResp.  # noqa: E501
        :rtype: list[FSQuotaTree]
        """
        return self._fs_quota_trees

    @fs_quota_trees.setter
    def fs_quota_trees(self, fs_quota_trees):
        """Sets the fs_quota_trees of this FSFolderQuotaTreesResp.


        :param fs_quota_trees: The fs_quota_trees of this FSFolderQuotaTreesResp.  # noqa: E501
        :type: list[FSQuotaTree]
        """
        if fs_quota_trees is None:
            raise ValueError("Invalid value for `fs_quota_trees`, must not be `None`")  # noqa: E501

        self._fs_quota_trees = fs_quota_trees

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
        if not isinstance(other, FSFolderQuotaTreesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
