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
# from xms_client.models.dfs_path_nestview import DfsPathNestview  # noqa: F401,E501
# from xms_client.models.dfs_rootfs_nestview import DfsRootfsNestview  # noqa: F401,E501
# from xms_client.models.progress_info import ProgressInfo  # noqa: F401,E501


class DfsTrash(object):
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
        'create': 'datetime',
        'expired_time': 'int',
        'id': 'int',
        'path': 'DfsPathNestview',
        'progress': 'float',
        'progress_info': 'ProgressInfo',
        'rootfs': 'DfsRootfsNestview',
        'status': 'str',
        'total_files': 'int',
        'total_kbyte': 'int',
        'update': 'datetime'
    }

    attribute_map = {
        'action_status': 'action_status',
        'cluster': 'cluster',
        'create': 'create',
        'expired_time': 'expired_time',
        'id': 'id',
        'path': 'path',
        'progress': 'progress',
        'progress_info': 'progress_info',
        'rootfs': 'rootfs',
        'status': 'status',
        'total_files': 'total_files',
        'total_kbyte': 'total_kbyte',
        'update': 'update'
    }

    def __init__(self, action_status=None, cluster=None, create=None, expired_time=None, id=None, path=None, progress=None, progress_info=None, rootfs=None, status=None, total_files=None, total_kbyte=None, update=None):  # noqa: E501
        """DfsTrash - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._cluster = None
        self._create = None
        self._expired_time = None
        self._id = None
        self._path = None
        self._progress = None
        self._progress_info = None
        self._rootfs = None
        self._status = None
        self._total_files = None
        self._total_kbyte = None
        self._update = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if expired_time is not None:
            self.expired_time = expired_time
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if progress is not None:
            self.progress = progress
        if progress_info is not None:
            self.progress_info = progress_info
        if rootfs is not None:
            self.rootfs = rootfs
        if status is not None:
            self.status = status
        if total_files is not None:
            self.total_files = total_files
        if total_kbyte is not None:
            self.total_kbyte = total_kbyte
        if update is not None:
            self.update = update

    @property
    def action_status(self):
        """Gets the action_status of this DfsTrash.  # noqa: E501


        :return: The action_status of this DfsTrash.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this DfsTrash.


        :param action_status: The action_status of this DfsTrash.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def cluster(self):
        """Gets the cluster of this DfsTrash.  # noqa: E501


        :return: The cluster of this DfsTrash.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DfsTrash.


        :param cluster: The cluster of this DfsTrash.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this DfsTrash.  # noqa: E501


        :return: The create of this DfsTrash.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DfsTrash.


        :param create: The create of this DfsTrash.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def expired_time(self):
        """Gets the expired_time of this DfsTrash.  # noqa: E501


        :return: The expired_time of this DfsTrash.  # noqa: E501
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this DfsTrash.


        :param expired_time: The expired_time of this DfsTrash.  # noqa: E501
        :type: int
        """

        self._expired_time = expired_time

    @property
    def id(self):
        """Gets the id of this DfsTrash.  # noqa: E501


        :return: The id of this DfsTrash.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DfsTrash.


        :param id: The id of this DfsTrash.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this DfsTrash.  # noqa: E501


        :return: The path of this DfsTrash.  # noqa: E501
        :rtype: DfsPathNestview
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DfsTrash.


        :param path: The path of this DfsTrash.  # noqa: E501
        :type: DfsPathNestview
        """

        self._path = path

    @property
    def progress(self):
        """Gets the progress of this DfsTrash.  # noqa: E501


        :return: The progress of this DfsTrash.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DfsTrash.


        :param progress: The progress of this DfsTrash.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def progress_info(self):
        """Gets the progress_info of this DfsTrash.  # noqa: E501


        :return: The progress_info of this DfsTrash.  # noqa: E501
        :rtype: ProgressInfo
        """
        return self._progress_info

    @progress_info.setter
    def progress_info(self, progress_info):
        """Sets the progress_info of this DfsTrash.


        :param progress_info: The progress_info of this DfsTrash.  # noqa: E501
        :type: ProgressInfo
        """

        self._progress_info = progress_info

    @property
    def rootfs(self):
        """Gets the rootfs of this DfsTrash.  # noqa: E501


        :return: The rootfs of this DfsTrash.  # noqa: E501
        :rtype: DfsRootfsNestview
        """
        return self._rootfs

    @rootfs.setter
    def rootfs(self, rootfs):
        """Sets the rootfs of this DfsTrash.


        :param rootfs: The rootfs of this DfsTrash.  # noqa: E501
        :type: DfsRootfsNestview
        """

        self._rootfs = rootfs

    @property
    def status(self):
        """Gets the status of this DfsTrash.  # noqa: E501


        :return: The status of this DfsTrash.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DfsTrash.


        :param status: The status of this DfsTrash.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def total_files(self):
        """Gets the total_files of this DfsTrash.  # noqa: E501


        :return: The total_files of this DfsTrash.  # noqa: E501
        :rtype: int
        """
        return self._total_files

    @total_files.setter
    def total_files(self, total_files):
        """Sets the total_files of this DfsTrash.


        :param total_files: The total_files of this DfsTrash.  # noqa: E501
        :type: int
        """

        self._total_files = total_files

    @property
    def total_kbyte(self):
        """Gets the total_kbyte of this DfsTrash.  # noqa: E501


        :return: The total_kbyte of this DfsTrash.  # noqa: E501
        :rtype: int
        """
        return self._total_kbyte

    @total_kbyte.setter
    def total_kbyte(self, total_kbyte):
        """Sets the total_kbyte of this DfsTrash.


        :param total_kbyte: The total_kbyte of this DfsTrash.  # noqa: E501
        :type: int
        """

        self._total_kbyte = total_kbyte

    @property
    def update(self):
        """Gets the update of this DfsTrash.  # noqa: E501


        :return: The update of this DfsTrash.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DfsTrash.


        :param update: The update of this DfsTrash.  # noqa: E501
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
        if not isinstance(other, DfsTrash):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
