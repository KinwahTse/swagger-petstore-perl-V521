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

# from xms_client.models.osd_group import OsdGroup  # noqa: F401,E501
# from xms_client.models.osd_group_stat import OsdGroupStat  # noqa: F401,E501
# from xms_client.models.osd_qos import OsdQos  # noqa: F401,E501
# from xms_client.models.pool_nestview import PoolNestview  # noqa: F401,E501


class OsdGroupRecord(object):
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
        'create': 'datetime',
        'device_type': 'str',
        'device_type_check_disabled': 'bool',
        'failure_domain_type': 'str',
        'id': 'int',
        'numa_bind_policy': 'str',
        'numa_enabled': 'bool',
        'osd_async_recovery_max_updates': 'int',
        'osd_full_ratio': 'float',
        'osd_num': 'int',
        'pools': 'list[PoolNestview]',
        'qos': 'OsdQos',
        'status': 'str',
        'update': 'datetime',
        'samples': 'list[OsdGroupStat]'
    }

    attribute_map = {
        'action_status': 'action_status',
        'create': 'create',
        'device_type': 'device_type',
        'device_type_check_disabled': 'device_type_check_disabled',
        'failure_domain_type': 'failure_domain_type',
        'id': 'id',
        'numa_bind_policy': 'numa_bind_policy',
        'numa_enabled': 'numa_enabled',
        'osd_async_recovery_max_updates': 'osd_async_recovery_max_updates',
        'osd_full_ratio': 'osd_full_ratio',
        'osd_num': 'osd_num',
        'pools': 'pools',
        'qos': 'qos',
        'status': 'status',
        'update': 'update',
        'samples': 'samples'
    }

    def __init__(self, action_status=None, create=None, device_type=None, device_type_check_disabled=None, failure_domain_type=None, id=None, numa_bind_policy=None, numa_enabled=None, osd_async_recovery_max_updates=None, osd_full_ratio=None, osd_num=None, pools=None, qos=None, status=None, update=None, samples=None):  # noqa: E501
        """OsdGroupRecord - a model defined in Swagger"""  # noqa: E501

        self._action_status = None
        self._create = None
        self._device_type = None
        self._device_type_check_disabled = None
        self._failure_domain_type = None
        self._id = None
        self._numa_bind_policy = None
        self._numa_enabled = None
        self._osd_async_recovery_max_updates = None
        self._osd_full_ratio = None
        self._osd_num = None
        self._pools = None
        self._qos = None
        self._status = None
        self._update = None
        self._samples = None
        self.discriminator = None

        if action_status is not None:
            self.action_status = action_status
        if create is not None:
            self.create = create
        if device_type is not None:
            self.device_type = device_type
        if device_type_check_disabled is not None:
            self.device_type_check_disabled = device_type_check_disabled
        if failure_domain_type is not None:
            self.failure_domain_type = failure_domain_type
        if id is not None:
            self.id = id
        if numa_bind_policy is not None:
            self.numa_bind_policy = numa_bind_policy
        if numa_enabled is not None:
            self.numa_enabled = numa_enabled
        if osd_async_recovery_max_updates is not None:
            self.osd_async_recovery_max_updates = osd_async_recovery_max_updates
        if osd_full_ratio is not None:
            self.osd_full_ratio = osd_full_ratio
        if osd_num is not None:
            self.osd_num = osd_num
        if pools is not None:
            self.pools = pools
        if qos is not None:
            self.qos = qos
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if samples is not None:
            self.samples = samples

    @property
    def action_status(self):
        """Gets the action_status of this OsdGroupRecord.  # noqa: E501


        :return: The action_status of this OsdGroupRecord.  # noqa: E501
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        """Sets the action_status of this OsdGroupRecord.


        :param action_status: The action_status of this OsdGroupRecord.  # noqa: E501
        :type: str
        """

        self._action_status = action_status

    @property
    def create(self):
        """Gets the create of this OsdGroupRecord.  # noqa: E501


        :return: The create of this OsdGroupRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this OsdGroupRecord.


        :param create: The create of this OsdGroupRecord.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def device_type(self):
        """Gets the device_type of this OsdGroupRecord.  # noqa: E501


        :return: The device_type of this OsdGroupRecord.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this OsdGroupRecord.


        :param device_type: The device_type of this OsdGroupRecord.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def device_type_check_disabled(self):
        """Gets the device_type_check_disabled of this OsdGroupRecord.  # noqa: E501


        :return: The device_type_check_disabled of this OsdGroupRecord.  # noqa: E501
        :rtype: bool
        """
        return self._device_type_check_disabled

    @device_type_check_disabled.setter
    def device_type_check_disabled(self, device_type_check_disabled):
        """Sets the device_type_check_disabled of this OsdGroupRecord.


        :param device_type_check_disabled: The device_type_check_disabled of this OsdGroupRecord.  # noqa: E501
        :type: bool
        """

        self._device_type_check_disabled = device_type_check_disabled

    @property
    def failure_domain_type(self):
        """Gets the failure_domain_type of this OsdGroupRecord.  # noqa: E501


        :return: The failure_domain_type of this OsdGroupRecord.  # noqa: E501
        :rtype: str
        """
        return self._failure_domain_type

    @failure_domain_type.setter
    def failure_domain_type(self, failure_domain_type):
        """Sets the failure_domain_type of this OsdGroupRecord.


        :param failure_domain_type: The failure_domain_type of this OsdGroupRecord.  # noqa: E501
        :type: str
        """

        self._failure_domain_type = failure_domain_type

    @property
    def id(self):
        """Gets the id of this OsdGroupRecord.  # noqa: E501


        :return: The id of this OsdGroupRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OsdGroupRecord.


        :param id: The id of this OsdGroupRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def numa_bind_policy(self):
        """Gets the numa_bind_policy of this OsdGroupRecord.  # noqa: E501


        :return: The numa_bind_policy of this OsdGroupRecord.  # noqa: E501
        :rtype: str
        """
        return self._numa_bind_policy

    @numa_bind_policy.setter
    def numa_bind_policy(self, numa_bind_policy):
        """Sets the numa_bind_policy of this OsdGroupRecord.


        :param numa_bind_policy: The numa_bind_policy of this OsdGroupRecord.  # noqa: E501
        :type: str
        """

        self._numa_bind_policy = numa_bind_policy

    @property
    def numa_enabled(self):
        """Gets the numa_enabled of this OsdGroupRecord.  # noqa: E501


        :return: The numa_enabled of this OsdGroupRecord.  # noqa: E501
        :rtype: bool
        """
        return self._numa_enabled

    @numa_enabled.setter
    def numa_enabled(self, numa_enabled):
        """Sets the numa_enabled of this OsdGroupRecord.


        :param numa_enabled: The numa_enabled of this OsdGroupRecord.  # noqa: E501
        :type: bool
        """

        self._numa_enabled = numa_enabled

    @property
    def osd_async_recovery_max_updates(self):
        """Gets the osd_async_recovery_max_updates of this OsdGroupRecord.  # noqa: E501


        :return: The osd_async_recovery_max_updates of this OsdGroupRecord.  # noqa: E501
        :rtype: int
        """
        return self._osd_async_recovery_max_updates

    @osd_async_recovery_max_updates.setter
    def osd_async_recovery_max_updates(self, osd_async_recovery_max_updates):
        """Sets the osd_async_recovery_max_updates of this OsdGroupRecord.


        :param osd_async_recovery_max_updates: The osd_async_recovery_max_updates of this OsdGroupRecord.  # noqa: E501
        :type: int
        """

        self._osd_async_recovery_max_updates = osd_async_recovery_max_updates

    @property
    def osd_full_ratio(self):
        """Gets the osd_full_ratio of this OsdGroupRecord.  # noqa: E501


        :return: The osd_full_ratio of this OsdGroupRecord.  # noqa: E501
        :rtype: float
        """
        return self._osd_full_ratio

    @osd_full_ratio.setter
    def osd_full_ratio(self, osd_full_ratio):
        """Sets the osd_full_ratio of this OsdGroupRecord.


        :param osd_full_ratio: The osd_full_ratio of this OsdGroupRecord.  # noqa: E501
        :type: float
        """

        self._osd_full_ratio = osd_full_ratio

    @property
    def osd_num(self):
        """Gets the osd_num of this OsdGroupRecord.  # noqa: E501


        :return: The osd_num of this OsdGroupRecord.  # noqa: E501
        :rtype: int
        """
        return self._osd_num

    @osd_num.setter
    def osd_num(self, osd_num):
        """Sets the osd_num of this OsdGroupRecord.


        :param osd_num: The osd_num of this OsdGroupRecord.  # noqa: E501
        :type: int
        """

        self._osd_num = osd_num

    @property
    def pools(self):
        """Gets the pools of this OsdGroupRecord.  # noqa: E501


        :return: The pools of this OsdGroupRecord.  # noqa: E501
        :rtype: list[PoolNestview]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this OsdGroupRecord.


        :param pools: The pools of this OsdGroupRecord.  # noqa: E501
        :type: list[PoolNestview]
        """

        self._pools = pools

    @property
    def qos(self):
        """Gets the qos of this OsdGroupRecord.  # noqa: E501


        :return: The qos of this OsdGroupRecord.  # noqa: E501
        :rtype: OsdQos
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """Sets the qos of this OsdGroupRecord.


        :param qos: The qos of this OsdGroupRecord.  # noqa: E501
        :type: OsdQos
        """

        self._qos = qos

    @property
    def status(self):
        """Gets the status of this OsdGroupRecord.  # noqa: E501


        :return: The status of this OsdGroupRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OsdGroupRecord.


        :param status: The status of this OsdGroupRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update(self):
        """Gets the update of this OsdGroupRecord.  # noqa: E501


        :return: The update of this OsdGroupRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this OsdGroupRecord.


        :param update: The update of this OsdGroupRecord.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def samples(self):
        """Gets the samples of this OsdGroupRecord.  # noqa: E501


        :return: The samples of this OsdGroupRecord.  # noqa: E501
        :rtype: list[OsdGroupStat]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this OsdGroupRecord.


        :param samples: The samples of this OsdGroupRecord.  # noqa: E501
        :type: list[OsdGroupStat]
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
        if not isinstance(other, OsdGroupRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
