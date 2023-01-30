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


class NetworkDiagnosisStat(object):
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
        'bandwidth': 'int',
        'coll_pkgs': 'int',
        'err_pkg_ratio': 'float',
        'lost_pkg_ratio': 'float',
        'recv_bytes': 'int',
        'recv_pkgs': 'int',
        'send_bytes': 'int',
        'send_pkgs': 'int',
        'tcp_conn_errs': 'int',
        'tcp_segment_retrans': 'int'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'coll_pkgs': 'coll_pkgs',
        'err_pkg_ratio': 'err_pkg_ratio',
        'lost_pkg_ratio': 'lost_pkg_ratio',
        'recv_bytes': 'recv_bytes',
        'recv_pkgs': 'recv_pkgs',
        'send_bytes': 'send_bytes',
        'send_pkgs': 'send_pkgs',
        'tcp_conn_errs': 'tcp_conn_errs',
        'tcp_segment_retrans': 'tcp_segment_retrans'
    }

    def __init__(self, bandwidth=None, coll_pkgs=None, err_pkg_ratio=None, lost_pkg_ratio=None, recv_bytes=None, recv_pkgs=None, send_bytes=None, send_pkgs=None, tcp_conn_errs=None, tcp_segment_retrans=None):  # noqa: E501
        """NetworkDiagnosisStat - a model defined in Swagger"""  # noqa: E501

        self._bandwidth = None
        self._coll_pkgs = None
        self._err_pkg_ratio = None
        self._lost_pkg_ratio = None
        self._recv_bytes = None
        self._recv_pkgs = None
        self._send_bytes = None
        self._send_pkgs = None
        self._tcp_conn_errs = None
        self._tcp_segment_retrans = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if coll_pkgs is not None:
            self.coll_pkgs = coll_pkgs
        if err_pkg_ratio is not None:
            self.err_pkg_ratio = err_pkg_ratio
        if lost_pkg_ratio is not None:
            self.lost_pkg_ratio = lost_pkg_ratio
        if recv_bytes is not None:
            self.recv_bytes = recv_bytes
        if recv_pkgs is not None:
            self.recv_pkgs = recv_pkgs
        if send_bytes is not None:
            self.send_bytes = send_bytes
        if send_pkgs is not None:
            self.send_pkgs = send_pkgs
        if tcp_conn_errs is not None:
            self.tcp_conn_errs = tcp_conn_errs
        if tcp_segment_retrans is not None:
            self.tcp_segment_retrans = tcp_segment_retrans

    @property
    def bandwidth(self):
        """Gets the bandwidth of this NetworkDiagnosisStat.  # noqa: E501


        :return: The bandwidth of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this NetworkDiagnosisStat.


        :param bandwidth: The bandwidth of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def coll_pkgs(self):
        """Gets the coll_pkgs of this NetworkDiagnosisStat.  # noqa: E501


        :return: The coll_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._coll_pkgs

    @coll_pkgs.setter
    def coll_pkgs(self, coll_pkgs):
        """Sets the coll_pkgs of this NetworkDiagnosisStat.


        :param coll_pkgs: The coll_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._coll_pkgs = coll_pkgs

    @property
    def err_pkg_ratio(self):
        """Gets the err_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501


        :return: The err_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: float
        """
        return self._err_pkg_ratio

    @err_pkg_ratio.setter
    def err_pkg_ratio(self, err_pkg_ratio):
        """Sets the err_pkg_ratio of this NetworkDiagnosisStat.


        :param err_pkg_ratio: The err_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501
        :type: float
        """

        self._err_pkg_ratio = err_pkg_ratio

    @property
    def lost_pkg_ratio(self):
        """Gets the lost_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501


        :return: The lost_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: float
        """
        return self._lost_pkg_ratio

    @lost_pkg_ratio.setter
    def lost_pkg_ratio(self, lost_pkg_ratio):
        """Sets the lost_pkg_ratio of this NetworkDiagnosisStat.


        :param lost_pkg_ratio: The lost_pkg_ratio of this NetworkDiagnosisStat.  # noqa: E501
        :type: float
        """

        self._lost_pkg_ratio = lost_pkg_ratio

    @property
    def recv_bytes(self):
        """Gets the recv_bytes of this NetworkDiagnosisStat.  # noqa: E501


        :return: The recv_bytes of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._recv_bytes

    @recv_bytes.setter
    def recv_bytes(self, recv_bytes):
        """Sets the recv_bytes of this NetworkDiagnosisStat.


        :param recv_bytes: The recv_bytes of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._recv_bytes = recv_bytes

    @property
    def recv_pkgs(self):
        """Gets the recv_pkgs of this NetworkDiagnosisStat.  # noqa: E501


        :return: The recv_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._recv_pkgs

    @recv_pkgs.setter
    def recv_pkgs(self, recv_pkgs):
        """Sets the recv_pkgs of this NetworkDiagnosisStat.


        :param recv_pkgs: The recv_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._recv_pkgs = recv_pkgs

    @property
    def send_bytes(self):
        """Gets the send_bytes of this NetworkDiagnosisStat.  # noqa: E501


        :return: The send_bytes of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._send_bytes

    @send_bytes.setter
    def send_bytes(self, send_bytes):
        """Sets the send_bytes of this NetworkDiagnosisStat.


        :param send_bytes: The send_bytes of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._send_bytes = send_bytes

    @property
    def send_pkgs(self):
        """Gets the send_pkgs of this NetworkDiagnosisStat.  # noqa: E501


        :return: The send_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._send_pkgs

    @send_pkgs.setter
    def send_pkgs(self, send_pkgs):
        """Sets the send_pkgs of this NetworkDiagnosisStat.


        :param send_pkgs: The send_pkgs of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._send_pkgs = send_pkgs

    @property
    def tcp_conn_errs(self):
        """Gets the tcp_conn_errs of this NetworkDiagnosisStat.  # noqa: E501


        :return: The tcp_conn_errs of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._tcp_conn_errs

    @tcp_conn_errs.setter
    def tcp_conn_errs(self, tcp_conn_errs):
        """Sets the tcp_conn_errs of this NetworkDiagnosisStat.


        :param tcp_conn_errs: The tcp_conn_errs of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._tcp_conn_errs = tcp_conn_errs

    @property
    def tcp_segment_retrans(self):
        """Gets the tcp_segment_retrans of this NetworkDiagnosisStat.  # noqa: E501


        :return: The tcp_segment_retrans of this NetworkDiagnosisStat.  # noqa: E501
        :rtype: int
        """
        return self._tcp_segment_retrans

    @tcp_segment_retrans.setter
    def tcp_segment_retrans(self, tcp_segment_retrans):
        """Sets the tcp_segment_retrans of this NetworkDiagnosisStat.


        :param tcp_segment_retrans: The tcp_segment_retrans of this NetworkDiagnosisStat.  # noqa: E501
        :type: int
        """

        self._tcp_segment_retrans = tcp_segment_retrans

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
        if not isinstance(other, NetworkDiagnosisStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
