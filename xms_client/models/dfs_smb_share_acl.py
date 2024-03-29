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

# from xms_client.models.cluster_nestview import ClusterNestview  # noqa: F401,E501
# from xms_client.models.dfs_smb_share_nestview import DfsSMBShareNestview  # noqa: F401,E501
# from xms_client.models.fs_user_group_nestview import FSUserGroupNestview  # noqa: F401,E501
# from xms_client.models.fs_user_nestview import FSUserNestview  # noqa: F401,E501


class DfsSMBShareACL(object):
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
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'dfs_smb_share': 'DfsSMBShareNestview',
        'fs_user': 'FSUserNestview',
        'fs_user_group': 'FSUserGroupNestview',
        'fs_user_group_name': 'str',
        'fs_user_name': 'str',
        'id': 'int',
        'permission': 'str',
        'security': 'str',
        'type': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'dfs_smb_share': 'dfs_smb_share',
        'fs_user': 'fs_user',
        'fs_user_group': 'fs_user_group',
        'fs_user_group_name': 'fs_user_group_name',
        'fs_user_name': 'fs_user_name',
        'id': 'id',
        'permission': 'permission',
        'security': 'security',
        'type': 'type',
        'update': 'update'
    }

    def __init__(self, cluster=None, create=None, dfs_smb_share=None, fs_user=None, fs_user_group=None, fs_user_group_name=None, fs_user_name=None, id=None, permission=None, security=None, type=None, update=None):  # noqa: E501
        """DfsSMBShareACL - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._dfs_smb_share = None
        self._fs_user = None
        self._fs_user_group = None
        self._fs_user_group_name = None
        self._fs_user_name = None
        self._id = None
        self._permission = None
        self._security = None
        self._type = None
        self._update = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if dfs_smb_share is not None:
            self.dfs_smb_share = dfs_smb_share
        if fs_user is not None:
            self.fs_user = fs_user
        if fs_user_group is not None:
            self.fs_user_group = fs_user_group
        if fs_user_group_name is not None:
            self.fs_user_group_name = fs_user_group_name
        if fs_user_name is not None:
            self.fs_user_name = fs_user_name
        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if security is not None:
            self.security = security
        if type is not None:
            self.type = type
        if update is not None:
            self.update = update

    @property
    def cluster(self):
        """Gets the cluster of this DfsSMBShareACL.  # noqa: E501


        :return: The cluster of this DfsSMBShareACL.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsSMBShareACL.


        :param cluster: The cluster of this DfsSMBShareACL.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsSMBShareACL.  # noqa: E501


        :return: The create of this DfsSMBShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsSMBShareACL.


        :param create: The create of this DfsSMBShareACL.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dfs_smb_share(self):
        """Gets the dfs_smb_share of this DfsSMBShareACL.  # noqa: E501


        :return: The dfs_smb_share of this DfsSMBShareACL.  # noqa: E501
        :rtype: DfsSMBShareNestview
        """
        return self._dfs_smb_share

    @dfs_smb_share.setter
    def dfs_smb_share(self, dfs_smb_share):
        """Sets the dfs_smb_share of this DfsSMBShareACL.


        :param dfs_smb_share: The dfs_smb_share of this DfsSMBShareACL.  # noqa: E501
        :type: DfsSMBShareNestview
        """

        self._dfs_smb_share = dfs_smb_share

    @property
    def fs_user(self):
        """Gets the fs_user of this DfsSMBShareACL.  # noqa: E501


        :return: The fs_user of this DfsSMBShareACL.  # noqa: E501
        :rtype: FSUserNestview
        """
        return self._fs_user

    @fs_user.setter
    def fs_user(self, fs_user):
        """Sets the fs_user of this DfsSMBShareACL.


        :param fs_user: The fs_user of this DfsSMBShareACL.  # noqa: E501
        :type: FSUserNestview
        """

        self._fs_user = fs_user

    @property
    def fs_user_group(self):
        """Gets the fs_user_group of this DfsSMBShareACL.  # noqa: E501


        :return: The fs_user_group of this DfsSMBShareACL.  # noqa: E501
        :rtype: FSUserGroupNestview
        """
        return self._fs_user_group

    @fs_user_group.setter
    def fs_user_group(self, fs_user_group):
        """Sets the fs_user_group of this DfsSMBShareACL.


        :param fs_user_group: The fs_user_group of this DfsSMBShareACL.  # noqa: E501
        :type: FSUserGroupNestview
        """

        self._fs_user_group = fs_user_group

    @property
    def fs_user_group_name(self):
        """Gets the fs_user_group_name of this DfsSMBShareACL.  # noqa: E501


        :return: The fs_user_group_name of this DfsSMBShareACL.  # noqa: E501
        :rtype: str
        """
        return self._fs_user_group_name

    @fs_user_group_name.setter
    def fs_user_group_name(self, fs_user_group_name):
        """Sets the fs_user_group_name of this DfsSMBShareACL.


        :param fs_user_group_name: The fs_user_group_name of this DfsSMBShareACL.  # noqa: E501
        :type: str
        """

        self._fs_user_group_name = fs_user_group_name

    @property
    def fs_user_name(self):
        """Gets the fs_user_name of this DfsSMBShareACL.  # noqa: E501


        :return: The fs_user_name of this DfsSMBShareACL.  # noqa: E501
        :rtype: str
        """
        return self._fs_user_name

    @fs_user_name.setter
    def fs_user_name(self, fs_user_name):
        """Sets the fs_user_name of this DfsSMBShareACL.


        :param fs_user_name: The fs_user_name of this DfsSMBShareACL.  # noqa: E501
        :type: str
        """

        self._fs_user_name = fs_user_name

    @property
    def id(self):
        """Gets the id of this DfsSMBShareACL.  # noqa: E501


        :return: The id of this DfsSMBShareACL.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsSMBShareACL.


        :param id: The id of this DfsSMBShareACL.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def permission(self):
        """Gets the permission of this DfsSMBShareACL.  # noqa: E501


        :return: The permission of this DfsSMBShareACL.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DfsSMBShareACL.


        :param permission: The permission of this DfsSMBShareACL.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def security(self):
        """Gets the security of this DfsSMBShareACL.  # noqa: E501


        :return: The security of this DfsSMBShareACL.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this DfsSMBShareACL.


        :param security: The security of this DfsSMBShareACL.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def type(self):
        """Gets the type of this DfsSMBShareACL.  # noqa: E501


        :return: The type of this DfsSMBShareACL.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DfsSMBShareACL.


        :param type: The type of this DfsSMBShareACL.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this DfsSMBShareACL.  # noqa: E501


        :return: The update of this DfsSMBShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsSMBShareACL.


        :param update: The update of this DfsSMBShareACL.  # noqa: E501
        :type: datetime
        """

        self._update = update

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
        if not isinstance(other, DfsSMBShareACL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
