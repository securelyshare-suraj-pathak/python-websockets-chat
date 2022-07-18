# coding: utf-8

"""
    ShiftText

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@securelyshare.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class EncodeRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'data': 'dict(str, str)',
        'scopes': 'list[Scope]'
    }

    attribute_map = {
        'data': 'data',
        'scopes': 'scopes'
    }

    def __init__(self, data=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """EncodeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._scopes = None
        self.discriminator = None

        self.data = data
        if scopes is not None:
            self.scopes = scopes

    @property
    def data(self):
        """Gets the data of this EncodeRequest.  # noqa: E501

        [Required] Content to encode in KEY:VALUE format. Key is the content  identifier from caller application which is returned in the response as it is so that the encoded value can be used, while Value is the  content that need to be encoded.  # noqa: E501

        :return: The data of this EncodeRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EncodeRequest.

        [Required] Content to encode in KEY:VALUE format. Key is the content  identifier from caller application which is returned in the response as it is so that the encoded value can be used, while Value is the  content that need to be encoded.  # noqa: E501

        :param data: The data of this EncodeRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def scopes(self):
        """Gets the scopes of this EncodeRequest.  # noqa: E501

        [Optional] List of scopes along with its values to create different  font. e.g. unique fonts are required per 'session per user' then key can be SESSION, USER. The order of scopes in the list should be  retained to get the same text/font.  # noqa: E501

        :return: The scopes of this EncodeRequest.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this EncodeRequest.

        [Optional] List of scopes along with its values to create different  font. e.g. unique fonts are required per 'session per user' then key can be SESSION, USER. The order of scopes in the list should be  retained to get the same text/font.  # noqa: E501

        :param scopes: The scopes of this EncodeRequest.  # noqa: E501
        :type: list[Scope]
        """

        self._scopes = scopes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, EncodeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncodeRequest):
            return True

        return self.to_dict() != other.to_dict()
