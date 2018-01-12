# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class EndpointInterface(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, description: str=None, location: str=None, ssl_verify: bool=None, login: str=None, password: str=None, ignore_binding: bool=None, reseller: bool=None, type: str=None):
        """
        EndpointInterface - a model defined in Swagger

        :param id: The id of this EndpointInterface.
        :type id: str
        :param name: The name of this EndpointInterface.
        :type name: str
        :param description: The description of this EndpointInterface.
        :type description: str
        :param location: The location of this EndpointInterface.
        :type location: str
        :param ssl_verify: The ssl_verify of this EndpointInterface.
        :type ssl_verify: bool
        :param login: The login of this EndpointInterface.
        :type login: str
        :param password: The password of this EndpointInterface.
        :type password: str
        :param ignore_binding: The ignore_binding of this EndpointInterface.
        :type ignore_binding: bool
        :param reseller: The reseller of this EndpointInterface.
        :type reseller: bool
        :param type: The type of this EndpointInterface.
        :type type: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'description': str,
            'location': str,
            'ssl_verify': bool,
            'login': str,
            'password': str,
            'ignore_binding': bool,
            'reseller': bool,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'location': 'location',
            'ssl_verify': 'ssl_verify',
            'login': 'login',
            'password': 'password',
            'ignore_binding': 'ignore_binding',
            'reseller': 'reseller',
            'type': 'type'
        }

        self._id = id
        self._name = name
        self._description = description
        self._location = location
        self._ssl_verify = ssl_verify
        self._login = login
        self._password = password
        self._ignore_binding = ignore_binding
        self._reseller = reseller
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'EndpointInterface':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EndpointInterface of this EndpointInterface.
        :rtype: EndpointInterface
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this EndpointInterface.

        :return: The id of this EndpointInterface.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this EndpointInterface.

        :param id: The id of this EndpointInterface.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EndpointInterface.
        

        :return: The name of this EndpointInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this EndpointInterface.
        

        :param name: The name of this EndpointInterface.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this EndpointInterface.
        

        :return: The description of this EndpointInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """
        Sets the description of this EndpointInterface.
        

        :param description: The description of this EndpointInterface.
        :type description: str
        """

        self._description = description

    @property
    def location(self) -> str:
        """
        Gets the location of this EndpointInterface.
        The url / address / location of the endpoint interface

        :return: The location of this EndpointInterface.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Sets the location of this EndpointInterface.
        The url / address / location of the endpoint interface

        :param location: The location of this EndpointInterface.
        :type location: str
        """

        self._location = location

    @property
    def ssl_verify(self) -> bool:
        """
        Gets the ssl_verify of this EndpointInterface.
        

        :return: The ssl_verify of this EndpointInterface.
        :rtype: bool
        """
        return self._ssl_verify

    @ssl_verify.setter
    def ssl_verify(self, ssl_verify: bool):
        """
        Sets the ssl_verify of this EndpointInterface.
        

        :param ssl_verify: The ssl_verify of this EndpointInterface.
        :type ssl_verify: bool
        """

        self._ssl_verify = ssl_verify

    @property
    def login(self) -> str:
        """
        Gets the login of this EndpointInterface.
        

        :return: The login of this EndpointInterface.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """
        Sets the login of this EndpointInterface.
        

        :param login: The login of this EndpointInterface.
        :type login: str
        """

        self._login = login

    @property
    def password(self) -> str:
        """
        Gets the password of this EndpointInterface.
        

        :return: The password of this EndpointInterface.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """
        Sets the password of this EndpointInterface.
        

        :param password: The password of this EndpointInterface.
        :type password: str
        """

        self._password = password

    @property
    def ignore_binding(self) -> bool:
        """
        Gets the ignore_binding of this EndpointInterface.
        

        :return: The ignore_binding of this EndpointInterface.
        :rtype: bool
        """
        return self._ignore_binding

    @ignore_binding.setter
    def ignore_binding(self, ignore_binding: bool):
        """
        Sets the ignore_binding of this EndpointInterface.
        

        :param ignore_binding: The ignore_binding of this EndpointInterface.
        :type ignore_binding: bool
        """

        self._ignore_binding = ignore_binding

    @property
    def reseller(self) -> bool:
        """
        Gets the reseller of this EndpointInterface.
        

        :return: The reseller of this EndpointInterface.
        :rtype: bool
        """
        return self._reseller

    @reseller.setter
    def reseller(self, reseller: bool):
        """
        Sets the reseller of this EndpointInterface.
        

        :param reseller: The reseller of this EndpointInterface.
        :type reseller: bool
        """

        self._reseller = reseller

    @property
    def type(self) -> str:
        """
        Gets the type of this EndpointInterface.
        \"Endpoint Interface Type\": * appsuite-soap - The App Suite SOAP API Endpoint * dovecot-ldap-dovecotMailboxUid - The Dovecot LDAP Endpoint for Mailbox Information * dovecot-ldap-dovecotMailPrimaryAddress - The Dovecot LDAP Endpoint for Primary Mail Address Information * dovecot-ldap-dovecotMailAliasAddress - The Dovecot LDAP Endpoint for Alias Information * dovecot-ldap-dovecotUserQuotaStorage - The Dovecot LDAP Endpoint for Quota Information 

        :return: The type of this EndpointInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this EndpointInterface.
        \"Endpoint Interface Type\": * appsuite-soap - The App Suite SOAP API Endpoint * dovecot-ldap-dovecotMailboxUid - The Dovecot LDAP Endpoint for Mailbox Information * dovecot-ldap-dovecotMailPrimaryAddress - The Dovecot LDAP Endpoint for Primary Mail Address Information * dovecot-ldap-dovecotMailAliasAddress - The Dovecot LDAP Endpoint for Alias Information * dovecot-ldap-dovecotUserQuotaStorage - The Dovecot LDAP Endpoint for Quota Information 

        :param type: The type of this EndpointInterface.
        :type type: str
        """
        allowed_values = ["appsuite-soap", "dovecot-ldap-dovecotMailboxUid", "dovecot-ldap-dovecotMailPrimaryAddress", "dovecot-ldap-dovecotMailAliasAddress", "dovecot-ldap-dovecotUserQuotaStorage"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

