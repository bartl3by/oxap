# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Filestore(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_contexts: int=None, id: int=None, max_contexts: int=None, reserved: int=None, size: int=None, url: str=None, used: int=None):
        """
        Filestore - a model defined in Swagger

        :param current_contexts: The current_contexts of this Filestore.
        :type current_contexts: int
        :param id: The id of this Filestore.
        :type id: int
        :param max_contexts: The max_contexts of this Filestore.
        :type max_contexts: int
        :param reserved: The reserved of this Filestore.
        :type reserved: int
        :param size: The size of this Filestore.
        :type size: int
        :param url: The url of this Filestore.
        :type url: str
        :param used: The used of this Filestore.
        :type used: int
        """
        self.swagger_types = {
            'current_contexts': int,
            'id': int,
            'max_contexts': int,
            'reserved': int,
            'size': int,
            'url': str,
            'used': int
        }

        self.attribute_map = {
            'current_contexts': 'currentContexts',
            'id': 'id',
            'max_contexts': 'maxContexts',
            'reserved': 'reserved',
            'size': 'size',
            'url': 'url',
            'used': 'used'
        }

        self._current_contexts = current_contexts
        self._id = id
        self._max_contexts = max_contexts
        self._reserved = reserved
        self._size = size
        self._url = url
        self._used = used

    @classmethod
    def from_dict(cls, dikt) -> 'Filestore':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Filestore of this Filestore.
        :rtype: Filestore
        """
        return deserialize_model(dikt, cls)

    @property
    def current_contexts(self) -> int:
        """
        Gets the current_contexts of this Filestore.
        

        :return: The current_contexts of this Filestore.
        :rtype: int
        """
        return self._current_contexts

    @current_contexts.setter
    def current_contexts(self, current_contexts: int):
        """
        Sets the current_contexts of this Filestore.
        

        :param current_contexts: The current_contexts of this Filestore.
        :type current_contexts: int
        """

        self._current_contexts = current_contexts

    @property
    def id(self) -> int:
        """
        Gets the id of this Filestore.
        

        :return: The id of this Filestore.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Filestore.
        

        :param id: The id of this Filestore.
        :type id: int
        """

        self._id = id

    @property
    def max_contexts(self) -> int:
        """
        Gets the max_contexts of this Filestore.
        

        :return: The max_contexts of this Filestore.
        :rtype: int
        """
        return self._max_contexts

    @max_contexts.setter
    def max_contexts(self, max_contexts: int):
        """
        Sets the max_contexts of this Filestore.
        

        :param max_contexts: The max_contexts of this Filestore.
        :type max_contexts: int
        """

        self._max_contexts = max_contexts

    @property
    def reserved(self) -> int:
        """
        Gets the reserved of this Filestore.
        

        :return: The reserved of this Filestore.
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved: int):
        """
        Sets the reserved of this Filestore.
        

        :param reserved: The reserved of this Filestore.
        :type reserved: int
        """

        self._reserved = reserved

    @property
    def size(self) -> int:
        """
        Gets the size of this Filestore.
        

        :return: The size of this Filestore.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """
        Sets the size of this Filestore.
        

        :param size: The size of this Filestore.
        :type size: int
        """

        self._size = size

    @property
    def url(self) -> str:
        """
        Gets the url of this Filestore.
        

        :return: The url of this Filestore.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """
        Sets the url of this Filestore.
        

        :param url: The url of this Filestore.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def used(self) -> int:
        """
        Gets the used of this Filestore.
        

        :return: The used of this Filestore.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used: int):
        """
        Sets the used of this Filestore.
        

        :param used: The used of this Filestore.
        :type used: int
        """

        self._used = used
