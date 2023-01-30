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

# from xms_client.models.client_group_create_req_client_group_clients_elt import ClientGroupCreateReqClientGroupClientsElt  # noqa: F401,E501


class ClientGroupCreateReqClientGroup(object):
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
        'chap': 'bool',
        'clients': 'list[ClientGroupCreateReqClientGroupClientsElt]',
        'description': 'str',
        'iname': 'str',
        'isecret': 'str',
        'name': 'str',
        'type': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'chap': 'chap',
        'clients': 'clients',
        'description': 'description',
        'iname': 'iname',
        'isecret': 'isecret',
        'name': 'name',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, chap=None, clients=None, description=None, iname=None, isecret=None, name=None, type=None, uid=None):  # noqa: E501
        """ClientGroupCreateReqClientGroup - a model defined in Swagger"""  # noqa: E501

        self._chap = None
        self._clients = None
        self._description = None
        self._iname = None
        self._isecret = None
        self._name = None
        self._type = None
        self._uid = None
        self.discriminator = None

        if chap is not None:
            self.chap = chap
        if clients is not None:
            self.clients = clients
        if description is not None:
            self.description = description
        if iname is not None:
            self.iname = iname
        if isecret is not None:
            self.isecret = isecret
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid

    @property
    def chap(self):
        """Gets the chap of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The chap of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: bool
        """
        return self._chap

    @chap.setter
    def chap(self, chap):
        """Sets the chap of this ClientGroupCreateReqClientGroup.


        :param chap: The chap of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: bool
        """

        self._chap = chap

    @property
    def clients(self):
        """Gets the clients of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The clients of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: list[ClientGroupCreateReqClientGroupClientsElt]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ClientGroupCreateReqClientGroup.


        :param clients: The clients of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: list[ClientGroupCreateReqClientGroupClientsElt]
        """

        self._clients = clients

    @property
    def description(self):
        """Gets the description of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The description of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClientGroupCreateReqClientGroup.


        :param description: The description of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def iname(self):
        """Gets the iname of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The iname of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._iname

    @iname.setter
    def iname(self, iname):
        """Sets the iname of this ClientGroupCreateReqClientGroup.


        :param iname: The iname of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._iname = iname

    @property
    def isecret(self):
        """Gets the isecret of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The isecret of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._isecret

    @isecret.setter
    def isecret(self, isecret):
        """Sets the isecret of this ClientGroupCreateReqClientGroup.


        :param isecret: The isecret of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._isecret = isecret

    @property
    def name(self):
        """Gets the name of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The name of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientGroupCreateReqClientGroup.


        :param name: The name of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The type of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientGroupCreateReqClientGroup.


        :param type: The type of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this ClientGroupCreateReqClientGroup.  # noqa: E501


        :return: The uid of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ClientGroupCreateReqClientGroup.


        :param uid: The uid of this ClientGroupCreateReqClientGroup.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, ClientGroupCreateReqClientGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other