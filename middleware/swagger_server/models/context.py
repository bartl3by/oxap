# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Context(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, average_size: int=None, enabled: bool=None, filestore_id: int=None, filestore_name: str=None, id: int=None, customid: str=None, login_mappings: str=None, max_quota: int=None, name: str=None, read_database: object=None, write_database: object=None, used_quota: int=None, user_attributes: object=None):
        """Context - a model defined in Swagger

        :param average_size: The average_size of this Context.
        :type average_size: int
        :param enabled: The enabled of this Context.
        :type enabled: bool
        :param filestore_id: The filestore_id of this Context.
        :type filestore_id: int
        :param filestore_name: The filestore_name of this Context.
        :type filestore_name: str
        :param id: The id of this Context.
        :type id: int
        :param customid: The customid of this Context.
        :type customid: str
        :param login_mappings: The login_mappings of this Context.
        :type login_mappings: str
        :param max_quota: The max_quota of this Context.
        :type max_quota: int
        :param name: The name of this Context.
        :type name: str
        :param read_database: The read_database of this Context.
        :type read_database: object
        :param write_database: The write_database of this Context.
        :type write_database: object
        :param used_quota: The used_quota of this Context.
        :type used_quota: int
        :param user_attributes: The user_attributes of this Context.
        :type user_attributes: object
        """
        self.swagger_types = {
            'average_size': int,
            'enabled': bool,
            'filestore_id': int,
            'filestore_name': str,
            'id': int,
            'customid': str,
            'login_mappings': str,
            'max_quota': int,
            'name': str,
            'read_database': object,
            'write_database': object,
            'used_quota': int,
            'user_attributes': object
        }

        self.attribute_map = {
            'average_size': 'average_size',
            'enabled': 'enabled',
            'filestore_id': 'filestoreId',
            'filestore_name': 'filestore_name',
            'id': 'id',
            'customid': 'customid',
            'login_mappings': 'loginMappings',
            'max_quota': 'maxQuota',
            'name': 'name',
            'read_database': 'readDatabase',
            'write_database': 'writeDatabase',
            'used_quota': 'usedQuota',
            'user_attributes': 'userAttributes'
        }

        self._average_size = average_size
        self._enabled = enabled
        self._filestore_id = filestore_id
        self._filestore_name = filestore_name
        self._id = id
        self._customid = customid
        self._login_mappings = login_mappings
        self._max_quota = max_quota
        self._name = name
        self._read_database = read_database
        self._write_database = write_database
        self._used_quota = used_quota
        self._user_attributes = user_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Context':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Context of this Context.
        :rtype: Context
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_size(self) -> int:
        """Gets the average_size of this Context.

        The average size of a context

        :return: The average_size of this Context.
        :rtype: int
        """
        return self._average_size

    @average_size.setter
    def average_size(self, average_size: int):
        """Sets the average_size of this Context.

        The average size of a context

        :param average_size: The average_size of this Context.
        :type average_size: int
        """

        self._average_size = average_size

    @property
    def enabled(self) -> bool:
        """Gets the enabled of this Context.

        Defines if the context is enabled or not

        :return: The enabled of this Context.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        """Sets the enabled of this Context.

        Defines if the context is enabled or not

        :param enabled: The enabled of this Context.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def filestore_id(self) -> int:
        """Gets the filestore_id of this Context.

        The filestore id of a context

        :return: The filestore_id of this Context.
        :rtype: int
        """
        return self._filestore_id

    @filestore_id.setter
    def filestore_id(self, filestore_id: int):
        """Sets the filestore_id of this Context.

        The filestore id of a context

        :param filestore_id: The filestore_id of this Context.
        :type filestore_id: int
        """

        self._filestore_id = filestore_id

    @property
    def filestore_name(self) -> str:
        """Gets the filestore_name of this Context.

        The filestore name of a context

        :return: The filestore_name of this Context.
        :rtype: str
        """
        return self._filestore_name

    @filestore_name.setter
    def filestore_name(self, filestore_name: str):
        """Sets the filestore_name of this Context.

        The filestore name of a context

        :param filestore_name: The filestore_name of this Context.
        :type filestore_name: str
        """

        self._filestore_name = filestore_name

    @property
    def id(self) -> int:
        """Gets the id of this Context.

        The id of a context

        :return: The id of this Context.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Context.

        The id of a context

        :param id: The id of this Context.
        :type id: int
        """

        self._id = id

    @property
    def customid(self) -> str:
        """Gets the customid of this Context.

        The customid of a context, only used for OXaaS API endpoints

        :return: The customid of this Context.
        :rtype: str
        """
        return self._customid

    @customid.setter
    def customid(self, customid: str):
        """Sets the customid of this Context.

        The customid of a context, only used for OXaaS API endpoints

        :param customid: The customid of this Context.
        :type customid: str
        """

        self._customid = customid

    @property
    def login_mappings(self) -> str:
        """Gets the login_mappings of this Context.

        The login mappings of a context (usually a list of domains)

        :return: The login_mappings of this Context.
        :rtype: str
        """
        return self._login_mappings

    @login_mappings.setter
    def login_mappings(self, login_mappings: str):
        """Sets the login_mappings of this Context.

        The login mappings of a context (usually a list of domains)

        :param login_mappings: The login_mappings of this Context.
        :type login_mappings: str
        """

        self._login_mappings = login_mappings

    @property
    def max_quota(self) -> int:
        """Gets the max_quota of this Context.

        The Drive quota setting of a context

        :return: The max_quota of this Context.
        :rtype: int
        """
        return self._max_quota

    @max_quota.setter
    def max_quota(self, max_quota: int):
        """Sets the max_quota of this Context.

        The Drive quota setting of a context

        :param max_quota: The max_quota of this Context.
        :type max_quota: int
        """
        if max_quota is None:
            raise ValueError("Invalid value for `max_quota`, must not be `None`")

        self._max_quota = max_quota

    @property
    def name(self) -> str:
        """Gets the name of this Context.

        The name of a context

        :return: The name of this Context.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Context.

        The name of a context

        :param name: The name of this Context.
        :type name: str
        """

        self._name = name

    @property
    def read_database(self) -> object:
        """Gets the read_database of this Context.

        The read database of a context

        :return: The read_database of this Context.
        :rtype: object
        """
        return self._read_database

    @read_database.setter
    def read_database(self, read_database: object):
        """Sets the read_database of this Context.

        The read database of a context

        :param read_database: The read_database of this Context.
        :type read_database: object
        """

        self._read_database = read_database

    @property
    def write_database(self) -> object:
        """Gets the write_database of this Context.

        The write database of a context

        :return: The write_database of this Context.
        :rtype: object
        """
        return self._write_database

    @write_database.setter
    def write_database(self, write_database: object):
        """Sets the write_database of this Context.

        The write database of a context

        :param write_database: The write_database of this Context.
        :type write_database: object
        """

        self._write_database = write_database

    @property
    def used_quota(self) -> int:
        """Gets the used_quota of this Context.

        The used quota of a context

        :return: The used_quota of this Context.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota: int):
        """Sets the used_quota of this Context.

        The used quota of a context

        :param used_quota: The used_quota of this Context.
        :type used_quota: int
        """

        self._used_quota = used_quota

    @property
    def user_attributes(self) -> object:
        """Gets the user_attributes of this Context.

        The user attributes of a context

        :return: The user_attributes of this Context.
        :rtype: object
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes: object):
        """Sets the user_attributes of this Context.

        The user attributes of a context

        :param user_attributes: The user_attributes of this Context.
        :type user_attributes: object
        """

        self._user_attributes = user_attributes
