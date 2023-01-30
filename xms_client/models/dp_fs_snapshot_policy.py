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

# from xms_client.models.dp_gateway_nestview import DpGatewayNestview  # noqa: F401,E501


class DpFSSnapshotPolicy(object):
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
        'create': 'datetime',
        'cron_expr': 'str',
        'dp_gateway': 'DpGatewayNestview',
        'fs_folder_num': 'int',
        'id': 'int',
        'name': 'str',
        'retained_max': 'int',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'create': 'create',
        'cron_expr': 'cron_expr',
        'dp_gateway': 'dp_gateway',
        'fs_folder_num': 'fs_folder_num',
        'id': 'id',
        'name': 'name',
        'retained_max': 'retained_max',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, create=None, cron_expr=None, dp_gateway=None, fs_folder_num=None, id=None, name=None, retained_max=None, status=None, update=None):  # noqa: E501
        """DpFSSnapshotPolicy - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._cron_expr = None
        self._dp_gateway = None
        self._fs_folder_num = None
        self._id = None
        self._name = None
        self._retained_max = None
        self._status = None
        self._update = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if cron_expr is not None:
            self.cron_expr = cron_expr
        if dp_gateway is not None:
            self.dp_gateway = dp_gateway
        if fs_folder_num is not None:
            self.fs_folder_num = fs_folder_num
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if retained_max is not None:
            self.retained_max = retained_max
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def create(self):
        """Gets the create of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The create of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this DpFSSnapshotPolicy.


        :param create: The create of this DpFSSnapshotPolicy.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def cron_expr(self):
        """Gets the cron_expr of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The cron_expr of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: str
        """
        return self._cron_expr

    @cron_expr.setter
    def cron_expr(self, cron_expr):
        """Sets the cron_expr of this DpFSSnapshotPolicy.


        :param cron_expr: The cron_expr of this DpFSSnapshotPolicy.  # noqa: E501
        :type: str
        """

        self._cron_expr = cron_expr

    @property
    def dp_gateway(self):
        """Gets the dp_gateway of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The dp_gateway of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: DpGatewayNestview
        """
        return self._dp_gateway

    @dp_gateway.setter
    def dp_gateway(self, dp_gateway):
        """Sets the dp_gateway of this DpFSSnapshotPolicy.


        :param dp_gateway: The dp_gateway of this DpFSSnapshotPolicy.  # noqa: E501
        :type: DpGatewayNestview
        """

        self._dp_gateway = dp_gateway

    @property
    def fs_folder_num(self):
        """Gets the fs_folder_num of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The fs_folder_num of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: int
        """
        return self._fs_folder_num

    @fs_folder_num.setter
    def fs_folder_num(self, fs_folder_num):
        """Sets the fs_folder_num of this DpFSSnapshotPolicy.


        :param fs_folder_num: The fs_folder_num of this DpFSSnapshotPolicy.  # noqa: E501
        :type: int
        """

        self._fs_folder_num = fs_folder_num

    @property
    def id(self):
        """Gets the id of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The id of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DpFSSnapshotPolicy.


        :param id: The id of this DpFSSnapshotPolicy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The name of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DpFSSnapshotPolicy.


        :param name: The name of this DpFSSnapshotPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def retained_max(self):
        """Gets the retained_max of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The retained_max of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: int
        """
        return self._retained_max

    @retained_max.setter
    def retained_max(self, retained_max):
        """Sets the retained_max of this DpFSSnapshotPolicy.


        :param retained_max: The retained_max of this DpFSSnapshotPolicy.  # noqa: E501
        :type: int
        """

        self._retained_max = retained_max

    @property
    def status(self):
        """Gets the status of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The status of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DpFSSnapshotPolicy.


        :param status: The status of this DpFSSnapshotPolicy.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this DpFSSnapshotPolicy.  # noqa: E501


        :return: The update of this DpFSSnapshotPolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this DpFSSnapshotPolicy.


        :param update: The update of this DpFSSnapshotPolicy.  # noqa: E501
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
        if not isinstance(other, DpFSSnapshotPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other