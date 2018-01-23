# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Restriction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mandatory_members_change: str=None, mandatory_members_create: str=None, mandatory_members_delete: str=None, mandatory_members_register: str=None):
        """Restriction - a model defined in Swagger

        :param mandatory_members_change: The mandatory_members_change of this Restriction.
        :type mandatory_members_change: str
        :param mandatory_members_create: The mandatory_members_create of this Restriction.
        :type mandatory_members_create: str
        :param mandatory_members_delete: The mandatory_members_delete of this Restriction.
        :type mandatory_members_delete: str
        :param mandatory_members_register: The mandatory_members_register of this Restriction.
        :type mandatory_members_register: str
        """
        self.swagger_types = {
            'mandatory_members_change': str,
            'mandatory_members_create': str,
            'mandatory_members_delete': str,
            'mandatory_members_register': str
        }

        self.attribute_map = {
            'mandatory_members_change': 'mandatoryMembersChange',
            'mandatory_members_create': 'mandatoryMembersCreate',
            'mandatory_members_delete': 'mandatoryMembersDelete',
            'mandatory_members_register': 'mandatoryMembersRegister'
        }

        self._mandatory_members_change = mandatory_members_change
        self._mandatory_members_create = mandatory_members_create
        self._mandatory_members_delete = mandatory_members_delete
        self._mandatory_members_register = mandatory_members_register

    @classmethod
    def from_dict(cls, dikt) -> 'Restriction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Restriction of this Restriction.
        :rtype: Restriction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mandatory_members_change(self) -> str:
        """Gets the mandatory_members_change of this Restriction.


        :return: The mandatory_members_change of this Restriction.
        :rtype: str
        """
        return self._mandatory_members_change

    @mandatory_members_change.setter
    def mandatory_members_change(self, mandatory_members_change: str):
        """Sets the mandatory_members_change of this Restriction.


        :param mandatory_members_change: The mandatory_members_change of this Restriction.
        :type mandatory_members_change: str
        """

        self._mandatory_members_change = mandatory_members_change

    @property
    def mandatory_members_create(self) -> str:
        """Gets the mandatory_members_create of this Restriction.


        :return: The mandatory_members_create of this Restriction.
        :rtype: str
        """
        return self._mandatory_members_create

    @mandatory_members_create.setter
    def mandatory_members_create(self, mandatory_members_create: str):
        """Sets the mandatory_members_create of this Restriction.


        :param mandatory_members_create: The mandatory_members_create of this Restriction.
        :type mandatory_members_create: str
        """

        self._mandatory_members_create = mandatory_members_create

    @property
    def mandatory_members_delete(self) -> str:
        """Gets the mandatory_members_delete of this Restriction.


        :return: The mandatory_members_delete of this Restriction.
        :rtype: str
        """
        return self._mandatory_members_delete

    @mandatory_members_delete.setter
    def mandatory_members_delete(self, mandatory_members_delete: str):
        """Sets the mandatory_members_delete of this Restriction.


        :param mandatory_members_delete: The mandatory_members_delete of this Restriction.
        :type mandatory_members_delete: str
        """

        self._mandatory_members_delete = mandatory_members_delete

    @property
    def mandatory_members_register(self) -> str:
        """Gets the mandatory_members_register of this Restriction.


        :return: The mandatory_members_register of this Restriction.
        :rtype: str
        """
        return self._mandatory_members_register

    @mandatory_members_register.setter
    def mandatory_members_register(self, mandatory_members_register: str):
        """Sets the mandatory_members_register of this Restriction.


        :param mandatory_members_register: The mandatory_members_register of this Restriction.
        :type mandatory_members_register: str
        """

        self._mandatory_members_register = mandatory_members_register
