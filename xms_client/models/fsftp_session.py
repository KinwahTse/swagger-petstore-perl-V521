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
# from xms_client.models.fsftp_share_nestview import FSFTPShareNestview  # noqa: F401,E501


class FSFTPSession(object):
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
        'client_ip': 'str',
        'client_port': 'int',
        'cluster': 'ClusterNestview',
        'connected_at': 'datetime',
        'create': 'datetime',
        'fs_ftp_share': 'FSFTPShareNestview',
        'id': 'int',
        'update': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'client_port': 'client_port',
        'cluster': 'cluster',
        'connected_at': 'connected_at',
        'create': 'create',
        'fs_ftp_share': 'fs_ftp_share',
        'id': 'id',
        'update': 'update',
        'username': 'username'
    }

    def __init__(self, client_ip=None, client_port=None, cluster=None, connected_at=None, create=None, fs_ftp_share=None, id=None, update=None, username=None):  # noqa: E501
        """FSFTPSession - a model defined in Swagger"""  # noqa: E501

        self._client_ip = None
        self._client_port = None
        self._cluster = None
        self._connected_at = None
        self._create = None
        self._fs_ftp_share = None
        self._id = None
        self._update = None
        self._username = None
        self.discriminator = None

        if client_ip is not None:
            self.client_ip = client_ip
        if client_port is not None:
            self.client_port = client_port
        if cluster is not None:
            self.cluster = cluster
        if connected_at is not None:
            self.connected_at = connected_at
        if create is not None:
            self.create = create
        if fs_ftp_share is not None:
            self.fs_ftp_share = fs_ftp_share
        if id is not None:
            self.id = id
        if update is not None:
            self.update = update
        if username is not None:
            self.username = username

    @property
    def client_ip(self):
        """Gets the client_ip of this FSFTPSession.  # noqa: E501


        :return: The client_ip of this FSFTPSession.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this FSFTPSession.


        :param client_ip: The client_ip of this FSFTPSession.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def client_port(self):
        """Gets the client_port of this FSFTPSession.  # noqa: E501


        :return: The client_port of this FSFTPSession.  # noqa: E501
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        """Sets the client_port of this FSFTPSession.


        :param client_port: The client_port of this FSFTPSession.  # noqa: E501
        :type: int
        """

        self._client_port = client_port

    @property
    def cluster(self):
        """Gets the cluster of this FSFTPSession.  # noqa: E501


        :return: The cluster of this FSFTPSession.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this FSFTPSession.


        :param cluster: The cluster of this FSFTPSession.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def connected_at(self):
        """Gets the connected_at of this FSFTPSession.  # noqa: E501


        :return: The connected_at of this FSFTPSession.  # noqa: E501
        :rtype: datetime
        """
        return self._connected_at

    @connected_at.setter
    def connected_at(self, connected_at):
        """Sets the connected_at of this FSFTPSession.


        :param connected_at: The connected_at of this FSFTPSession.  # noqa: E501
        :type: datetime
        """

        self._connected_at = connected_at

    @property
    def create(self):
        """Gets the create of this FSFTPSession.  # noqa: E501


        :return: The create of this FSFTPSession.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this FSFTPSession.


        :param create: The create of this FSFTPSession.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def fs_ftp_share(self):
        """Gets the fs_ftp_share of this FSFTPSession.  # noqa: E501


        :return: The fs_ftp_share of this FSFTPSession.  # noqa: E501
        :rtype: FSFTPShareNestview
        """
        return self._fs_ftp_share

    @fs_ftp_share.setter
    def fs_ftp_share(self, fs_ftp_share):
        """Sets the fs_ftp_share of this FSFTPSession.


        :param fs_ftp_share: The fs_ftp_share of this FSFTPSession.  # noqa: E501
        :type: FSFTPShareNestview
        """

        self._fs_ftp_share = fs_ftp_share

    @property
    def id(self):
        """Gets the id of this FSFTPSession.  # noqa: E501


        :return: The id of this FSFTPSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FSFTPSession.


        :param id: The id of this FSFTPSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def update(self):
        """Gets the update of this FSFTPSession.  # noqa: E501


        :return: The update of this FSFTPSession.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FSFTPSession.


        :param update: The update of this FSFTPSession.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def username(self):
        """Gets the username of this FSFTPSession.  # noqa: E501


        :return: The username of this FSFTPSession.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this FSFTPSession.


        :param username: The username of this FSFTPSession.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, FSFTPSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
