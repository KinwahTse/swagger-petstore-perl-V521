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
# from xms_client.models.fs_user_group_nestview import FSUserGroupNestview  # noqa: F401,E501
# from xms_client.models.fs_user_nestview import FSUserNestview  # noqa: F401,E501
# from xms_client.models.fsftp_share_nestview import FSFTPShareNestview  # noqa: F401,E501


class FSFTPShareACL(object):
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
        'create_enabled': 'bool',
        'delete_enabled': 'bool',
        'download_bandwidth': 'int',
        'download_enabled': 'bool',
        'fs_ftp_share': 'FSFTPShareNestview',
        'fs_user': 'FSUserNestview',
        'fs_user_group': 'FSUserGroupNestview',
        'id': 'int',
        'list_enabled': 'bool',
        'rename_enabled': 'bool',
        'type': 'str',
        'update': 'datetime',
        'upload_bandwidth': 'int',
        'upload_enabled': 'bool'
    }

    attribute_map = {
        'cluster': 'cluster',
        'create': 'create',
        'create_enabled': 'create_enabled',
        'delete_enabled': 'delete_enabled',
        'download_bandwidth': 'download_bandwidth',
        'download_enabled': 'download_enabled',
        'fs_ftp_share': 'fs_ftp_share',
        'fs_user': 'fs_user',
        'fs_user_group': 'fs_user_group',
        'id': 'id',
        'list_enabled': 'list_enabled',
        'rename_enabled': 'rename_enabled',
        'type': 'type',
        'update': 'update',
        'upload_bandwidth': 'upload_bandwidth',
        'upload_enabled': 'upload_enabled'
    }

    def __init__(self, cluster=None, create=None, create_enabled=None, delete_enabled=None, download_bandwidth=None, download_enabled=None, fs_ftp_share=None, fs_user=None, fs_user_group=None, id=None, list_enabled=None, rename_enabled=None, type=None, update=None, upload_bandwidth=None, upload_enabled=None):  # noqa: E501
        """FSFTPShareACL - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._create = None
        self._create_enabled = None
        self._delete_enabled = None
        self._download_bandwidth = None
        self._download_enabled = None
        self._fs_ftp_share = None
        self._fs_user = None
        self._fs_user_group = None
        self._id = None
        self._list_enabled = None
        self._rename_enabled = None
        self._type = None
        self._update = None
        self._upload_bandwidth = None
        self._upload_enabled = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if create_enabled is not None:
            self.create_enabled = create_enabled
        if delete_enabled is not None:
            self.delete_enabled = delete_enabled
        if download_bandwidth is not None:
            self.download_bandwidth = download_bandwidth
        if download_enabled is not None:
            self.download_enabled = download_enabled
        if fs_ftp_share is not None:
            self.fs_ftp_share = fs_ftp_share
        if fs_user is not None:
            self.fs_user = fs_user
        if fs_user_group is not None:
            self.fs_user_group = fs_user_group
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
    def cluster(self):
        """Gets the cluster of this FSFTPShareACL.  # noqa: E501


        :return: The cluster of this FSFTPShareACL.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this FSFTPShareACL.


        :param cluster: The cluster of this FSFTPShareACL.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this FSFTPShareACL.  # noqa: E501


        :return: The create of this FSFTPShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this FSFTPShareACL.


        :param create: The create of this FSFTPShareACL.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def create_enabled(self):
        """Gets the create_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The create_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._create_enabled

    @create_enabled.setter
    def create_enabled(self, create_enabled):
        """Sets the create_enabled of this FSFTPShareACL.


        :param create_enabled: The create_enabled of this FSFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._create_enabled = create_enabled

    @property
    def delete_enabled(self):
        """Gets the delete_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The delete_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._delete_enabled

    @delete_enabled.setter
    def delete_enabled(self, delete_enabled):
        """Sets the delete_enabled of this FSFTPShareACL.


        :param delete_enabled: The delete_enabled of this FSFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._delete_enabled = delete_enabled

    @property
    def download_bandwidth(self):
        """Gets the download_bandwidth of this FSFTPShareACL.  # noqa: E501


        :return: The download_bandwidth of this FSFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._download_bandwidth

    @download_bandwidth.setter
    def download_bandwidth(self, download_bandwidth):
        """Sets the download_bandwidth of this FSFTPShareACL.


        :param download_bandwidth: The download_bandwidth of this FSFTPShareACL.  # noqa: E501
        :type: int
        """

        self._download_bandwidth = download_bandwidth

    @property
    def download_enabled(self):
        """Gets the download_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The download_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._download_enabled

    @download_enabled.setter
    def download_enabled(self, download_enabled):
        """Sets the download_enabled of this FSFTPShareACL.


        :param download_enabled: The download_enabled of this FSFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._download_enabled = download_enabled

    @property
    def fs_ftp_share(self):
        """Gets the fs_ftp_share of this FSFTPShareACL.  # noqa: E501


        :return: The fs_ftp_share of this FSFTPShareACL.  # noqa: E501
        :rtype: FSFTPShareNestview
        """
        return self._fs_ftp_share

    @fs_ftp_share.setter
    def fs_ftp_share(self, fs_ftp_share):
        """Sets the fs_ftp_share of this FSFTPShareACL.


        :param fs_ftp_share: The fs_ftp_share of this FSFTPShareACL.  # noqa: E501
        :type: FSFTPShareNestview
        """

        self._fs_ftp_share = fs_ftp_share

    @property
    def fs_user(self):
        """Gets the fs_user of this FSFTPShareACL.  # noqa: E501


        :return: The fs_user of this FSFTPShareACL.  # noqa: E501
        :rtype: FSUserNestview
        """
        return self._fs_user

    @fs_user.setter
    def fs_user(self, fs_user):
        """Sets the fs_user of this FSFTPShareACL.


        :param fs_user: The fs_user of this FSFTPShareACL.  # noqa: E501
        :type: FSUserNestview
        """

        self._fs_user = fs_user

    @property
    def fs_user_group(self):
        """Gets the fs_user_group of this FSFTPShareACL.  # noqa: E501


        :return: The fs_user_group of this FSFTPShareACL.  # noqa: E501
        :rtype: FSUserGroupNestview
        """
        return self._fs_user_group

    @fs_user_group.setter
    def fs_user_group(self, fs_user_group):
        """Sets the fs_user_group of this FSFTPShareACL.


        :param fs_user_group: The fs_user_group of this FSFTPShareACL.  # noqa: E501
        :type: FSUserGroupNestview
        """

        self._fs_user_group = fs_user_group

    @property
    def id(self):
        """Gets the id of this FSFTPShareACL.  # noqa: E501


        :return: The id of this FSFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FSFTPShareACL.


        :param id: The id of this FSFTPShareACL.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def list_enabled(self):
        """Gets the list_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The list_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._list_enabled

    @list_enabled.setter
    def list_enabled(self, list_enabled):
        """Sets the list_enabled of this FSFTPShareACL.


        :param list_enabled: The list_enabled of this FSFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._list_enabled = list_enabled

    @property
    def rename_enabled(self):
        """Gets the rename_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The rename_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._rename_enabled

    @rename_enabled.setter
    def rename_enabled(self, rename_enabled):
        """Sets the rename_enabled of this FSFTPShareACL.


        :param rename_enabled: The rename_enabled of this FSFTPShareACL.  # noqa: E501
        :type: bool
        """

        self._rename_enabled = rename_enabled

    @property
    def type(self):
        """Gets the type of this FSFTPShareACL.  # noqa: E501


        :return: The type of this FSFTPShareACL.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FSFTPShareACL.


        :param type: The type of this FSFTPShareACL.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this FSFTPShareACL.  # noqa: E501


        :return: The update of this FSFTPShareACL.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FSFTPShareACL.


        :param update: The update of this FSFTPShareACL.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def upload_bandwidth(self):
        """Gets the upload_bandwidth of this FSFTPShareACL.  # noqa: E501


        :return: The upload_bandwidth of this FSFTPShareACL.  # noqa: E501
        :rtype: int
        """
        return self._upload_bandwidth

    @upload_bandwidth.setter
    def upload_bandwidth(self, upload_bandwidth):
        """Sets the upload_bandwidth of this FSFTPShareACL.


        :param upload_bandwidth: The upload_bandwidth of this FSFTPShareACL.  # noqa: E501
        :type: int
        """

        self._upload_bandwidth = upload_bandwidth

    @property
    def upload_enabled(self):
        """Gets the upload_enabled of this FSFTPShareACL.  # noqa: E501


        :return: The upload_enabled of this FSFTPShareACL.  # noqa: E501
        :rtype: bool
        """
        return self._upload_enabled

    @upload_enabled.setter
    def upload_enabled(self, upload_enabled):
        """Sets the upload_enabled of this FSFTPShareACL.


        :param upload_enabled: The upload_enabled of this FSFTPShareACL.  # noqa: E501
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
        if not isinstance(other, FSFTPShareACL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
