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


class OSUserPropertiesReq(object):
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
        'area_code': 'str',
        'contact_person': 'str',
        'email': 'str',
        'mobile': 'str',
        'user_name': 'str',
        'user_type': 'int'
    }

    attribute_map = {
        'area_code': 'area_code',
        'contact_person': 'contact_person',
        'email': 'email',
        'mobile': 'mobile',
        'user_name': 'user_name',
        'user_type': 'user_type'
    }

    def __init__(self, area_code=None, contact_person=None, email=None, mobile=None, user_name=None, user_type=None):  # noqa: E501
        """OSUserPropertiesReq - a model defined in Swagger"""  # noqa: E501

        self._area_code = None
        self._contact_person = None
        self._email = None
        self._mobile = None
        self._user_name = None
        self._user_type = None
        self.discriminator = None

        if area_code is not None:
            self.area_code = area_code
        if contact_person is not None:
            self.contact_person = contact_person
        if email is not None:
            self.email = email
        if mobile is not None:
            self.mobile = mobile
        if user_name is not None:
            self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type

    @property
    def area_code(self):
        """Gets the area_code of this OSUserPropertiesReq.  # noqa: E501


        :return: The area_code of this OSUserPropertiesReq.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this OSUserPropertiesReq.


        :param area_code: The area_code of this OSUserPropertiesReq.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def contact_person(self):
        """Gets the contact_person of this OSUserPropertiesReq.  # noqa: E501


        :return: The contact_person of this OSUserPropertiesReq.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this OSUserPropertiesReq.


        :param contact_person: The contact_person of this OSUserPropertiesReq.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def email(self):
        """Gets the email of this OSUserPropertiesReq.  # noqa: E501


        :return: The email of this OSUserPropertiesReq.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OSUserPropertiesReq.


        :param email: The email of this OSUserPropertiesReq.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def mobile(self):
        """Gets the mobile of this OSUserPropertiesReq.  # noqa: E501


        :return: The mobile of this OSUserPropertiesReq.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this OSUserPropertiesReq.


        :param mobile: The mobile of this OSUserPropertiesReq.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def user_name(self):
        """Gets the user_name of this OSUserPropertiesReq.  # noqa: E501


        :return: The user_name of this OSUserPropertiesReq.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OSUserPropertiesReq.


        :param user_name: The user_name of this OSUserPropertiesReq.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_type(self):
        """Gets the user_type of this OSUserPropertiesReq.  # noqa: E501


        :return: The user_type of this OSUserPropertiesReq.  # noqa: E501
        :rtype: int
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this OSUserPropertiesReq.


        :param user_type: The user_type of this OSUserPropertiesReq.  # noqa: E501
        :type: int
        """

        self._user_type = user_type

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
        if not isinstance(other, OSUserPropertiesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
