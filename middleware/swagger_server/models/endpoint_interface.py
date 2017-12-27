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
    def __init__(self, id: str=None, name: str=None, description: str=None, location: str=None, login: str=None, password: str=None, endpoint_type: str=None):
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
        :param login: The login of this EndpointInterface.
        :type login: str
        :param password: The password of this EndpointInterface.
        :type password: str
        :param endpoint_type: The endpoint_type of this EndpointInterface.
        :type endpoint_type: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'description': str,
            'location': str,
            'login': str,
            'password': str,
            'endpoint_type': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'location': 'location',
            'login': 'login',
            'password': 'password',
            'endpoint_type': 'endpoint_type'
        }

        self._id = id
        self._name = name
        self._description = description
        self._location = location
        self._login = login
        self._password = password
        self._endpoint_type = endpoint_type

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
    def endpoint_type(self) -> str:
        """
        Gets the endpoint_type of this EndpointInterface.
        \"Endpoint Interface Type\": * appsuite-soap-oxaas - The App Suite SOAP API Endpoint for OXaaS * appsuite-soap-onprem - The App Suite SOAP API Endpoint for On-Premise Installations * dovecot-ldap-dovecotMailboxUid - The Dovecot LDAP Endpoint for Mailbox Information * dovecot-ldap-dovecotMailPrimaryAddress - The Dovecot LDAP Endpoint for Primary Mail Address Information * dovecot-ldap-dovecotMailAliasAddress - The Dovecot LDAP Endpoint for Alias Information * dovecot-ldap-dovecotUserQuotaStorage - The Dovecot LDAP Endpoint for Quota Information 

        :return: The endpoint_type of this EndpointInterface.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type: str):
        """
        Sets the endpoint_type of this EndpointInterface.
        \"Endpoint Interface Type\": * appsuite-soap-oxaas - The App Suite SOAP API Endpoint for OXaaS * appsuite-soap-onprem - The App Suite SOAP API Endpoint for On-Premise Installations * dovecot-ldap-dovecotMailboxUid - The Dovecot LDAP Endpoint for Mailbox Information * dovecot-ldap-dovecotMailPrimaryAddress - The Dovecot LDAP Endpoint for Primary Mail Address Information * dovecot-ldap-dovecotMailAliasAddress - The Dovecot LDAP Endpoint for Alias Information * dovecot-ldap-dovecotUserQuotaStorage - The Dovecot LDAP Endpoint for Quota Information 

        :param endpoint_type: The endpoint_type of this EndpointInterface.
        :type endpoint_type: str
        """
        allowed_values = ["appsuite-soap-oxaas", "appsuite-soap-onprem", "dovecot-ldap-dovecotMailboxUid", "dovecot-ldap-dovecotMailPrimaryAddress", "dovecot-ldap-dovecotMailAliasAddress", "dovecot-ldap-dovecotUserQuotaStorage"]
        if endpoint_type not in allowed_values:
            raise ValueError(
                "Invalid value for `endpoint_type` ({0}), must be one of {1}"
                .format(endpoint_type, allowed_values)
            )

        self._endpoint_type = endpoint_type

