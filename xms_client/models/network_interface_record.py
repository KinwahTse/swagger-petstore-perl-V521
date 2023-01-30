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

# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.network_interface import NetworkInterface  # noqa: F401,E501
# from xms_client.models.network_interface_nestview import NetworkInterfaceNestview  # noqa: F401,E501
# from xms_client.models.network_interface_stat import NetworkInterfaceStat  # noqa: F401,E501


class NetworkInterfaceRecord(object):
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
        'bonding_mode': 'str',
        'create': 'datetime',
        'host': 'HostNestview',
        'id': 'int',
        'link_detected': 'bool',
        'mac_address': 'str',
        'master_network_interface': 'NetworkInterfaceNestview',
        'megabits': 'int',
        'name': 'str',
        'operstate': 'str',
        'type': 'str',
        'update': 'datetime',
        'vf_num': 'int',
        'samples': 'list[NetworkInterfaceStat]'
    }

    attribute_map = {
        'bonding_mode': 'bonding_mode',
        'create': 'create',
        'host': 'host',
        'id': 'id',
        'link_detected': 'link_detected',
        'mac_address': 'mac_address',
        'master_network_interface': 'master_network_interface',
        'megabits': 'megabits',
        'name': 'name',
        'operstate': 'operstate',
        'type': 'type',
        'update': 'update',
        'vf_num': 'vf_num',
        'samples': 'samples'
    }

    def __init__(self, bonding_mode=None, create=None, host=None, id=None, link_detected=None, mac_address=None, master_network_interface=None, megabits=None, name=None, operstate=None, type=None, update=None, vf_num=None, samples=None):  # noqa: E501
        """NetworkInterfaceRecord - a model defined in Swagger"""  # noqa: E501

        self._bonding_mode = None
        self._create = None
        self._host = None
        self._id = None
        self._link_detected = None
        self._mac_address = None
        self._master_network_interface = None
        self._megabits = None
        self._name = None
        self._operstate = None
        self._type = None
        self._update = None
        self._vf_num = None
        self._samples = None
        self.discriminator = None

        if bonding_mode is not None:
            self.bonding_mode = bonding_mode
        if create is not None:
            self.create = create
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if link_detected is not None:
            self.link_detected = link_detected
        if mac_address is not None:
            self.mac_address = mac_address
        if master_network_interface is not None:
            self.master_network_interface = master_network_interface
        if megabits is not None:
            self.megabits = megabits
        if name is not None:
            self.name = name
        if operstate is not None:
            self.operstate = operstate
        if type is not None:
            self.type = type
        if update is not None:
            self.update = update
        if vf_num is not None:
            self.vf_num = vf_num
        if samples is not None:
            self.samples = samples

    @property
    def bonding_mode(self):
        """Gets the bonding_mode of this NetworkInterfaceRecord.  # noqa: E501


        :return: The bonding_mode of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: str
        """
        return self._bonding_mode

    @bonding_mode.setter
    def bonding_mode(self, bonding_mode):
        """Sets the bonding_mode of this NetworkInterfaceRecord.


        :param bonding_mode: The bonding_mode of this NetworkInterfaceRecord.  # noqa: E501
        :type: str
        """

        self._bonding_mode = bonding_mode

    @property
    def create(self):
        """Gets the create of this NetworkInterfaceRecord.  # noqa: E501


        :return: The create of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this NetworkInterfaceRecord.


        :param create: The create of this NetworkInterfaceRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def host(self):
        """Gets the host of this NetworkInterfaceRecord.  # noqa: E501


        :return: The host of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this NetworkInterfaceRecord.


        :param host: The host of this NetworkInterfaceRecord.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this NetworkInterfaceRecord.  # noqa: E501


        :return: The id of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkInterfaceRecord.


        :param id: The id of this NetworkInterfaceRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def link_detected(self):
        """Gets the link_detected of this NetworkInterfaceRecord.  # noqa: E501


        :return: The link_detected of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: bool
        """
        return self._link_detected

    @link_detected.setter
    def link_detected(self, link_detected):
        """Sets the link_detected of this NetworkInterfaceRecord.


        :param link_detected: The link_detected of this NetworkInterfaceRecord.  # noqa: E501
        :type: bool
        """

        self._link_detected = link_detected

    @property
    def mac_address(self):
        """Gets the mac_address of this NetworkInterfaceRecord.  # noqa: E501


        :return: The mac_address of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetworkInterfaceRecord.


        :param mac_address: The mac_address of this NetworkInterfaceRecord.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def master_network_interface(self):
        """Gets the master_network_interface of this NetworkInterfaceRecord.  # noqa: E501


        :return: The master_network_interface of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: NetworkInterfaceNestview
        """
        return self._master_network_interface

    @master_network_interface.setter
    def master_network_interface(self, master_network_interface):
        """Sets the master_network_interface of this NetworkInterfaceRecord.


        :param master_network_interface: The master_network_interface of this NetworkInterfaceRecord.  # noqa: E501
        :type: NetworkInterfaceNestview
        """

        self._master_network_interface = master_network_interface

    @property
    def megabits(self):
        """Gets the megabits of this NetworkInterfaceRecord.  # noqa: E501


        :return: The megabits of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: int
        """
        return self._megabits

    @megabits.setter
    def megabits(self, megabits):
        """Sets the megabits of this NetworkInterfaceRecord.


        :param megabits: The megabits of this NetworkInterfaceRecord.  # noqa: E501
        :type: int
        """

        self._megabits = megabits

    @property
    def name(self):
        """Gets the name of this NetworkInterfaceRecord.  # noqa: E501


        :return: The name of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkInterfaceRecord.


        :param name: The name of this NetworkInterfaceRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def operstate(self):
        """Gets the operstate of this NetworkInterfaceRecord.  # noqa: E501


        :return: The operstate of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: str
        """
        return self._operstate

    @operstate.setter
    def operstate(self, operstate):
        """Sets the operstate of this NetworkInterfaceRecord.


        :param operstate: The operstate of this NetworkInterfaceRecord.  # noqa: E501
        :type: str
        """

        self._operstate = operstate

    @property
    def type(self):
        """Gets the type of this NetworkInterfaceRecord.  # noqa: E501

        ethernet or bond  # noqa: E501

        :return: The type of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkInterfaceRecord.

        ethernet or bond  # noqa: E501

        :param type: The type of this NetworkInterfaceRecord.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this NetworkInterfaceRecord.  # noqa: E501


        :return: The update of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this NetworkInterfaceRecord.


        :param update: The update of this NetworkInterfaceRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def vf_num(self):
        """Gets the vf_num of this NetworkInterfaceRecord.  # noqa: E501


        :return: The vf_num of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: int
        """
        return self._vf_num

    @vf_num.setter
    def vf_num(self, vf_num):
        """Sets the vf_num of this NetworkInterfaceRecord.


        :param vf_num: The vf_num of this NetworkInterfaceRecord.  # noqa: E501
        :type: int
        """

        self._vf_num = vf_num

    @property
    def samples(self):
        """Gets the samples of this NetworkInterfaceRecord.  # noqa: E501


        :return: The samples of this NetworkInterfaceRecord.  # noqa: E501
        :rtype: list[NetworkInterfaceStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this NetworkInterfaceRecord.


        :param samples: The samples of this NetworkInterfaceRecord.  # noqa: E501
        :type: list[NetworkInterfaceStat]
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
        if not isinstance(other, NetworkInterfaceRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
