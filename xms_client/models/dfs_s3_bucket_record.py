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
# from xms_client.models.dfs_gateway_group_nestview import DfsGatewayGroupNestview  # noqa: F401,E501
# from xms_client.models.dfs_path_nestview import DfsPathNestview  # noqa: F401,E501
# from xms_client.models.dfs_rootfs_nestview import DfsRootfsNestview  # noqa: F401,E501
# from xms_client.models.dfs_s3_bucket import DfsS3Bucket  # noqa: F401,E501
# from xms_client.models.dfs_s3_bucket_stat import DfsS3BucketStat  # noqa: F401,E501
# from xms_client.models.fs_user_nestview import FSUserNestview  # noqa: F401,E501


class DfsS3BucketRecord(object):
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
        'action_status': 'str',
        'all_user_permission': 'str',
        'auth_user_permission': 'str',
        'bucket_policy': 'str',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'data_verify': 'bool',
        'dfs_gateway_group': 'DfsGatewayGroupNestview',
        'dfs_rootfs': 'DfsRootfsNestview',
        'enable_etag': 'bool',
        'id': 'int',
        'name': 'str',
        'owner': 'FSUserNestview',
        'owner_permission': 'str',
        'path': 'DfsPathNestview',
        'status': 'str',
        'update': 'datetime',
        'samples': 'list[DfsS3BucketStat]'
    }

    attribute_map = {
        'action_status': 'action_status',
        'all_user_permission': 'all_user_permission',
        'auth_user_permission': 'auth_user_permission',
        'bucket_policy': 'bucket_policy',
        'cluster': 'cluster',
        'create': 'create',
        'data_verify': 'data_verify',
        'dfs_gateway_group': 'dfs_gateway_group',
        'dfs_rootfs': 'dfs_rootfs',
        'enable_etag': 'enable_etag',
        'id': 'id',
        'name': 'name',
        'owner': 'owner',
        'owner_permission': 'owner_permission',
        'path': 'path',
        'status': 'status',
        'update': 'update',
        'samples': 'samples'
    }

    def __init__(self, action_status=None, all_user_permission=None, auth_user_permission=None, bucket_policy=None, cluster=None, create=None, data_verify=None, dfs_gateway_group=None, dfs_rootfs=None, enable_etag=None, id=None, name=None, owner=None, owner_permission=None, path=None, status=None, update=None, samples=None):  # noqa: E501
        """DfsS3BucketRecord - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._all_user_permission = None
        self._auth_user_permission = None
        self._bucket_policy = None
        self._cluster = None
        self._create = None
        self._data_verify = None
        self._dfs_gateway_group = None
        self._dfs_rootfs = None
        self._enable_etag = None
        self._id = None
        self._name = None
        self._owner = None
        self._owner_permission = None
        self._path = None
        self._status = None
        self._update = None
        self._samples = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if all_user_permission is not None:
            self.all_user_permission = all_user_permission
        if auth_user_permission is not None:
            self.auth_user_permission = auth_user_permission
        if bucket_policy is not None:
            self.bucket_policy = bucket_policy
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if data_verify is not None:
            self.data_verify = data_verify
        if dfs_gateway_group is not None:
            self.dfs_gateway_group = dfs_gateway_group
        if dfs_rootfs is not None:
            self.dfs_rootfs = dfs_rootfs
        if enable_etag is not None:
            self.enable_etag = enable_etag
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if owner_permission is not None:
            self.owner_permission = owner_permission
        if path is not None:
            self.path = path
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if samples is not None:
            self.samples = samples

    @property
    def action_status(self):
        """Gets the action_status of this DfsS3BucketRecord.  # noqa: E501


        :return: The action_status of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this DfsS3BucketRecord.


        :param action_status: The action_status of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def all_user_permission(self):
        """Gets the all_user_permission of this DfsS3BucketRecord.  # noqa: E501


        :return: The all_user_permission of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._all_user_permission

    @all_user_permission.setter
    def all_user_permission(self, all_user_permission):
        """Sets the all_user_permission of this DfsS3BucketRecord.


        :param all_user_permission: The all_user_permission of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._all_user_permission = all_user_permission

    @property
    def auth_user_permission(self):
        """Gets the auth_user_permission of this DfsS3BucketRecord.  # noqa: E501


        :return: The auth_user_permission of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._auth_user_permission

    @auth_user_permission.setter
    def auth_user_permission(self, auth_user_permission):
        """Sets the auth_user_permission of this DfsS3BucketRecord.


        :param auth_user_permission: The auth_user_permission of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._auth_user_permission = auth_user_permission

    @property
    def bucket_policy(self):
        """Gets the bucket_policy of this DfsS3BucketRecord.  # noqa: E501


        :return: The bucket_policy of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._bucket_policy

    @bucket_policy.setter
    def bucket_policy(self, bucket_policy):
        """Sets the bucket_policy of this DfsS3BucketRecord.


        :param bucket_policy: The bucket_policy of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._bucket_policy = bucket_policy

    @property
    def cluster(self):
        """Gets the cluster of this DfsS3BucketRecord.  # noqa: E501


        :return: The cluster of this DfsS3BucketRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsS3BucketRecord.


        :param cluster: The cluster of this DfsS3BucketRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsS3BucketRecord.  # noqa: E501


        :return: The create of this DfsS3BucketRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsS3BucketRecord.


        :param create: The create of this DfsS3BucketRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def data_verify(self):
        """Gets the data_verify of this DfsS3BucketRecord.  # noqa: E501


        :return: The data_verify of this DfsS3BucketRecord.  # noqa: E501
        :rtype: bool
        """
        return self._data_verify

    @data_verify.setter
    def data_verify(self, data_verify):
        """Sets the data_verify of this DfsS3BucketRecord.


        :param data_verify: The data_verify of this DfsS3BucketRecord.  # noqa: E501
        :type: bool
        """

        self._data_verify = data_verify

    @property
    def dfs_gateway_group(self):
        """Gets the dfs_gateway_group of this DfsS3BucketRecord.  # noqa: E501


        :return: The dfs_gateway_group of this DfsS3BucketRecord.  # noqa: E501
        :rtype: DfsGatewayGroupNestview
        """
        return self._dfs_gateway_group

    @dfs_gateway_group.setter
    def dfs_gateway_group(self, dfs_gateway_group):
        """Sets the dfs_gateway_group of this DfsS3BucketRecord.


        :param dfs_gateway_group: The dfs_gateway_group of this DfsS3BucketRecord.  # noqa: E501
        :type: DfsGatewayGroupNestview
        """

        self._dfs_gateway_group = dfs_gateway_group

    @property
    def dfs_rootfs(self):
        """Gets the dfs_rootfs of this DfsS3BucketRecord.  # noqa: E501


        :return: The dfs_rootfs of this DfsS3BucketRecord.  # noqa: E501
        :rtype: DfsRootfsNestview
        """
        return self._dfs_rootfs

    @dfs_rootfs.setter
    def dfs_rootfs(self, dfs_rootfs):
        """Sets the dfs_rootfs of this DfsS3BucketRecord.


        :param dfs_rootfs: The dfs_rootfs of this DfsS3BucketRecord.  # noqa: E501
        :type: DfsRootfsNestview
        """

        self._dfs_rootfs = dfs_rootfs

    @property
    def enable_etag(self):
        """Gets the enable_etag of this DfsS3BucketRecord.  # noqa: E501


        :return: The enable_etag of this DfsS3BucketRecord.  # noqa: E501
        :rtype: bool
        """
        return self._enable_etag

    @enable_etag.setter
    def enable_etag(self, enable_etag):
        """Sets the enable_etag of this DfsS3BucketRecord.


        :param enable_etag: The enable_etag of this DfsS3BucketRecord.  # noqa: E501
        :type: bool
        """

        self._enable_etag = enable_etag

    @property
    def id(self):
        """Gets the id of this DfsS3BucketRecord.  # noqa: E501


        :return: The id of this DfsS3BucketRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsS3BucketRecord.


        :param id: The id of this DfsS3BucketRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DfsS3BucketRecord.  # noqa: E501


        :return: The name of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DfsS3BucketRecord.


        :param name: The name of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this DfsS3BucketRecord.  # noqa: E501


        :return: The owner of this DfsS3BucketRecord.  # noqa: E501
        :rtype: FSUserNestview
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DfsS3BucketRecord.


        :param owner: The owner of this DfsS3BucketRecord.  # noqa: E501
        :type: FSUserNestview
        """

        self._owner = owner

    @property
    def owner_permission(self):
        """Gets the owner_permission of this DfsS3BucketRecord.  # noqa: E501


        :return: The owner_permission of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._owner_permission

    @owner_permission.setter
    def owner_permission(self, owner_permission):
        """Sets the owner_permission of this DfsS3BucketRecord.


        :param owner_permission: The owner_permission of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._owner_permission = owner_permission

    @property
    def path(self):
        """Gets the path of this DfsS3BucketRecord.  # noqa: E501


        :return: The path of this DfsS3BucketRecord.  # noqa: E501
        :rtype: DfsPathNestview
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsS3BucketRecord.


        :param path: The path of this DfsS3BucketRecord.  # noqa: E501
        :type: DfsPathNestview
        """

        self._path = path

    @property
    def status(self):
        """Gets the status of this DfsS3BucketRecord.  # noqa: E501


        :return: The status of this DfsS3BucketRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DfsS3BucketRecord.


        :param status: The status of this DfsS3BucketRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this DfsS3BucketRecord.  # noqa: E501


        :return: The update of this DfsS3BucketRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsS3BucketRecord.


        :param update: The update of this DfsS3BucketRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def samples(self):
        """Gets the samples of this DfsS3BucketRecord.  # noqa: E501


        :return: The samples of this DfsS3BucketRecord.  # noqa: E501
        :rtype: list[DfsS3BucketStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this DfsS3BucketRecord.


        :param samples: The samples of this DfsS3BucketRecord.  # noqa: E501
        :type: list[DfsS3BucketStat]
        """

        self._samples = samples

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
        if not isinstance(other, DfsS3BucketRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other