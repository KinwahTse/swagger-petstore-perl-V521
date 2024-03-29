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

# from xms_client.models.dfs_ftp_session import DfsFTPSession  # noqa: F401,E501
# from xms_client.models.dfs_nfs_connection import DfsNFSConnection  # noqa: F401,E501
# from xms_client.models.dfs_s3_bucket_connection import DfsS3BucketConnection  # noqa: F401,E501
# from xms_client.models.dfs_smb_session import DfsSMBSession  # noqa: F401,E501


class DfsGatewayConnectionsResp(object):
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
        'ftp_sessions': 'list[DfsFTPSession]',
        'nfs_connections': 'list[DfsNFSConnection]',
        's3_connections': 'list[DfsS3BucketConnection]',
        'smb_sessions': 'list[DfsSMBSession]'
    }

    attribute_map = {
        'ftp_sessions': 'ftp_sessions',
        'nfs_connections': 'nfs_connections',
        's3_connections': 's3_connections',
        'smb_sessions': 'smb_sessions'
    }

    def __init__(self, ftp_sessions=None, nfs_connections=None, s3_connections=None, smb_sessions=None):  # noqa: E501
        """DfsGatewayConnectionsResp - a model defined in Swagger"""  # noqa: E501

        self._ftp_sessions = None
        self._nfs_connections = None
        self._s3_connections = None
        self._smb_sessions = None
        self.discriminator = None

        if ftp_sessions is not None:
            self.ftp_sessions = ftp_sessions
        if nfs_connections is not None:
            self.nfs_connections = nfs_connections
        if s3_connections is not None:
            self.s3_connections = s3_connections
        if smb_sessions is not None:
            self.smb_sessions = smb_sessions

    @property
    def ftp_sessions(self):
        """Gets the ftp_sessions of this DfsGatewayConnectionsResp.  # noqa: E501

        dfs ftp sessions  # noqa: E501

        :return: The ftp_sessions of this DfsGatewayConnectionsResp.  # noqa: E501
        :rtype: list[DfsFTPSession]
        """
        return self._ftp_sessions

    @ftp_sessions.setter
    def ftp_sessions(self, ftp_sessions):
        """Sets the ftp_sessions of this DfsGatewayConnectionsResp.

        dfs ftp sessions  # noqa: E501

        :param ftp_sessions: The ftp_sessions of this DfsGatewayConnectionsResp.  # noqa: E501
        :type: list[DfsFTPSession]
        """

        self._ftp_sessions = ftp_sessions

    @property
    def nfs_connections(self):
        """Gets the nfs_connections of this DfsGatewayConnectionsResp.  # noqa: E501

        dfs nfs connections  # noqa: E501

        :return: The nfs_connections of this DfsGatewayConnectionsResp.  # noqa: E501
        :rtype: list[DfsNFSConnection]
        """
        return self._nfs_connections

    @nfs_connections.setter
    def nfs_connections(self, nfs_connections):
        """Sets the nfs_connections of this DfsGatewayConnectionsResp.

        dfs nfs connections  # noqa: E501

        :param nfs_connections: The nfs_connections of this DfsGatewayConnectionsResp.  # noqa: E501
        :type: list[DfsNFSConnection]
        """

        self._nfs_connections = nfs_connections

    @property
    def s3_connections(self):
        """Gets the s3_connections of this DfsGatewayConnectionsResp.  # noqa: E501

        dfs s3 bucket connections  # noqa: E501

        :return: The s3_connections of this DfsGatewayConnectionsResp.  # noqa: E501
        :rtype: list[DfsS3BucketConnection]
        """
        return self._s3_connections

    @s3_connections.setter
    def s3_connections(self, s3_connections):
        """Sets the s3_connections of this DfsGatewayConnectionsResp.

        dfs s3 bucket connections  # noqa: E501

        :param s3_connections: The s3_connections of this DfsGatewayConnectionsResp.  # noqa: E501
        :type: list[DfsS3BucketConnection]
        """

        self._s3_connections = s3_connections

    @property
    def smb_sessions(self):
        """Gets the smb_sessions of this DfsGatewayConnectionsResp.  # noqa: E501

        dfs smb sessions  # noqa: E501

        :return: The smb_sessions of this DfsGatewayConnectionsResp.  # noqa: E501
        :rtype: list[DfsSMBSession]
        """
        return self._smb_sessions

    @smb_sessions.setter
    def smb_sessions(self, smb_sessions):
        """Sets the smb_sessions of this DfsGatewayConnectionsResp.

        dfs smb sessions  # noqa: E501

        :param smb_sessions: The smb_sessions of this DfsGatewayConnectionsResp.  # noqa: E501
        :type: list[DfsSMBSession]
        """

        self._smb_sessions = smb_sessions

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
        if not isinstance(other, DfsGatewayConnectionsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
