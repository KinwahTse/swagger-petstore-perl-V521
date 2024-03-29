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


class IdentityPlatform(object):
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
        'enabled': 'bool',
        'extra': 'object',
        'failure_num': 'int',
        'id': 'int',
        'key': 'str',
        'login_page_enabled': 'bool',
        'logout_url': 'str',
        'name': 'str',
        'success_num': 'int',
        'type': 'str',
        'update': 'datetime',
        'url': 'str',
        'uuid': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'create': 'create',
        'enabled': 'enabled',
        'extra': 'extra',
        'failure_num': 'failure_num',
        'id': 'id',
        'key': 'key',
        'login_page_enabled': 'login_page_enabled',
        'logout_url': 'logout_url',
        'name': 'name',
        'success_num': 'success_num',
        'type': 'type',
        'update': 'update',
        'url': 'url',
        'uuid': 'uuid',
        'vendor': 'vendor'
    }

    def __init__(self, create=None, enabled=None, extra=None, failure_num=None, id=None, key=None, login_page_enabled=None, logout_url=None, name=None, success_num=None, type=None, update=None, url=None, uuid=None, vendor=None):  # noqa: E501
        """IdentityPlatform - a model defined in Swagger"""  # noqa: E501

        self._create = None
        self._enabled = None
        self._extra = None
        self._failure_num = None
        self._id = None
        self._key = None
        self._login_page_enabled = None
        self._logout_url = None
        self._name = None
        self._success_num = None
        self._type = None
        self._update = None
        self._url = None
        self._uuid = None
        self._vendor = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if enabled is not None:
            self.enabled = enabled
        if extra is not None:
            self.extra = extra
        if failure_num is not None:
            self.failure_num = failure_num
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if login_page_enabled is not None:
            self.login_page_enabled = login_page_enabled
        if logout_url is not None:
            self.logout_url = logout_url
        if name is not None:
            self.name = name
        if success_num is not None:
            self.success_num = success_num
        if type is not None:
            self.type = type
        if update is not None:
            self.update = update
        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid
        if vendor is not None:
            self.vendor = vendor

    @property
    def create(self):
        """Gets the create of this IdentityPlatform.  # noqa: E501

        time of creating identity platform  # noqa: E501

        :return: The create of this IdentityPlatform.  # noqa: E501
        :rtype: datetime
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this IdentityPlatform.

        time of creating identity platform  # noqa: E501

        :param create: The create of this IdentityPlatform.  # noqa: E501
        :type: datetime
        """

        self._create = create

    @property
    def enabled(self):
        """Gets the enabled of this IdentityPlatform.  # noqa: E501

        enable the identity platform or not  # noqa: E501

        :return: The enabled of this IdentityPlatform.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityPlatform.

        enable the identity platform or not  # noqa: E501

        :param enabled: The enabled of this IdentityPlatform.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def extra(self):
        """Gets the extra of this IdentityPlatform.  # noqa: E501


        :return: The extra of this IdentityPlatform.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this IdentityPlatform.


        :param extra: The extra of this IdentityPlatform.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def failure_num(self):
        """Gets the failure_num of this IdentityPlatform.  # noqa: E501

        num of failed authorization  # noqa: E501

        :return: The failure_num of this IdentityPlatform.  # noqa: E501
        :rtype: int
        """
        return self._failure_num

    @failure_num.setter
    def failure_num(self, failure_num):
        """Sets the failure_num of this IdentityPlatform.

        num of failed authorization  # noqa: E501

        :param failure_num: The failure_num of this IdentityPlatform.  # noqa: E501
        :type: int
        """

        self._failure_num = failure_num

    @property
    def id(self):
        """Gets the id of this IdentityPlatform.  # noqa: E501

        id of identity platform  # noqa: E501

        :return: The id of this IdentityPlatform.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityPlatform.

        id of identity platform  # noqa: E501

        :param id: The id of this IdentityPlatform.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this IdentityPlatform.  # noqa: E501

        secret key of identity platform  # noqa: E501

        :return: The key of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IdentityPlatform.

        secret key of identity platform  # noqa: E501

        :param key: The key of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def login_page_enabled(self):
        """Gets the login_page_enabled of this IdentityPlatform.  # noqa: E501


        :return: The login_page_enabled of this IdentityPlatform.  # noqa: E501
        :rtype: bool
        """
        return self._login_page_enabled

    @login_page_enabled.setter
    def login_page_enabled(self, login_page_enabled):
        """Sets the login_page_enabled of this IdentityPlatform.


        :param login_page_enabled: The login_page_enabled of this IdentityPlatform.  # noqa: E501
        :type: bool
        """

        self._login_page_enabled = login_page_enabled

    @property
    def logout_url(self):
        """Gets the logout_url of this IdentityPlatform.  # noqa: E501


        :return: The logout_url of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._logout_url

    @logout_url.setter
    def logout_url(self, logout_url):
        """Sets the logout_url of this IdentityPlatform.


        :param logout_url: The logout_url of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._logout_url = logout_url

    @property
    def name(self):
        """Gets the name of this IdentityPlatform.  # noqa: E501

        name of identity platform  # noqa: E501

        :return: The name of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityPlatform.

        name of identity platform  # noqa: E501

        :param name: The name of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def success_num(self):
        """Gets the success_num of this IdentityPlatform.  # noqa: E501

        num of successful authorization  # noqa: E501

        :return: The success_num of this IdentityPlatform.  # noqa: E501
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this IdentityPlatform.

        num of successful authorization  # noqa: E501

        :param success_num: The success_num of this IdentityPlatform.  # noqa: E501
        :type: int
        """

        self._success_num = success_num

    @property
    def type(self):
        """Gets the type of this IdentityPlatform.  # noqa: E501

        type of identity platform  # noqa: E501

        :return: The type of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityPlatform.

        type of identity platform  # noqa: E501

        :param type: The type of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update(self):
        """Gets the update of this IdentityPlatform.  # noqa: E501

        time of updating identity platform  # noqa: E501

        :return: The update of this IdentityPlatform.  # noqa: E501
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this IdentityPlatform.

        time of updating identity platform  # noqa: E501

        :param update: The update of this IdentityPlatform.  # noqa: E501
        :type: datetime
        """

        self._update = update

    @property
    def url(self):
        """Gets the url of this IdentityPlatform.  # noqa: E501

        url of identity platform  # noqa: E501

        :return: The url of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdentityPlatform.

        url of identity platform  # noqa: E501

        :param url: The url of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """Gets the uuid of this IdentityPlatform.  # noqa: E501


        :return: The uuid of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this IdentityPlatform.


        :param uuid: The uuid of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vendor(self):
        """Gets the vendor of this IdentityPlatform.  # noqa: E501

        vendor for type  # noqa: E501

        :return: The vendor of this IdentityPlatform.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this IdentityPlatform.

        vendor for type  # noqa: E501

        :param vendor: The vendor of this IdentityPlatform.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, IdentityPlatform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
