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
# from xms_client.models.dfs_ftp_share_nestview import DfsFTPShareNestview  # noqa: F401,E501
# from xms_client.models.fs_user_nestview import FSUserNestview  # noqa: F401,E501


class DfsFTPShareACL(object):
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
        'admin_enabled': 'bool',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'create_enabled': 'bool',
        'delete_enabled': 'bool',
        'dfs_ftp_share': 'DfsFTPShareNestview',
        'download_bandwidth': 'int',
        'download_enabled': 'bool',
        'fs_user': 'FSUserNestview',
        'id': 'int',
        'list_enabled': 'bool',
        'rename_enabled': 'bool',
        'type': 'str',
        'update': 'datetime',
        'upload_bandwidth': 'int',
        'upload_enabled': 'bool'
    }

    attribute_map = {
        'admin_enabled': 'admin_enabled',
        'cluster': 'cluster',
        'create': 'create',
        'create_enabled': 'create_enabled',
        'delete_enabled': 'delete_enabled',
        'dfs_ftp_share': 'dfs_ftp_share',
        'download_bandwidth': 'download_bandwidth',
        'download_enabled': 'download_enabled',
        'fs_user': 'fs_user',
        'id': 'id',
        'list_enabled': 'list_enabled',
        'rename_enabled': 'rename_enabled',
        'type': 'type',
        'update': 'update',
        'upload_bandwidth': 'upload_bandwidth',
        'upload_enabled': 'upload_enabled'
    }

    def __init__(self, admin_enabled=None, cluster=None, create=None, create_enabled=None, delete_enabled=None, dfs_ftp_share=None, download_bandwidth=None, download_enabled=None, fs_user=None, id=None, list_enabled=None, rename_enabled=None, type=None, update=None, upload_bandwidth=None, upload_enabled=None):  # noqa: E501
        """DfsFTPShareACL - a model defined in Swagger"""  # noqa: E501

        self._admin_enabled = None
        self._cluster = None
        self._create = None
        self._create_enabled = None
        self._delete_enabled = None
        self._dfs_ftp_share = None
        self._download_bandwidth = None
        self._download_enabled = None
        self._fs_user = None
        self._id = None
        self._list_enabled = None
        self._rename_enabled = None
        self._type = None
        self._update = None
        self._upload_bandwidth = None
        self._upload_enabled = None
        self.discriminator = None

        if admin_enabled is not None:
            self.admin_enabled = admin_enabled
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if create_enabled is not None:
            self.create_enabled = create_enabled
        if delete_enabled is not None:
            self.delete_enabled = delete_enabled
        if dfs_ftp_share is not None:
            self.dfs_ftp_share = dfs_ftp_share
        if download_bandwidth is not None:
            self.download_bandwidth = download_bandwidth
        if download_enabled is not None:
            self.download_enabled = download_enabled
        if fs_user is not None:
            self.fs_user = fs_user
        if id is not None:
            self.id = id
        if list_enabled is not None:
            self.list_enabled = list_enabled
        if rename_enabled is not None:
            self.rename_enabled = rename_enabled
        if type is not None:
            self.type = type
        if update is not None:
            self.update = update
        if upload_bandwidth is not None:
            self.upload_bandwidth = upload_bandwidth
        if upload_enabled is not None:
            self.upload_enabled = upload_enabled

    @property
    def admin_enabled(self):
        """Gets the admin_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The admin_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._admin_enabled

    @admin_enabled.setter
    def admin_enabled(self, admin_enabled):
        """Sets the admin_enabled of this DfsFTPShareACL.


        :param admin_enabled: The admin_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._admin_enabled = admin_enabled

    @property
    def cluster(self):
        """Gets the cluster of this DfsFTPShareACL.  # noqa: E501


        :return: The cluster of this DfsFTPShareACL.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsFTPShareACL.


        :param cluster: The cluster of this DfsFTPShareACL.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsFTPShareACL.  # noqa: E501


        :return: The create of this DfsFTPShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsFTPShareACL.


        :param create: The create of this DfsFTPShareACL.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def create_enabled(self):
        """Gets the create_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The create_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._create_enabled

    @create_enabled.setter
    def create_enabled(self, create_enabled):
        """Sets the create_enabled of this DfsFTPShareACL.


        :param create_enabled: The create_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._create_enabled = create_enabled

    @property
    def delete_enabled(self):
        """Gets the delete_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The delete_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._delete_enabled

    @delete_enabled.setter
    def delete_enabled(self, delete_enabled):
        """Sets the delete_enabled of this DfsFTPShareACL.


        :param delete_enabled: The delete_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._delete_enabled = delete_enabled

    @property
    def dfs_ftp_share(self):
        """Gets the dfs_ftp_share of this DfsFTPShareACL.  # noqa: E501


        :return: The dfs_ftp_share of this DfsFTPShareACL.  # noqa: E501
        :rtype: DfsFTPShareNestview
        """
        return self._dfs_ftp_share

    @dfs_ftp_share.setter
    def dfs_ftp_share(self, dfs_ftp_share):
        """Sets the dfs_ftp_share of this DfsFTPShareACL.


        :param dfs_ftp_share: The dfs_ftp_share of this DfsFTPShareACL.  # noqa: E501
        :type: DfsFTPShareNestview
        """

        self._dfs_ftp_share = dfs_ftp_share

    @property
    def download_bandwidth(self):
        """Gets the download_bandwidth of this DfsFTPShareACL.  # noqa: E501


        :return: The download_bandwidth of this DfsFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._download_bandwidth

    @download_bandwidth.setter
    def download_bandwidth(self, download_bandwidth):
        """Sets the download_bandwidth of this DfsFTPShareACL.


        :param download_bandwidth: The download_bandwidth of this DfsFTPShareACL.  # noqa: E501
        :type: int
        """

        self._download_bandwidth = download_bandwidth

    @property
    def download_enabled(self):
        """Gets the download_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The download_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._download_enabled

    @download_enabled.setter
    def download_enabled(self, download_enabled):
        """Sets the download_enabled of this DfsFTPShareACL.


        :param download_enabled: The download_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._download_enabled = download_enabled

    @property
    def fs_user(self):
        """Gets the fs_user of this DfsFTPShareACL.  # noqa: E501


        :return: The fs_user of this DfsFTPShareACL.  # noqa: E501
        :rtype: FSUserNestview
        """
        return self._fs_user

    @fs_user.setter
    def fs_user(self, fs_user):
        """Sets the fs_user of this DfsFTPShareACL.


        :param fs_user: The fs_user of this DfsFTPShareACL.  # noqa: E501
        :type: FSUserNestview
        """

        self._fs_user = fs_user

    @property
    def id(self):
        """Gets the id of this DfsFTPShareACL.  # noqa: E501


        :return: The id of this DfsFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsFTPShareACL.


        :param id: The id of this DfsFTPShareACL.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def list_enabled(self):
        """Gets the list_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The list_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._list_enabled

    @list_enabled.setter
    def list_enabled(self, list_enabled):
        """Sets the list_enabled of this DfsFTPShareACL.


        :param list_enabled: The list_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._list_enabled = list_enabled

    @property
    def rename_enabled(self):
        """Gets the rename_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The rename_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._rename_enabled

    @rename_enabled.setter
    def rename_enabled(self, rename_enabled):
        """Sets the rename_enabled of this DfsFTPShareACL.


        :param rename_enabled: The rename_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._rename_enabled = rename_enabled

    @property
    def type(self):
        """Gets the type of this DfsFTPShareACL.  # noqa: E501


        :return: The type of this DfsFTPShareACL.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DfsFTPShareACL.


        :param type: The type of this DfsFTPShareACL.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this DfsFTPShareACL.  # noqa: E501


        :return: The update of this DfsFTPShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsFTPShareACL.


        :param update: The update of this DfsFTPShareACL.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def upload_bandwidth(self):
        """Gets the upload_bandwidth of this DfsFTPShareACL.  # noqa: E501


        :return: The upload_bandwidth of this DfsFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._upload_bandwidth

    @upload_bandwidth.setter
    def upload_bandwidth(self, upload_bandwidth):
        """Sets the upload_bandwidth of this DfsFTPShareACL.


        :param upload_bandwidth: The upload_bandwidth of this DfsFTPShareACL.  # noqa: E501
        :type: int
        """

        self._upload_bandwidth = upload_bandwidth

    @property
    def upload_enabled(self):
        """Gets the upload_enabled of this DfsFTPShareACL.  # noqa: E501


        :return: The upload_enabled of this DfsFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._upload_enabled

    @upload_enabled.setter
    def upload_enabled(self, upload_enabled):
        """Sets the upload_enabled of this DfsFTPShareACL.


        :param upload_enabled: The upload_enabled of this DfsFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._upload_enabled = upload_enabled

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
        if not isinstance(other, DfsFTPShareACL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other