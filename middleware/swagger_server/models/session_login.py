# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SessionLogin(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, password: str=None, account_id: str=None, endpoint_id: str=None, role: str=None):
        """SessionLogin - a model defined in Swagger

        :param username: The username of this SessionLogin.
        :type username: str
        :param password: The password of this SessionLogin.
        :type password: str
        :param account_id: The account_id of this SessionLogin.
        :type account_id: str
        :param endpoint_id: The endpoint_id of this SessionLogin.
        :type endpoint_id: str
        :param role: The role of this SessionLogin.
        :type role: str
        """
        self.swagger_types = {
            'username': str,
            'password': str,
            'account_id': str,
            'endpoint_id': str,
            'role': str
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'account_id': 'account_id',
            'endpoint_id': 'endpoint_id',
            'role': 'role'
        }

        self._username = username
        self._password = password
        self._account_id = account_id
        self._endpoint_id = endpoint_id
        self._role = role

    @classmethod
    def from_dict(cls, dikt) -> 'SessionLogin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SessionLogin of this SessionLogin.
        :rtype: SessionLogin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this SessionLogin.

        Id of the OXAP account

        :return: The username of this SessionLogin.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this SessionLogin.

        Id of the OXAP account

        :param username: The username of this SessionLogin.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this SessionLogin.

        Id of the OXAP endpoint for this OXAP account

        :return: The password of this SessionLogin.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this SessionLogin.

        Id of the OXAP endpoint for this OXAP account

        :param password: The password of this SessionLogin.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def account_id(self) -> str:
        """Gets the account_id of this SessionLogin.

        Id of the OXAP account

        :return: The account_id of this SessionLogin.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this SessionLogin.

        Id of the OXAP account

        :param account_id: The account_id of this SessionLogin.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def endpoint_id(self) -> str:
        """Gets the endpoint_id of this SessionLogin.

        Id of the OXAP endpoint for this OXAP account

        :return: The endpoint_id of this SessionLogin.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id: str):
        """Sets the endpoint_id of this SessionLogin.

        Id of the OXAP endpoint for this OXAP account

        :param endpoint_id: The endpoint_id of this SessionLogin.
        :type endpoint_id: str
        """

        self._endpoint_id = endpoint_id

    @property
    def role(self) -> str:
        """Gets the role of this SessionLogin.

        'The type of account that requests the login. If type is ': * oxap - An OXAP Master administrator having access to multiple endpoints * reseller - A Context reseller managing a context within an endpoint (the endpoint_id is required in data object) * context - A Context administrator managing a context within an endpoint (the endpoint_id is required in data object) * user - An Open-Xchange user account (the endpoint_id is required in data object)

        :return: The role of this SessionLogin.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this SessionLogin.

        'The type of account that requests the login. If type is ': * oxap - An OXAP Master administrator having access to multiple endpoints * reseller - A Context reseller managing a context within an endpoint (the endpoint_id is required in data object) * context - A Context administrator managing a context within an endpoint (the endpoint_id is required in data object) * user - An Open-Xchange user account (the endpoint_id is required in data object)

        :param role: The role of this SessionLogin.
        :type role: str
        """
        allowed_values = ["oxap", "context", "reseller", "user"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role