# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Group(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, displayname: str=None, id: int=None, members: int=None, name: str=None):
        """Group - a model defined in Swagger

        :param displayname: The displayname of this Group.
        :type displayname: str
        :param id: The id of this Group.
        :type id: int
        :param members: The members of this Group.
        :type members: int
        :param name: The name of this Group.
        :type name: str
        """
        self.swagger_types = {
            'displayname': str,
            'id': int,
            'members': int,
            'name': str
        }

        self.attribute_map = {
            'displayname': 'displayname',
            'id': 'id',
            'members': 'members',
            'name': 'name'
        }

        self._displayname = displayname
        self._id = id
        self._members = members
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Group':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group of this Group.
        :rtype: Group
        """
        return util.deserialize_model(dikt, cls)

    @property
    def displayname(self) -> str:
        """Gets the displayname of this Group.

        The displayname of the group

        :return: The displayname of this Group.
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname: str):
        """Sets the displayname of this Group.

        The displayname of the group

        :param displayname: The displayname of this Group.
        :type displayname: str
        """
        if displayname is None:
            raise ValueError("Invalid value for `displayname`, must not be `None`")

        self._displayname = displayname

    @property
    def id(self) -> int:
        """Gets the id of this Group.

        The id of the group

        :return: The id of this Group.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Group.

        The id of the group

        :param id: The id of this Group.
        :type id: int
        """

        self._id = id

    @property
    def members(self) -> int:
        """Gets the members of this Group.

        The members of the group

        :return: The members of this Group.
        :rtype: int
        """
        return self._members

    @members.setter
    def members(self, members: int):
        """Sets the members of this Group.

        The members of the group

        :param members: The members of this Group.
        :type members: int
        """

        self._members = members

    @property
    def name(self) -> str:
        """Gets the name of this Group.

        The displayname of the group

        :return: The name of this Group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Group.

        The displayname of the group

        :param name: The name of this Group.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
