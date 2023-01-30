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

# from xms_client.models.alert_info import AlertInfo  # noqa: F401,E501


class AlertInfoGroup(object):
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
        'alert_info': 'AlertInfo',
        'create': 'datetime',
        'group': 'str',
        'id': 'int',
        'resource_id': 'int',
        'resource_type': 'str',
        'status': 'str',
        'update': 'datetime'
    }

    attribute_map = {
        'alert_info': 'alert_info',
        'create': 'create',
        'group': 'group',
        'id': 'id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'status': 'status',
        'update': 'update'
    }

    def __init__(self, alert_info=None, create=None, group=None, id=None, resource_id=None, resource_type=None, status=None, update=None):  # noqa: E501
        """AlertInfoGroup - a model defined in Swagger"""  # noqa: E501

        self._alert_info = None
        self._create = None
        self._group = None
        self._id = None
        self._resource_id = None
        self._resource_type = None
        self._status = None
        self._update = None
        self.discriminator = None

        if alert_info is not None:
            self.alert_info = alert_info
        if create is not None:
            self.create = create
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update

    @property
    def alert_info(self):
        """Gets the alert_info of this AlertInfoGroup.  # noqa: E501


        :return: The alert_info of this AlertInfoGroup.  # noqa: E501
        :rtype: AlertInfo
        """
        return self._alert_info

    @alert_info.setter
    def alert_info(self, alert_info):
        """Sets the alert_info of this AlertInfoGroup.


        :param alert_info: The alert_info of this AlertInfoGroup.  # noqa: E501
        :type: AlertInfo
        """

        self._alert_info = alert_info

    @property
    def create(self):
        """Gets the create of this AlertInfoGroup.  # noqa: E501


        :return: The create of this AlertInfoGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this AlertInfoGroup.


        :param create: The create of this AlertInfoGroup.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def group(self):
        """Gets the group of this AlertInfoGroup.  # noqa: E501


        :return: The group of this AlertInfoGroup.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AlertInfoGroup.


        :param group: The group of this AlertInfoGroup.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def id(self):
        """Gets the id of this AlertInfoGroup.  # noqa: E501


        :return: The id of this AlertInfoGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertInfoGroup.


        :param id: The id of this AlertInfoGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this AlertInfoGroup.  # noqa: E501


        :return: The resource_id of this AlertInfoGroup.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AlertInfoGroup.


        :param resource_id: The resource_id of this AlertInfoGroup.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this AlertInfoGroup.  # noqa: E501


        :return: The resource_type of this AlertInfoGroup.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AlertInfoGroup.


        :param resource_type: The resource_type of this AlertInfoGroup.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this AlertInfoGroup.  # noqa: E501


        :return: The status of this AlertInfoGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertInfoGroup.


        :param status: The status of this AlertInfoGroup.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this AlertInfoGroup.  # noqa: E501


        :return: The update of this AlertInfoGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this AlertInfoGroup.


        :param update: The update of this AlertInfoGroup.  # noqa: E501
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
        if not isinstance(other, AlertInfoGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
