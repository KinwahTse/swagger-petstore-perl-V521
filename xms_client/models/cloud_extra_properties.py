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


class CloudExtraProperties(object):
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
        'csi_driver_versions': 'list[str]',
        'domain_id': 'str',
        'domain_name': 'str',
        'k8s_version': 'str',
        'regions': 'list[str]',
        'tenant_id': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'csi_driver_versions': 'csi_driver_versions',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'k8s_version': 'k8s_version',
        'regions': 'regions',
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, csi_driver_versions=None, domain_id=None, domain_name=None, k8s_version=None, regions=None, tenant_id=None, tenant_name=None):  # noqa: E501
        """CloudExtraProperties - a model defined in Swagger"""  # noqa: E501

        self._csi_driver_versions = None
        self._domain_id = None
        self._domain_name = None
        self._k8s_version = None
        self._regions = None
        self._tenant_id = None
        self._tenant_name = None
        self.discriminator = None

        if csi_driver_versions is not None:
            self.csi_driver_versions = csi_driver_versions
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if k8s_version is not None:
            self.k8s_version = k8s_version
        if regions is not None:
            self.regions = regions
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def csi_driver_versions(self):
        """Gets the csi_driver_versions of this CloudExtraProperties.  # noqa: E501

        csi driver versions  # noqa: E501

        :return: The csi_driver_versions of this CloudExtraProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._csi_driver_versions

    @csi_driver_versions.setter
    def csi_driver_versions(self, csi_driver_versions):
        """Sets the csi_driver_versions of this CloudExtraProperties.

        csi driver versions  # noqa: E501

        :param csi_driver_versions: The csi_driver_versions of this CloudExtraProperties.  # noqa: E501
        :type: list[str]
        """

        self._csi_driver_versions = csi_driver_versions

    @property
    def domain_id(self):
        """Gets the domain_id of this CloudExtraProperties.  # noqa: E501

        domain id for openstack  # noqa: E501

        :return: The domain_id of this CloudExtraProperties.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CloudExtraProperties.

        domain id for openstack  # noqa: E501

        :param domain_id: The domain_id of this CloudExtraProperties.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this CloudExtraProperties.  # noqa: E501

        domain name for openstack  # noqa: E501

        :return: The domain_name of this CloudExtraProperties.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CloudExtraProperties.

        domain name for openstack  # noqa: E501

        :param domain_name: The domain_name of this CloudExtraProperties.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def k8s_version(self):
        """Gets the k8s_version of this CloudExtraProperties.  # noqa: E501

        kubernetes version  # noqa: E501

        :return: The k8s_version of this CloudExtraProperties.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this CloudExtraProperties.

        kubernetes version  # noqa: E501

        :param k8s_version: The k8s_version of this CloudExtraProperties.  # noqa: E501
        :type: str
        """

        self._k8s_version = k8s_version

    @property
    def regions(self):
        """Gets the regions of this CloudExtraProperties.  # noqa: E501

        regions for openstack  # noqa: E501

        :return: The regions of this CloudExtraProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this CloudExtraProperties.

        regions for openstack  # noqa: E501

        :param regions: The regions of this CloudExtraProperties.  # noqa: E501
        :type: list[str]
        """

        self._regions = regions

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CloudExtraProperties.  # noqa: E501

        tenant id for openstack  # noqa: E501

        :return: The tenant_id of this CloudExtraProperties.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CloudExtraProperties.

        tenant id for openstack  # noqa: E501

        :param tenant_id: The tenant_id of this CloudExtraProperties.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this CloudExtraProperties.  # noqa: E501

        tenant name for openstack  # noqa: E501

        :return: The tenant_name of this CloudExtraProperties.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this CloudExtraProperties.

        tenant name for openstack  # noqa: E501

        :param tenant_name: The tenant_name of this CloudExtraProperties.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

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
        if not isinstance(other, CloudExtraProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
