# coding: utf-8

"""
    Products

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.products.configuration import Configuration


class LabelsBetweenObjectPair(object):
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
    openapi_types = {"from_object_type_id": "str", "from_object_id": "int", "to_object_type_id": "str", "to_object_id": "int", "labels": "list[str]"}

    attribute_map = {"from_object_type_id": "fromObjectTypeId", "from_object_id": "fromObjectId", "to_object_type_id": "toObjectTypeId", "to_object_id": "toObjectId", "labels": "labels"}

    def __init__(self, from_object_type_id=None, from_object_id=None, to_object_type_id=None, to_object_id=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """LabelsBetweenObjectPair - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_object_type_id = None
        self._from_object_id = None
        self._to_object_type_id = None
        self._to_object_id = None
        self._labels = None
        self.discriminator = None

        self.from_object_type_id = from_object_type_id
        self.from_object_id = from_object_id
        self.to_object_type_id = to_object_type_id
        self.to_object_id = to_object_id
        self.labels = labels

    @property
    def from_object_type_id(self):
        """Gets the from_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501


        :return: The from_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501
        :rtype: str
        """
        return self._from_object_type_id

    @from_object_type_id.setter
    def from_object_type_id(self, from_object_type_id):
        """Sets the from_object_type_id of this LabelsBetweenObjectPair.


        :param from_object_type_id: The from_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and from_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_object_type_id`, must not be `None`")  # noqa: E501

        self._from_object_type_id = from_object_type_id

    @property
    def from_object_id(self):
        """Gets the from_object_id of this LabelsBetweenObjectPair.  # noqa: E501


        :return: The from_object_id of this LabelsBetweenObjectPair.  # noqa: E501
        :rtype: int
        """
        return self._from_object_id

    @from_object_id.setter
    def from_object_id(self, from_object_id):
        """Sets the from_object_id of this LabelsBetweenObjectPair.


        :param from_object_id: The from_object_id of this LabelsBetweenObjectPair.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and from_object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_object_id`, must not be `None`")  # noqa: E501

        self._from_object_id = from_object_id

    @property
    def to_object_type_id(self):
        """Gets the to_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501


        :return: The to_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501
        :rtype: str
        """
        return self._to_object_type_id

    @to_object_type_id.setter
    def to_object_type_id(self, to_object_type_id):
        """Sets the to_object_type_id of this LabelsBetweenObjectPair.


        :param to_object_type_id: The to_object_type_id of this LabelsBetweenObjectPair.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `to_object_type_id`, must not be `None`")  # noqa: E501

        self._to_object_type_id = to_object_type_id

    @property
    def to_object_id(self):
        """Gets the to_object_id of this LabelsBetweenObjectPair.  # noqa: E501


        :return: The to_object_id of this LabelsBetweenObjectPair.  # noqa: E501
        :rtype: int
        """
        return self._to_object_id

    @to_object_id.setter
    def to_object_id(self, to_object_id):
        """Sets the to_object_id of this LabelsBetweenObjectPair.


        :param to_object_id: The to_object_id of this LabelsBetweenObjectPair.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and to_object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `to_object_id`, must not be `None`")  # noqa: E501

        self._to_object_id = to_object_id

    @property
    def labels(self):
        """Gets the labels of this LabelsBetweenObjectPair.  # noqa: E501


        :return: The labels of this LabelsBetweenObjectPair.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this LabelsBetweenObjectPair.


        :param labels: The labels of this LabelsBetweenObjectPair.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, LabelsBetweenObjectPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LabelsBetweenObjectPair):
            return True

        return self.to_dict() != other.to_dict()
