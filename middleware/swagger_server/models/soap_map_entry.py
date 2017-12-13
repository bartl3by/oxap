# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.entry import Entry
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SOAPMapEntry(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key: str=None, value: Entry=None):
        """
        SOAPMapEntry - a model defined in Swagger

        :param key: The key of this SOAPMapEntry.
        :type key: str
        :param value: The value of this SOAPMapEntry.
        :type value: Entry
        """
        self.swagger_types = {
            'key': str,
            'value': Entry
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'SOAPMapEntry':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SOAPMapEntry of this SOAPMapEntry.
        :rtype: SOAPMapEntry
        """
        return deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """
        Gets the key of this SOAPMapEntry.

        :return: The key of this SOAPMapEntry.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """
        Sets the key of this SOAPMapEntry.

        :param key: The key of this SOAPMapEntry.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def value(self) -> Entry:
        """
        Gets the value of this SOAPMapEntry.

        :return: The value of this SOAPMapEntry.
        :rtype: Entry
        """
        return self._value

    @value.setter
    def value(self, value: Entry):
        """
        Sets the value of this SOAPMapEntry.

        :param value: The value of this SOAPMapEntry.
        :type value: Entry
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
