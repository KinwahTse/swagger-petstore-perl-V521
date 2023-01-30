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


class TrapReceiver(object):
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
        'id': 'int',
        'ip': 'str',
        'msg_level': 'str',
        'port': 'int',
        'update': 'datetime'
    }

    attribute_map = {
        'create': 'create',
        'id': 'id',
        'ip': 'ip',
        'msg_level': 'msg_level',
        'port': 'port',
        'update': 'update'
    }

    def __init__(self, create=None, id=None, ip=None, msg_level=None, port=None, update=None):  # noqa: E501
        """TrapReceiver - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._id = None
        self._ip = None
        self._msg_level = None
        self._port = None
        self._update = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if msg_level is not None:
            self.msg_level = msg_level
        if port is not None:
            self.port = port
        if update is not None:
            self.update = update

    @property
    def create(self):
        """Gets the create of this TrapReceiver.  # noqa: E501


        :return: The create of this TrapReceiver.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this TrapReceiver.


        :param create: The create of this TrapReceiver.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def id(self):
        """Gets the id of this TrapReceiver.  # noqa: E501


        :return: The id of this TrapReceiver.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrapReceiver.


        :param id: The id of this TrapReceiver.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this TrapReceiver.  # noqa: E501


        :return: The ip of this TrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TrapReceiver.


        :param ip: The ip of this TrapReceiver.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def msg_level(self):
        """Gets the msg_level of this TrapReceiver.  # noqa: E501


        :return: The msg_level of this TrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._msg_level

    @msg_level.setter
    def msg_level(self, msg_level):
        """Sets the msg_level of this TrapReceiver.


        :param msg_level: The msg_level of this TrapReceiver.  # noqa: E501
        :type: str
        """

        self._msg_level = msg_level

    @property
    def port(self):
        """Gets the port of this TrapReceiver.  # noqa: E501


        :return: The port of this TrapReceiver.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TrapReceiver.


        :param port: The port of this TrapReceiver.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def update(self):
        """Gets the update of this TrapReceiver.  # noqa: E501


        :return: The update of this TrapReceiver.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this TrapReceiver.


        :param update: The update of this TrapReceiver.  # noqa: E501
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
        if not isinstance(other, TrapReceiver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
