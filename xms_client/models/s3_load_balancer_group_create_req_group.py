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

# from xms_client.models.s3_lb_group_web_service_config import S3LbGroupWebServiceConfig  # noqa: F401,E501
# from xms_client.models.s3_load_balancer_group_create_req_group_load_balancers_elt import S3LoadBalancerGroupCreateReqGroupLoadBalancersElt  # noqa: F401,E501


class S3LoadBalancerGroupCreateReqGroup(object):
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
        'description': 'str',
        'https_port': 'int',
        'name': 'str',
        'oss_api_enabled': 'bool',
        'port': 'int',
        'roles': 'list[str]',
        's3_load_balancers': 'list[S3LoadBalancerGroupCreateReqGroupLoadBalancersElt]',
        'search_https_port': 'int',
        'search_port': 'int',
        'sync_port': 'int',
        'web_service_config': 'S3LbGroupWebServiceConfig',
        'web_service_port': 'int'
    }

    attribute_map = {
        'description': 'description',
        'https_port': 'https_port',
        'name': 'name',
        'oss_api_enabled': 'oss_api_enabled',
        'port': 'port',
        'roles': 'roles',
        's3_load_balancers': 's3_load_balancers',
        'search_https_port': 'search_https_port',
        'search_port': 'search_port',
        'sync_port': 'sync_port',
        'web_service_config': 'web_service_config',
        'web_service_port': 'web_service_port'
    }

    def __init__(self, description=None, https_port=None, name=None, oss_api_enabled=None, port=None, roles=None, s3_load_balancers=None, search_https_port=None, search_port=None, sync_port=None, web_service_config=None, web_service_port=None):  # noqa: E501
        """S3LoadBalancerGroupCreateReqGroup - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._https_port = None
        self._name = None
        self._oss_api_enabled = None
        self._port = None
        self._roles = None
        self._s3_load_balancers = None
        self._search_https_port = None
        self._search_port = None
        self._sync_port = None
        self._web_service_config = None
        self._web_service_port = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if https_port is not None:
            self.https_port = https_port
        self.name = name
        if oss_api_enabled is not None:
            self.oss_api_enabled = oss_api_enabled
        if port is not None:
            self.port = port
        if roles is not None:
            self.roles = roles
        self.s3_load_balancers = s3_load_balancers
        if search_https_port is not None:
            self.search_https_port = search_https_port
        if search_port is not None:
            self.search_port = search_port
        if sync_port is not None:
            self.sync_port = sync_port
        if web_service_config is not None:
            self.web_service_config = web_service_config
        if web_service_port is not None:
            self.web_service_port = web_service_port

    @property
    def description(self):
        """Gets the description of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group description  # noqa: E501

        :return: The description of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this S3LoadBalancerGroupCreateReqGroup.

        group description  # noqa: E501

        :param description: The description of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def https_port(self):
        """Gets the https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group access https port  # noqa: E501

        :return: The https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this S3LoadBalancerGroupCreateReqGroup.

        group access https port  # noqa: E501

        :param https_port: The https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._https_port = https_port

    @property
    def name(self):
        """Gets the name of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group name  # noqa: E501

        :return: The name of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3LoadBalancerGroupCreateReqGroup.

        group name  # noqa: E501

        :param name: The name of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def oss_api_enabled(self):
        """Gets the oss_api_enabled of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501


        :return: The oss_api_enabled of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: bool
        """
        return self._oss_api_enabled

    @oss_api_enabled.setter
    def oss_api_enabled(self, oss_api_enabled):
        """Sets the oss_api_enabled of this S3LoadBalancerGroupCreateReqGroup.


        :param oss_api_enabled: The oss_api_enabled of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: bool
        """

        self._oss_api_enabled = oss_api_enabled

    @property
    def port(self):
        """Gets the port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group access http port  # noqa: E501

        :return: The port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this S3LoadBalancerGroupCreateReqGroup.

        group access http port  # noqa: E501

        :param port: The port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def roles(self):
        """Gets the roles of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group roles  # noqa: E501

        :return: The roles of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this S3LoadBalancerGroupCreateReqGroup.

        group roles  # noqa: E501

        :param roles: The roles of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def s3_load_balancers(self):
        """Gets the s3_load_balancers of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        s3 load balancers  # noqa: E501

        :return: The s3_load_balancers of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: list[S3LoadBalancerGroupCreateReqGroupLoadBalancersElt]
        """
        return self._s3_load_balancers

    @s3_load_balancers.setter
    def s3_load_balancers(self, s3_load_balancers):
        """Sets the s3_load_balancers of this S3LoadBalancerGroupCreateReqGroup.

        s3 load balancers  # noqa: E501

        :param s3_load_balancers: The s3_load_balancers of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: list[S3LoadBalancerGroupCreateReqGroupLoadBalancersElt]
        """
        if s3_load_balancers is None:
            raise ValueError("Invalid value for `s3_load_balancers`, must not be `None`")  # noqa: E501

        self._s3_load_balancers = s3_load_balancers

    @property
    def search_https_port(self):
        """Gets the search_https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group search https port  # noqa: E501

        :return: The search_https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._search_https_port

    @search_https_port.setter
    def search_https_port(self, search_https_port):
        """Sets the search_https_port of this S3LoadBalancerGroupCreateReqGroup.

        group search https port  # noqa: E501

        :param search_https_port: The search_https_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._search_https_port = search_https_port

    @property
    def search_port(self):
        """Gets the search_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group search http port  # noqa: E501

        :return: The search_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._search_port

    @search_port.setter
    def search_port(self, search_port):
        """Sets the search_port of this S3LoadBalancerGroupCreateReqGroup.

        group search http port  # noqa: E501

        :param search_port: The search_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._search_port = search_port

    @property
    def sync_port(self):
        """Gets the sync_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group sync http port  # noqa: E501

        :return: The sync_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._sync_port

    @sync_port.setter
    def sync_port(self, sync_port):
        """Sets the sync_port of this S3LoadBalancerGroupCreateReqGroup.

        group sync http port  # noqa: E501

        :param sync_port: The sync_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._sync_port = sync_port

    @property
    def web_service_config(self):
        """Gets the web_service_config of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        web service config  # noqa: E501

        :return: The web_service_config of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: S3LbGroupWebServiceConfig
        """
        return self._web_service_config

    @web_service_config.setter
    def web_service_config(self, web_service_config):
        """Sets the web_service_config of this S3LoadBalancerGroupCreateReqGroup.

        web service config  # noqa: E501

        :param web_service_config: The web_service_config of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: S3LbGroupWebServiceConfig
        """

        self._web_service_config = web_service_config

    @property
    def web_service_port(self):
        """Gets the web_service_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501

        group web service http port  # noqa: E501

        :return: The web_service_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :rtype: int
        """
        return self._web_service_port

    @web_service_port.setter
    def web_service_port(self, web_service_port):
        """Sets the web_service_port of this S3LoadBalancerGroupCreateReqGroup.

        group web service http port  # noqa: E501

        :param web_service_port: The web_service_port of this S3LoadBalancerGroupCreateReqGroup.  # noqa: E501
        :type: int
        """

        self._web_service_port = web_service_port

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
        if not isinstance(other, S3LoadBalancerGroupCreateReqGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
