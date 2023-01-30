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
# from xms_client.models.host_nestview import HostNestview  # noqa: F401,E501
# from xms_client.models.vm_disk import VMDisk  # noqa: F401,E501
# from xms_client.models.vm_flavor_nestview import VMFlavorNestview  # noqa: F401,E501
# from xms_client.models.vm_image_nestview import VMImageNestview  # noqa: F401,E501
# from xms_client.models.vm_network_interface import VMNetworkInterface  # noqa: F401,E501
# from xms_client.models.volume_nestview import VolumeNestview  # noqa: F401,E501


class VirtualMachine(object):
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
        'custom_cpu': 'int',
        'disks': 'list[VMDisk]',
        'flavor': 'VMFlavorNestview',
        'host': 'HostNestview',
        'id': 'int',
        'image': 'VMImageNestview',
        'name': 'str',
        'nics': 'list[VMNetworkInterface]',
        'root_volume': 'VolumeNestview',
        'status': 'str',
        'update': 'datetime',
        'uuid': 'str',
        'vm_status': 'str'
    }

    attribute_map = {
        'action_status': 'action_status',
        'cluster': 'cluster',
        'create': 'create',
        'custom_cpu': 'custom_cpu',
        'disks': 'disks',
        'flavor': 'flavor',
        'host': 'host',
        'id': 'id',
        'image': 'image',
        'name': 'name',
        'nics': 'nics',
        'root_volume': 'root_volume',
        'status': 'status',
        'update': 'update',
        'uuid': 'uuid',
        'vm_status': 'vm_status'
    }

    def __init__(self, action_status=None, cluster=None, create=None, custom_cpu=None, disks=None, flavor=None, host=None, id=None, image=None, name=None, nics=None, root_volume=None, status=None, update=None, uuid=None, vm_status=None):  # noqa: E501
        """VirtualMachine - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._cluster = None
        self._create = None
        self._custom_cpu = None
        self._disks = None
        self._flavor = None
        self._host = None
        self._id = None
        self._image = None
        self._name = None
        self._nics = None
        self._root_volume = None
        self._status = None
        self._update = None
        self._uuid = None
        self._vm_status = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if cluster is not None:
            self.cluster = cluster
        if create is not None:
            self.create = create
        if custom_cpu is not None:
            self.custom_cpu = custom_cpu
        if disks is not None:
            self.disks = disks
        if flavor is not None:
            self.flavor = flavor
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if nics is not None:
            self.nics = nics
        if root_volume is not None:
            self.root_volume = root_volume
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if uuid is not None:
            self.uuid = uuid
        if vm_status is not None:
            self.vm_status = vm_status

    @property
    def action_status(self):
        """Gets the action_status of this VirtualMachine.  # noqa: E501


        :return: The action_status of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this VirtualMachine.


        :param action_status: The action_status of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def cluster(self):
        """Gets the cluster of this VirtualMachine.  # noqa: E501


        :return: The cluster of this VirtualMachine.  # noqa: E501
        :rtype: ClusterNestview
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this VirtualMachine.


        :param cluster: The cluster of this VirtualMachine.  # noqa: E501
        :type: ClusterNestview
        """

        self._cluster = cluster

    @property
    def create(self):
        """Gets the create of this VirtualMachine.  # noqa: E501


        :return: The create of this VirtualMachine.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this VirtualMachine.


        :param create: The create of this VirtualMachine.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def custom_cpu(self):
        """Gets the custom_cpu of this VirtualMachine.  # noqa: E501


        :return: The custom_cpu of this VirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._custom_cpu

    @custom_cpu.setter
    def custom_cpu(self, custom_cpu):
        """Sets the custom_cpu of this VirtualMachine.


        :param custom_cpu: The custom_cpu of this VirtualMachine.  # noqa: E501
        :type: int
        """

        self._custom_cpu = custom_cpu

    @property
    def disks(self):
        """Gets the disks of this VirtualMachine.  # noqa: E501


        :return: The disks of this VirtualMachine.  # noqa: E501
        :rtype: list[VMDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this VirtualMachine.


        :param disks: The disks of this VirtualMachine.  # noqa: E501
        :type: list[VMDisk]
        """

        self._disks = disks

    @property
    def flavor(self):
        """Gets the flavor of this VirtualMachine.  # noqa: E501


        :return: The flavor of this VirtualMachine.  # noqa: E501
        :rtype: VMFlavorNestview
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this VirtualMachine.


        :param flavor: The flavor of this VirtualMachine.  # noqa: E501
        :type: VMFlavorNestview
        """

        self._flavor = flavor

    @property
    def host(self):
        """Gets the host of this VirtualMachine.  # noqa: E501


        :return: The host of this VirtualMachine.  # noqa: E501
        :rtype: HostNestview
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this VirtualMachine.


        :param host: The host of this VirtualMachine.  # noqa: E501
        :type: HostNestview
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this VirtualMachine.  # noqa: E501


        :return: The id of this VirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualMachine.


        :param id: The id of this VirtualMachine.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this VirtualMachine.  # noqa: E501


        :return: The image of this VirtualMachine.  # noqa: E501
        :rtype: VMImageNestview
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VirtualMachine.


        :param image: The image of this VirtualMachine.  # noqa: E501
        :type: VMImageNestview
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this VirtualMachine.  # noqa: E501


        :return: The name of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualMachine.


        :param name: The name of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nics(self):
        """Gets the nics of this VirtualMachine.  # noqa: E501


        :return: The nics of this VirtualMachine.  # noqa: E501
        :rtype: list[VMNetworkInterface]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this VirtualMachine.


        :param nics: The nics of this VirtualMachine.  # noqa: E501
        :type: list[VMNetworkInterface]
        """

        self._nics = nics

    @property
    def root_volume(self):
        """Gets the root_volume of this VirtualMachine.  # noqa: E501


        :return: The root_volume of this VirtualMachine.  # noqa: E501
        :rtype: VolumeNestview
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this VirtualMachine.


        :param root_volume: The root_volume of this VirtualMachine.  # noqa: E501
        :type: VolumeNestview
        """

        self._root_volume = root_volume

    @property
    def status(self):
        """Gets the status of this VirtualMachine.  # noqa: E501


        :return: The status of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualMachine.


        :param status: The status of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this VirtualMachine.  # noqa: E501


        :return: The update of this VirtualMachine.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this VirtualMachine.


        :param update: The update of this VirtualMachine.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def uuid(self):
        """Gets the uuid of this VirtualMachine.  # noqa: E501


        :return: The uuid of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this VirtualMachine.


        :param uuid: The uuid of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vm_status(self):
        """Gets the vm_status of this VirtualMachine.  # noqa: E501


        :return: The vm_status of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._vm_status

    @vm_status.setter
    def vm_status(self, vm_status):
        """Sets the vm_status of this VirtualMachine.


        :param vm_status: The vm_status of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._vm_status = vm_status

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
        if not isinstance(other, VirtualMachine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other