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


class DpBlockAsyncReplicationPairCreateReqPair(object):
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
        'chain_name': 'str',
        'group_pair_id': 'int',
        'master_cluster_fs_id': 'str',
        'master_gateway': 'str',
        'master_pair_id': 'int',
        'master_pool_id': 'int',
        'master_pool_name': 'str',
        'master_volume_id': 'int',
        'master_volume_name': 'str',
        'master_volume_size': 'int',
        'master_volume_uuid': 'str',
        'policy_cron': 'str',
        'slave_gateway': 'str',
        'slave_pool_id': 'int',
        'slave_pool_name': 'str',
        'slave_volume_name': 'str'
    }

    attribute_map = {
        'chain_name': 'chain_name',
        'group_pair_id': 'group_pair_id',
        'master_cluster_fs_id': 'master_cluster_fs_id',
        'master_gateway': 'master_gateway',
        'master_pair_id': 'master_pair_id',
        'master_pool_id': 'master_pool_id',
        'master_pool_name': 'master_pool_name',
        'master_volume_id': 'master_volume_id',
        'master_volume_name': 'master_volume_name',
        'master_volume_size': 'master_volume_size',
        'master_volume_uuid': 'master_volume_uuid',
        'policy_cron': 'policy_cron',
        'slave_gateway': 'slave_gateway',
        'slave_pool_id': 'slave_pool_id',
        'slave_pool_name': 'slave_pool_name',
        'slave_volume_name': 'slave_volume_name'
    }

    def __init__(self, chain_name=None, group_pair_id=None, master_cluster_fs_id=None, master_gateway=None, master_pair_id=None, master_pool_id=None, master_pool_name=None, master_volume_id=None, master_volume_name=None, master_volume_size=None, master_volume_uuid=None, policy_cron=None, slave_gateway=None, slave_pool_id=None, slave_pool_name=None, slave_volume_name=None):  # noqa: E501
        """DpBlockAsyncReplicationPairCreateReqPair - a model defined in Swagger"""  # noqa: E501

        self._chain_name = None
        self._group_pair_id = None
        self._master_cluster_fs_id = None
        self._master_gateway = None
        self._master_pair_id = None
        self._master_pool_id = None
        self._master_pool_name = None
        self._master_volume_id = None
        self._master_volume_name = None
        self._master_volume_size = None
        self._master_volume_uuid = None
        self._policy_cron = None
        self._slave_gateway = None
        self._slave_pool_id = None
        self._slave_pool_name = None
        self._slave_volume_name = None
        self.discriminator = None

        self.chain_name = chain_name
        self.group_pair_id = group_pair_id
        self.master_cluster_fs_id = master_cluster_fs_id
        self.master_gateway = master_gateway
        self.master_pair_id = master_pair_id
        self.master_pool_id = master_pool_id
        self.master_pool_name = master_pool_name
        self.master_volume_id = master_volume_id
        self.master_volume_name = master_volume_name
        self.master_volume_size = master_volume_size
        if master_volume_uuid is not None:
            self.master_volume_uuid = master_volume_uuid
        self.policy_cron = policy_cron
        self.slave_gateway = slave_gateway
        self.slave_pool_id = slave_pool_id
        self.slave_pool_name = slave_pool_name
        self.slave_volume_name = slave_volume_name

    @property
    def chain_name(self):
        """Gets the chain_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        chain name  # noqa: E501

        :return: The chain_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._chain_name

    @chain_name.setter
    def chain_name(self, chain_name):
        """Sets the chain_name of this DpBlockAsyncReplicationPairCreateReqPair.

        chain name  # noqa: E501

        :param chain_name: The chain_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if chain_name is None:
            raise ValueError("Invalid value for `chain_name`, must not be `None`")  # noqa: E501

        self._chain_name = chain_name

    @property
    def group_pair_id(self):
        """Gets the group_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        group pair id  # noqa: E501

        :return: The group_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._group_pair_id

    @group_pair_id.setter
    def group_pair_id(self, group_pair_id):
        """Sets the group_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.

        group pair id  # noqa: E501

        :param group_pair_id: The group_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if group_pair_id is None:
            raise ValueError("Invalid value for `group_pair_id`, must not be `None`")  # noqa: E501

        self._group_pair_id = group_pair_id

    @property
    def master_cluster_fs_id(self):
        """Gets the master_cluster_fs_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master cluster fs id  # noqa: E501

        :return: The master_cluster_fs_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._master_cluster_fs_id

    @master_cluster_fs_id.setter
    def master_cluster_fs_id(self, master_cluster_fs_id):
        """Sets the master_cluster_fs_id of this DpBlockAsyncReplicationPairCreateReqPair.

        master cluster fs id  # noqa: E501

        :param master_cluster_fs_id: The master_cluster_fs_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if master_cluster_fs_id is None:
            raise ValueError("Invalid value for `master_cluster_fs_id`, must not be `None`")  # noqa: E501

        self._master_cluster_fs_id = master_cluster_fs_id

    @property
    def master_gateway(self):
        """Gets the master_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        gateway ip  # noqa: E501

        :return: The master_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._master_gateway

    @master_gateway.setter
    def master_gateway(self, master_gateway):
        """Sets the master_gateway of this DpBlockAsyncReplicationPairCreateReqPair.

        gateway ip  # noqa: E501

        :param master_gateway: The master_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if master_gateway is None:
            raise ValueError("Invalid value for `master_gateway`, must not be `None`")  # noqa: E501

        self._master_gateway = master_gateway

    @property
    def master_pair_id(self):
        """Gets the master_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master pair id  # noqa: E501

        :return: The master_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._master_pair_id

    @master_pair_id.setter
    def master_pair_id(self, master_pair_id):
        """Sets the master_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.

        master pair id  # noqa: E501

        :param master_pair_id: The master_pair_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if master_pair_id is None:
            raise ValueError("Invalid value for `master_pair_id`, must not be `None`")  # noqa: E501

        self._master_pair_id = master_pair_id

    @property
    def master_pool_id(self):
        """Gets the master_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master pool id  # noqa: E501

        :return: The master_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._master_pool_id

    @master_pool_id.setter
    def master_pool_id(self, master_pool_id):
        """Sets the master_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.

        master pool id  # noqa: E501

        :param master_pool_id: The master_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if master_pool_id is None:
            raise ValueError("Invalid value for `master_pool_id`, must not be `None`")  # noqa: E501

        self._master_pool_id = master_pool_id

    @property
    def master_pool_name(self):
        """Gets the master_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master pool name  # noqa: E501

        :return: The master_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._master_pool_name

    @master_pool_name.setter
    def master_pool_name(self, master_pool_name):
        """Sets the master_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.

        master pool name  # noqa: E501

        :param master_pool_name: The master_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if master_pool_name is None:
            raise ValueError("Invalid value for `master_pool_name`, must not be `None`")  # noqa: E501

        self._master_pool_name = master_pool_name

    @property
    def master_volume_id(self):
        """Gets the master_volume_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master volume id  # noqa: E501

        :return: The master_volume_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._master_volume_id

    @master_volume_id.setter
    def master_volume_id(self, master_volume_id):
        """Sets the master_volume_id of this DpBlockAsyncReplicationPairCreateReqPair.

        master volume id  # noqa: E501

        :param master_volume_id: The master_volume_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if master_volume_id is None:
            raise ValueError("Invalid value for `master_volume_id`, must not be `None`")  # noqa: E501

        self._master_volume_id = master_volume_id

    @property
    def master_volume_name(self):
        """Gets the master_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master volume name  # noqa: E501

        :return: The master_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._master_volume_name

    @master_volume_name.setter
    def master_volume_name(self, master_volume_name):
        """Sets the master_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.

        master volume name  # noqa: E501

        :param master_volume_name: The master_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if master_volume_name is None:
            raise ValueError("Invalid value for `master_volume_name`, must not be `None`")  # noqa: E501

        self._master_volume_name = master_volume_name

    @property
    def master_volume_size(self):
        """Gets the master_volume_size of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        volume size  # noqa: E501

        :return: The master_volume_size of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._master_volume_size

    @master_volume_size.setter
    def master_volume_size(self, master_volume_size):
        """Sets the master_volume_size of this DpBlockAsyncReplicationPairCreateReqPair.

        volume size  # noqa: E501

        :param master_volume_size: The master_volume_size of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if master_volume_size is None:
            raise ValueError("Invalid value for `master_volume_size`, must not be `None`")  # noqa: E501

        self._master_volume_size = master_volume_size

    @property
    def master_volume_uuid(self):
        """Gets the master_volume_uuid of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        master volume uuid  # noqa: E501

        :return: The master_volume_uuid of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._master_volume_uuid

    @master_volume_uuid.setter
    def master_volume_uuid(self, master_volume_uuid):
        """Sets the master_volume_uuid of this DpBlockAsyncReplicationPairCreateReqPair.

        master volume uuid  # noqa: E501

        :param master_volume_uuid: The master_volume_uuid of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """

        self._master_volume_uuid = master_volume_uuid

    @property
    def policy_cron(self):
        """Gets the policy_cron of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        policy cron  # noqa: E501

        :return: The policy_cron of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._policy_cron

    @policy_cron.setter
    def policy_cron(self, policy_cron):
        """Sets the policy_cron of this DpBlockAsyncReplicationPairCreateReqPair.

        policy cron  # noqa: E501

        :param policy_cron: The policy_cron of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if policy_cron is None:
            raise ValueError("Invalid value for `policy_cron`, must not be `None`")  # noqa: E501

        self._policy_cron = policy_cron

    @property
    def slave_gateway(self):
        """Gets the slave_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        gateway ip  # noqa: E501

        :return: The slave_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._slave_gateway

    @slave_gateway.setter
    def slave_gateway(self, slave_gateway):
        """Sets the slave_gateway of this DpBlockAsyncReplicationPairCreateReqPair.

        gateway ip  # noqa: E501

        :param slave_gateway: The slave_gateway of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if slave_gateway is None:
            raise ValueError("Invalid value for `slave_gateway`, must not be `None`")  # noqa: E501

        self._slave_gateway = slave_gateway

    @property
    def slave_pool_id(self):
        """Gets the slave_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        slave pool id  # noqa: E501

        :return: The slave_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: int
        """
        return self._slave_pool_id

    @slave_pool_id.setter
    def slave_pool_id(self, slave_pool_id):
        """Sets the slave_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.

        slave pool id  # noqa: E501

        :param slave_pool_id: The slave_pool_id of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: int
        """
        if slave_pool_id is None:
            raise ValueError("Invalid value for `slave_pool_id`, must not be `None`")  # noqa: E501

        self._slave_pool_id = slave_pool_id

    @property
    def slave_pool_name(self):
        """Gets the slave_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        slave pool name  # noqa: E501

        :return: The slave_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._slave_pool_name

    @slave_pool_name.setter
    def slave_pool_name(self, slave_pool_name):
        """Sets the slave_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.

        slave pool name  # noqa: E501

        :param slave_pool_name: The slave_pool_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if slave_pool_name is None:
            raise ValueError("Invalid value for `slave_pool_name`, must not be `None`")  # noqa: E501

        self._slave_pool_name = slave_pool_name

    @property
    def slave_volume_name(self):
        """Gets the slave_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501

        slave volume name  # noqa: E501

        :return: The slave_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :rtype: str
        """
        return self._slave_volume_name

    @slave_volume_name.setter
    def slave_volume_name(self, slave_volume_name):
        """Sets the slave_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.

        slave volume name  # noqa: E501

        :param slave_volume_name: The slave_volume_name of this DpBlockAsyncReplicationPairCreateReqPair.  # noqa: E501
        :type: str
        """
        if slave_volume_name is None:
            raise ValueError("Invalid value for `slave_volume_name`, must not be `None`")  # noqa: E501

        self._slave_volume_name = slave_volume_name

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
        if not isinstance(other, DpBlockAsyncReplicationPairCreateReqPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
