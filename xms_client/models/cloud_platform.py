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

# from xms_client.models.cloud_extra_properties import CloudExtraProperties  # noqa: F401,E501


class CloudPlatform(object):
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
        'attached_cloud_volume_num': 'int',
        'cloud_instance_num': 'int',
        'cloud_volume_num': 'int',
        'create': 'datetime',
        'description': 'str',
        'extra_properties': 'CloudExtraProperties',
        'id': 'int',
        'name': 'str',
        'related_resource_data': 'str',
        'status': 'str',
        'sync_time': 'datetime',
        'type': 'str',
        'update': 'datetime',
        'url': 'str',
        'username': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'action_status': 'action_status',
        'attached_cloud_volume_num': 'attached_cloud_volume_num',
        'cloud_instance_num': 'cloud_instance_num',
        'cloud_volume_num': 'cloud_volume_num',
        'create': 'create',
        'description': 'description',
        'extra_properties': 'extra_properties',
        'id': 'id',
        'name': 'name',
        'related_resource_data': 'related_resource_data',
        'status': 'status',
        'sync_time': 'sync_time',
        'type': 'type',
        'update': 'update',
        'url': 'url',
        'username': 'username',
        'uuid': 'uuid'
    }

    def __init__(self, action_status=None, attached_cloud_volume_num=None, cloud_instance_num=None, cloud_volume_num=None, create=None, description=None, extra_properties=None, id=None, name=None, related_resource_data=None, status=None, sync_time=None, type=None, update=None, url=None, username=None, uuid=None):  # noqa: E501
        """CloudPlatform - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._attached_cloud_volume_num = None
        self._cloud_instance_num = None
        self._cloud_volume_num = None
        self._create = None
        self._description = None
        self._extra_properties = None
        self._id = None
        self._name = None
        self._related_resource_data = None
        self._status = None
        self._sync_time = None
        self._type = None
        self._update = None
        self._url = None
        self._username = None
        self._uuid = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if attached_cloud_volume_num is not None:
            self.attached_cloud_volume_num = attached_cloud_volume_num
        if cloud_instance_num is not None:
            self.cloud_instance_num = cloud_instance_num
        if cloud_volume_num is not None:
            self.cloud_volume_num = cloud_volume_num
        if create is not None:
            self.create = create
        if description is not None:
            self.description = description
        if extra_properties is not None:
            self.extra_properties = extra_properties
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if related_resource_data is not None:
            self.related_resource_data = related_resource_data
        if status is not None:
            self.status = status
        if sync_time is not None:
            self.sync_time = sync_time
        if type is not None:
            self.type = type
        if update is not None:
            self.update = update
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username
        if uuid is not None:
            self.uuid = uuid

    @property
    def action_status(self):
        """Gets the action_status of this CloudPlatform.  # noqa: E501


        :return: The action_status of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this CloudPlatform.


        :param action_status: The action_status of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def attached_cloud_volume_num(self):
        """Gets the attached_cloud_volume_num of this CloudPlatform.  # noqa: E501


        :return: The attached_cloud_volume_num of this CloudPlatform.  # noqa: E501
        :rtype: int
        """
        return self._attached_cloud_volume_num

    @attached_cloud_volume_num.setter
    def attached_cloud_volume_num(self, attached_cloud_volume_num):
        """Sets the attached_cloud_volume_num of this CloudPlatform.


        :param attached_cloud_volume_num: The attached_cloud_volume_num of this CloudPlatform.  # noqa: E501
        :type: int
        """

        self._attached_cloud_volume_num = attached_cloud_volume_num

    @property
    def cloud_instance_num(self):
        """Gets the cloud_instance_num of this CloudPlatform.  # noqa: E501


        :return: The cloud_instance_num of this CloudPlatform.  # noqa: E501
        :rtype: int
        """
        return self._cloud_instance_num

    @cloud_instance_num.setter
    def cloud_instance_num(self, cloud_instance_num):
        """Sets the cloud_instance_num of this CloudPlatform.


        :param cloud_instance_num: The cloud_instance_num of this CloudPlatform.  # noqa: E501
        :type: int
        """

        self._cloud_instance_num = cloud_instance_num

    @property
    def cloud_volume_num(self):
        """Gets the cloud_volume_num of this CloudPlatform.  # noqa: E501


        :return: The cloud_volume_num of this CloudPlatform.  # noqa: E501
        :rtype: int
        """
        return self._cloud_volume_num

    @cloud_volume_num.setter
    def cloud_volume_num(self, cloud_volume_num):
        """Sets the cloud_volume_num of this CloudPlatform.


        :param cloud_volume_num: The cloud_volume_num of this CloudPlatform.  # noqa: E501
        :type: int
        """

        self._cloud_volume_num = cloud_volume_num

    @property
    def create(self):
        """Gets the create of this CloudPlatform.  # noqa: E501


        :return: The create of this CloudPlatform.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this CloudPlatform.


        :param create: The create of this CloudPlatform.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def description(self):
        """Gets the description of this CloudPlatform.  # noqa: E501


        :return: The description of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudPlatform.


        :param description: The description of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extra_properties(self):
        """Gets the extra_properties of this CloudPlatform.  # noqa: E501


        :return: The extra_properties of this CloudPlatform.  # noqa: E501
        :rtype: CloudExtraProperties
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this CloudPlatform.


        :param extra_properties: The extra_properties of this CloudPlatform.  # noqa: E501
        :type: CloudExtraProperties
        """

        self._extra_properties = extra_properties

    @property
    def id(self):
        """Gets the id of this CloudPlatform.  # noqa: E501


        :return: The id of this CloudPlatform.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudPlatform.


        :param id: The id of this CloudPlatform.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CloudPlatform.  # noqa: E501


        :return: The name of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudPlatform.


        :param name: The name of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def related_resource_data(self):
        """Gets the related_resource_data of this CloudPlatform.  # noqa: E501


        :return: The related_resource_data of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._related_resource_data

    @related_resource_data.setter
    def related_resource_data(self, related_resource_data):
        """Sets the related_resource_data of this CloudPlatform.


        :param related_resource_data: The related_resource_data of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._related_resource_data = related_resource_data

    @property
    def status(self):
        """Gets the status of this CloudPlatform.  # noqa: E501


        :return: The status of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudPlatform.


        :param status: The status of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sync_time(self):
        """Gets the sync_time of this CloudPlatform.  # noqa: E501


        :return: The sync_time of this CloudPlatform.  # noqa: E501
        :rtype: datetime
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        """Sets the sync_time of this CloudPlatform.


        :param sync_time: The sync_time of this CloudPlatform.  # noqa: E501
        :type: datetime
        """

        self._sync_time = sync_time

    @property
    def type(self):
        """Gets the type of this CloudPlatform.  # noqa: E501


        :return: The type of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudPlatform.


        :param type: The type of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this CloudPlatform.  # noqa: E501


        :return: The update of this CloudPlatform.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this CloudPlatform.


        :param update: The update of this CloudPlatform.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def url(self):
        """Gets the url of this CloudPlatform.  # noqa: E501


        :return: The url of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CloudPlatform.


        :param url: The url of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this CloudPlatform.  # noqa: E501


        :return: The username of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CloudPlatform.


        :param username: The username of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def uuid(self):
        """Gets the uuid of this CloudPlatform.  # noqa: E501


        :return: The uuid of this CloudPlatform.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CloudPlatform.


        :param uuid: The uuid of this CloudPlatform.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, CloudPlatform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
