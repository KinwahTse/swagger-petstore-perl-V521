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
# from xms_client.models.object_storage_policy import ObjectStoragePolicy  # noqa: F401,E501


class OSStorageClass(object):
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
        'active_pool_ids': 'list[int]',
        'class_id': 'str',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'description': 'str',
        'id': 'int',
        'inactive_pool_ids': 'list[int]',
        'name': 'str',
        'os_policy': 'ObjectStoragePolicy',
        'os_policy_id': 'int',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'active_pool_ids': 'active_pool_ids',
        'class_id': 'class_id',
        'cluster': 'cluster',
        'create': 'create',
        'description': 'description',
        'id': 'id',
        'inactive_pool_ids': 'inactive_pool_ids',
        'name': 'name',
        'os_policy': 'os_policy',
        'os_policy_id': 'os_policy_id',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, active_pool_ids=None, class_id=None, cluster=None, create=None, description=None, id=None, inactive_pool_ids=None, name=None, os_policy=None, os_policy_id=None, status=None, update=None):  # noqa: E501
        """OSStorageClass - a model defined in Swagger"""  # noqa: E501

        self._active_pool_ids = None
        self._class_id = None
        self._cluster = None
        self._create = None
        self._description = None
        self._id = None
        self._inactive_pool_ids = None
        self._name = None
        self._os_policy = None
        self._os_policy_id = None
        self._status = None
        self._update = None
        self.discriminator = None

        if active_pool_ids is not None:
            self.active_pool_ids = active_pool_ids
        if class_id is not None:
            self.class_id = class_id
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if inactive_pool_ids is not None:
            self.inactive_pool_ids = inactive_pool_ids
        if name is not None:
            self.name = name
        if os_policy is not None:
            self.os_policy = os_policy
        if os_policy_id is not None:
            self.os_policy_id = os_policy_id
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def active_pool_ids(self):
        """Gets the active_pool_ids of this OSStorageClass.  # noqa: E501


        :return: The active_pool_ids of this OSStorageClass.  # noqa: E501
        :rtype: list[int]
        """
        return self._active_pool_ids

    @active_pool_ids.setter
    def active_pool_ids(self, active_pool_ids):
        """Sets the active_pool_ids of this OSStorageClass.


        :param active_pool_ids: The active_pool_ids of this OSStorageClass.  # noqa: E501
        :type: list[int]
        """

        self._active_pool_ids = active_pool_ids

    @property
    def class_id(self):
        """Gets the class_id of this OSStorageClass.  # noqa: E501


        :return: The class_id of this OSStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this OSStorageClass.


        :param class_id: The class_id of this OSStorageClass.  # noqa: E501
        :type: str
        """

        self._class_id = class_id

    @property
    def cluster(self):
        """Gets the cluster of this OSStorageClass.  # noqa: E501


        :return: The cluster of this OSStorageClass.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this OSStorageClass.


        :param cluster: The cluster of this OSStorageClass.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this OSStorageClass.  # noqa: E501


        :return: The create of this OSStorageClass.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OSStorageClass.


        :param create: The create of this OSStorageClass.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this OSStorageClass.  # noqa: E501


        :return: The description of this OSStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OSStorageClass.


        :param description: The description of this OSStorageClass.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this OSStorageClass.  # noqa: E501


        :return: The id of this OSStorageClass.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OSStorageClass.


        :param id: The id of this OSStorageClass.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def inactive_pool_ids(self):
        """Gets the inactive_pool_ids of this OSStorageClass.  # noqa: E501


        :return: The inactive_pool_ids of this OSStorageClass.  # noqa: E501
        :rtype: list[int]
        """
        return self._inactive_pool_ids

    @inactive_pool_ids.setter
    def inactive_pool_ids(self, inactive_pool_ids):
        """Sets the inactive_pool_ids of this OSStorageClass.


        :param inactive_pool_ids: The inactive_pool_ids of this OSStorageClass.  # noqa: E501
        :type: list[int]
        """

        self._inactive_pool_ids = inactive_pool_ids

    @property
    def name(self):
        """Gets the name of this OSStorageClass.  # noqa: E501


        :return: The name of this OSStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OSStorageClass.


        :param name: The name of this OSStorageClass.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os_policy(self):
        """Gets the os_policy of this OSStorageClass.  # noqa: E501


        :return: The os_policy of this OSStorageClass.  # noqa: E501
        :rtype: ObjectStoragePolicy
        """
        return self._os_policy

    @os_policy.setter
    def os_policy(self, os_policy):
        """Sets the os_policy of this OSStorageClass.


        :param os_policy: The os_policy of this OSStorageClass.  # noqa: E501
        :type: ObjectStoragePolicy
        """

        self._os_policy = os_policy

    @property
    def os_policy_id(self):
        """Gets the os_policy_id of this OSStorageClass.  # noqa: E501


        :return: The os_policy_id of this OSStorageClass.  # noqa: E501
        :rtype: int
        """
        return self._os_policy_id

    @os_policy_id.setter
    def os_policy_id(self, os_policy_id):
        """Sets the os_policy_id of this OSStorageClass.


        :param os_policy_id: The os_policy_id of this OSStorageClass.  # noqa: E501
        :type: int
        """

        self._os_policy_id = os_policy_id

    @property
    def status(self):
        """Gets the status of this OSStorageClass.  # noqa: E501


        :return: The status of this OSStorageClass.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OSStorageClass.


        :param status: The status of this OSStorageClass.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this OSStorageClass.  # noqa: E501


        :return: The update of this OSStorageClass.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this OSStorageClass.


        :param update: The update of this OSStorageClass.  # noqa: E501
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
        if not isinstance(other, OSStorageClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
