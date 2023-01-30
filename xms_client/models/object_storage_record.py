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
# from xms_client.models.object_storage import ObjectStorage  # noqa: F401,E501
# from xms_client.models.object_storage_stat import ObjectStorageStat  # noqa: F401,E501
# from xms_client.models.pool_nestview import PoolNestview  # noqa: F401,E501


class ObjectStorageRecord(object):
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
        'cluster': 'ClusterNestview',
        'cname_enabled': 'bool',
        'create': 'datetime',
        'dns_names': 'list[str]',
        'id': 'int',
        'index_pool': 'PoolNestview',
        'lifecycle_end_on': 'str',
        'lifecycle_start_on': 'str',
        'multi_zone_enabled': 'bool',
        'name': 'str',
        'origin_pull_host_ids': 'list[int]',
        's3_lb_system_user_ak': 'str',
        's3_lb_system_user_sk': 'str',
        'search_enabled': 'bool',
        'second_mergence_enabled': 'bool',
        'second_mergence_end_on': 'str',
        'second_mergence_start_on': 'str',
        'status': 'str',
        'tiering_host_ids': 'list[int]',
        'update': 'datetime',
        'samples': 'list[ObjectStorageStat]'
    }

    attribute_map = {
        'action_status': 'action_status',
        'cluster': 'cluster',
        'cname_enabled': 'cname_enabled',
        'create': 'create',
        'dns_names': 'dns_names',
        'id': 'id',
        'index_pool': 'index_pool',
        'lifecycle_end_on': 'lifecycle_end_on',
        'lifecycle_start_on': 'lifecycle_start_on',
        'multi_zone_enabled': 'multi_zone_enabled',
        'name': 'name',
        'origin_pull_host_ids': 'origin_pull_host_ids',
        's3_lb_system_user_ak': 's3_lb_system_user_ak',
        's3_lb_system_user_sk': 's3_lb_system_user_sk',
        'search_enabled': 'search_enabled',
        'second_mergence_enabled': 'second_mergence_enabled',
        'second_mergence_end_on': 'second_mergence_end_on',
        'second_mergence_start_on': 'second_mergence_start_on',
        'status': 'status',
        'tiering_host_ids': 'tiering_host_ids',
        'update': 'update',
        'samples': 'samples'
    }

    def __init__(self, action_status=None, cluster=None, cname_enabled=None, create=None, dns_names=None, id=None, index_pool=None, lifecycle_end_on=None, lifecycle_start_on=None, multi_zone_enabled=None, name=None, origin_pull_host_ids=None, s3_lb_system_user_ak=None, s3_lb_system_user_sk=None, search_enabled=None, second_mergence_enabled=None, second_mergence_end_on=None, second_mergence_start_on=None, status=None, tiering_host_ids=None, update=None, samples=None):  # noqa: E501
        """ObjectStorageRecord - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._cluster = None
        self._cname_enabled = None
        self._create = None
        self._dns_names = None
        self._id = None
        self._index_pool = None
        self._lifecycle_end_on = None
        self._lifecycle_start_on = None
        self._multi_zone_enabled = None
        self._name = None
        self._origin_pull_host_ids = None
        self._s3_lb_system_user_ak = None
        self._s3_lb_system_user_sk = None
        self._search_enabled = None
        self._second_mergence_enabled = None
        self._second_mergence_end_on = None
        self._second_mergence_start_on = None
        self._status = None
        self._tiering_host_ids = None
        self._update = None
        self._samples = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if cluster is not None:
            self.cluster = cluster
        if cname_enabled is not None:
            self.cname_enabled = cname_enabled
        if create is not None:
            self.create = create
        if dns_names is not None:
            self.dns_names = dns_names
        if id is not None:
            self.id = id
        if index_pool is not None:
            self.index_pool = index_pool
        if lifecycle_end_on is not None:
            self.lifecycle_end_on = lifecycle_end_on
        if lifecycle_start_on is not None:
            self.lifecycle_start_on = lifecycle_start_on
        if multi_zone_enabled is not None:
            self.multi_zone_enabled = multi_zone_enabled
        if name is not None:
            self.name = name
        if origin_pull_host_ids is not None:
            self.origin_pull_host_ids = origin_pull_host_ids
        if s3_lb_system_user_ak is not None:
            self.s3_lb_system_user_ak = s3_lb_system_user_ak
        if s3_lb_system_user_sk is not None:
            self.s3_lb_system_user_sk = s3_lb_system_user_sk
        if search_enabled is not None:
            self.search_enabled = search_enabled
        if second_mergence_enabled is not None:
            self.second_mergence_enabled = second_mergence_enabled
        if second_mergence_end_on is not None:
            self.second_mergence_end_on = second_mergence_end_on
        if second_mergence_start_on is not None:
            self.second_mergence_start_on = second_mergence_start_on
        if status is not None:
            self.status = status
        if tiering_host_ids is not None:
            self.tiering_host_ids = tiering_host_ids
        if update is not None:
            self.update = update
        if samples is not None:
            self.samples = samples

    @property
    def action_status(self):
        """Gets the action_status of this ObjectStorageRecord.  # noqa: E501


        :return: The action_status of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this ObjectStorageRecord.


        :param action_status: The action_status of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def cluster(self):
        """Gets the cluster of this ObjectStorageRecord.  # noqa: E501


        :return: The cluster of this ObjectStorageRecord.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ObjectStorageRecord.


        :param cluster: The cluster of this ObjectStorageRecord.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def cname_enabled(self):
        """Gets the cname_enabled of this ObjectStorageRecord.  # noqa: E501


        :return: The cname_enabled of this ObjectStorageRecord.  # noqa: E501
        :rtype: bool
        """
        return self._cname_enabled

    @cname_enabled.setter
    def cname_enabled(self, cname_enabled):
        """Sets the cname_enabled of this ObjectStorageRecord.


        :param cname_enabled: The cname_enabled of this ObjectStorageRecord.  # noqa: E501
        :type: bool
        """

        self._cname_enabled = cname_enabled

    @property
    def create(self):
        """Gets the create of this ObjectStorageRecord.  # noqa: E501


        :return: The create of this ObjectStorageRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ObjectStorageRecord.


        :param create: The create of this ObjectStorageRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def dns_names(self):
        """Gets the dns_names of this ObjectStorageRecord.  # noqa: E501


        :return: The dns_names of this ObjectStorageRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        """Sets the dns_names of this ObjectStorageRecord.


        :param dns_names: The dns_names of this ObjectStorageRecord.  # noqa: E501
        :type: list[str]
        """

        self._dns_names = dns_names

    @property
    def id(self):
        """Gets the id of this ObjectStorageRecord.  # noqa: E501


        :return: The id of this ObjectStorageRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectStorageRecord.


        :param id: The id of this ObjectStorageRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def index_pool(self):
        """Gets the index_pool of this ObjectStorageRecord.  # noqa: E501


        :return: The index_pool of this ObjectStorageRecord.  # noqa: E501
        :rtype: PoolNestview
        """
        return self._index_pool

    @index_pool.setter
    def index_pool(self, index_pool):
        """Sets the index_pool of this ObjectStorageRecord.


        :param index_pool: The index_pool of this ObjectStorageRecord.  # noqa: E501
        :type: PoolNestview
        """

        self._index_pool = index_pool

    @property
    def lifecycle_end_on(self):
        """Gets the lifecycle_end_on of this ObjectStorageRecord.  # noqa: E501


        :return: The lifecycle_end_on of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_end_on

    @lifecycle_end_on.setter
    def lifecycle_end_on(self, lifecycle_end_on):
        """Sets the lifecycle_end_on of this ObjectStorageRecord.


        :param lifecycle_end_on: The lifecycle_end_on of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._lifecycle_end_on = lifecycle_end_on

    @property
    def lifecycle_start_on(self):
        """Gets the lifecycle_start_on of this ObjectStorageRecord.  # noqa: E501


        :return: The lifecycle_start_on of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_start_on

    @lifecycle_start_on.setter
    def lifecycle_start_on(self, lifecycle_start_on):
        """Sets the lifecycle_start_on of this ObjectStorageRecord.


        :param lifecycle_start_on: The lifecycle_start_on of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._lifecycle_start_on = lifecycle_start_on

    @property
    def multi_zone_enabled(self):
        """Gets the multi_zone_enabled of this ObjectStorageRecord.  # noqa: E501


        :return: The multi_zone_enabled of this ObjectStorageRecord.  # noqa: E501
        :rtype: bool
        """
        return self._multi_zone_enabled

    @multi_zone_enabled.setter
    def multi_zone_enabled(self, multi_zone_enabled):
        """Sets the multi_zone_enabled of this ObjectStorageRecord.


        :param multi_zone_enabled: The multi_zone_enabled of this ObjectStorageRecord.  # noqa: E501
        :type: bool
        """

        self._multi_zone_enabled = multi_zone_enabled

    @property
    def name(self):
        """Gets the name of this ObjectStorageRecord.  # noqa: E501


        :return: The name of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectStorageRecord.


        :param name: The name of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def origin_pull_host_ids(self):
        """Gets the origin_pull_host_ids of this ObjectStorageRecord.  # noqa: E501


        :return: The origin_pull_host_ids of this ObjectStorageRecord.  # noqa: E501
        :rtype: list[int]
        """
        return self._origin_pull_host_ids

    @origin_pull_host_ids.setter
    def origin_pull_host_ids(self, origin_pull_host_ids):
        """Sets the origin_pull_host_ids of this ObjectStorageRecord.


        :param origin_pull_host_ids: The origin_pull_host_ids of this ObjectStorageRecord.  # noqa: E501
        :type: list[int]
        """

        self._origin_pull_host_ids = origin_pull_host_ids

    @property
    def s3_lb_system_user_ak(self):
        """Gets the s3_lb_system_user_ak of this ObjectStorageRecord.  # noqa: E501


        :return: The s3_lb_system_user_ak of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._s3_lb_system_user_ak

    @s3_lb_system_user_ak.setter
    def s3_lb_system_user_ak(self, s3_lb_system_user_ak):
        """Sets the s3_lb_system_user_ak of this ObjectStorageRecord.


        :param s3_lb_system_user_ak: The s3_lb_system_user_ak of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._s3_lb_system_user_ak = s3_lb_system_user_ak

    @property
    def s3_lb_system_user_sk(self):
        """Gets the s3_lb_system_user_sk of this ObjectStorageRecord.  # noqa: E501


        :return: The s3_lb_system_user_sk of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._s3_lb_system_user_sk

    @s3_lb_system_user_sk.setter
    def s3_lb_system_user_sk(self, s3_lb_system_user_sk):
        """Sets the s3_lb_system_user_sk of this ObjectStorageRecord.


        :param s3_lb_system_user_sk: The s3_lb_system_user_sk of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._s3_lb_system_user_sk = s3_lb_system_user_sk

    @property
    def search_enabled(self):
        """Gets the search_enabled of this ObjectStorageRecord.  # noqa: E501


        :return: The search_enabled of this ObjectStorageRecord.  # noqa: E501
        :rtype: bool
        """
        return self._search_enabled

    @search_enabled.setter
    def search_enabled(self, search_enabled):
        """Sets the search_enabled of this ObjectStorageRecord.


        :param search_enabled: The search_enabled of this ObjectStorageRecord.  # noqa: E501
        :type: bool
        """

        self._search_enabled = search_enabled

    @property
    def second_mergence_enabled(self):
        """Gets the second_mergence_enabled of this ObjectStorageRecord.  # noqa: E501


        :return: The second_mergence_enabled of this ObjectStorageRecord.  # noqa: E501
        :rtype: bool
        """
        return self._second_mergence_enabled

    @second_mergence_enabled.setter
    def second_mergence_enabled(self, second_mergence_enabled):
        """Sets the second_mergence_enabled of this ObjectStorageRecord.


        :param second_mergence_enabled: The second_mergence_enabled of this ObjectStorageRecord.  # noqa: E501
        :type: bool
        """

        self._second_mergence_enabled = second_mergence_enabled

    @property
    def second_mergence_end_on(self):
        """Gets the second_mergence_end_on of this ObjectStorageRecord.  # noqa: E501


        :return: The second_mergence_end_on of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._second_mergence_end_on

    @second_mergence_end_on.setter
    def second_mergence_end_on(self, second_mergence_end_on):
        """Sets the second_mergence_end_on of this ObjectStorageRecord.


        :param second_mergence_end_on: The second_mergence_end_on of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._second_mergence_end_on = second_mergence_end_on

    @property
    def second_mergence_start_on(self):
        """Gets the second_mergence_start_on of this ObjectStorageRecord.  # noqa: E501


        :return: The second_mergence_start_on of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._second_mergence_start_on

    @second_mergence_start_on.setter
    def second_mergence_start_on(self, second_mergence_start_on):
        """Sets the second_mergence_start_on of this ObjectStorageRecord.


        :param second_mergence_start_on: The second_mergence_start_on of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._second_mergence_start_on = second_mergence_start_on

    @property
    def status(self):
        """Gets the status of this ObjectStorageRecord.  # noqa: E501


        :return: The status of this ObjectStorageRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ObjectStorageRecord.


        :param status: The status of this ObjectStorageRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tiering_host_ids(self):
        """Gets the tiering_host_ids of this ObjectStorageRecord.  # noqa: E501


        :return: The tiering_host_ids of this ObjectStorageRecord.  # noqa: E501
        :rtype: list[int]
        """
        return self._tiering_host_ids

    @tiering_host_ids.setter
    def tiering_host_ids(self, tiering_host_ids):
        """Sets the tiering_host_ids of this ObjectStorageRecord.


        :param tiering_host_ids: The tiering_host_ids of this ObjectStorageRecord.  # noqa: E501
        :type: list[int]
        """

        self._tiering_host_ids = tiering_host_ids

    @property
    def update(self):
        """Gets the update of this ObjectStorageRecord.  # noqa: E501


        :return: The update of this ObjectStorageRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this ObjectStorageRecord.


        :param update: The update of this ObjectStorageRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def samples(self):
        """Gets the samples of this ObjectStorageRecord.  # noqa: E501


        :return: The samples of this ObjectStorageRecord.  # noqa: E501
        :rtype: list[ObjectStorageStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this ObjectStorageRecord.


        :param samples: The samples of this ObjectStorageRecord.  # noqa: E501
        :type: list[ObjectStorageStat]
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
        if not isinstance(other, ObjectStorageRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
