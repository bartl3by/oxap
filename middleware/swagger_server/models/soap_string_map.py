# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.soap_map_entry import SOAPMapEntry
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SOAPStringMap(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, entries: List[SOAPMapEntry]=None):
        """
        SOAPStringMap - a model defined in Swagger

        :param entries: The entries of this SOAPStringMap.
        :type entries: List[SOAPMapEntry]
        """
        self.swagger_types = {
            'entries': List[SOAPMapEntry]
        }

        self.attribute_map = {
            'entries': 'entries'
        }

        self._entries = entries

    @classmethod
    def from_dict(cls, dikt) -> 'SOAPStringMap':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SOAPStringMap of this SOAPStringMap.
        :rtype: SOAPStringMap
        """
        return deserialize_model(dikt, cls)

    @property
    def entries(self) -> List[SOAPMapEntry]:
        """
        Gets the entries of this SOAPStringMap.

        :return: The entries of this SOAPStringMap.
        :rtype: List[SOAPMapEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries: List[SOAPMapEntry]):
        """
        Sets the entries of this SOAPStringMap.

        :param entries: The entries of this SOAPStringMap.
        :type entries: List[SOAPMapEntry]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")

        self._entries = entries
