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
# from xms_client.models.fs_user_nestview import FSUserNestview  # noqa: F401,E501


class DfsS3Key(object):
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
        'access_key': 'str',
        'cluster': 'ClusterNestview',
        'create': 'datetime',
        'id': 'int',
        'secret_key': 'str',
        'status': 'str',
        'update': 'datetime',
        'user': 'FSUserNestview'
    }

    attribute_map = {
        'access_key': 'access_key',
        'cluster': 'cluster',
        'create': 'create',
        'id': 'id',
        'secret_key': 'secret_key',
        'status': 'status',
        'update': 'update',
        'user': 'user'
    }

    def __init__(self, access_key=None, cluster=None, create=None, id=None, secret_key=None, status=None, update=None, user=None):  # noqa: E501
        """DfsS3Key - a model defined in Swagger"""  # noqa: E501

        self._access_key = None
        self._cluster = None
        self._create = None
        self._id = None
        self._secret_key = None
        self._status = None
        self._update = None
        self._user = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if secret_key is not None:
            self.secret_key = secret_key
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if user is not None:
            self.user = user

    @property
    def access_key(self):
        """Gets the access_key of this DfsS3Key.  # noqa: E501


        :return: The access_key of this DfsS3Key.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this DfsS3Key.


        :param access_key: The access_key of this DfsS3Key.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def cluster(self):
        """Gets the cluster of this DfsS3Key.  # noqa: E501


        :return: The cluster of this DfsS3Key.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsS3Key.


        :param cluster: The cluster of this DfsS3Key.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsS3Key.  # noqa: E501


        :return: The create of this DfsS3Key.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsS3Key.


        :param create: The create of this DfsS3Key.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this DfsS3Key.  # noqa: E501


        :return: The id of this DfsS3Key.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsS3Key.


        :param id: The id of this DfsS3Key.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def secret_key(self):
        """Gets the secret_key of this DfsS3Key.  # noqa: E501


        :return: The secret_key of this DfsS3Key.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this DfsS3Key.


        :param secret_key: The secret_key of this DfsS3Key.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def status(self):
        """Gets the status of this DfsS3Key.  # noqa: E501


        :return: The status of this DfsS3Key.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DfsS3Key.


        :param status: The status of this DfsS3Key.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this DfsS3Key.  # noqa: E501


        :return: The update of this DfsS3Key.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsS3Key.


        :param update: The update of this DfsS3Key.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def user(self):
        """Gets the user of this DfsS3Key.  # noqa: E501


        :return: The user of this DfsS3Key.  # noqa: E501
        :rtype: FSUserNestview
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DfsS3Key.


        :param user: The user of this DfsS3Key.  # noqa: E501
        :type: FSUserNestview
        """

        self._user = user

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
        if not isinstance(other, DfsS3Key):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
