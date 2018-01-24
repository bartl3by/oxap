#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zeep.exceptions import Fault

from swagger_server.oxap.exceptions.group_exceptions import *
from swagger_server.oxap.soap.base_soap_handler import SOAPHandler


class GroupSOAPHandler(SOAPHandler):

    def list_all_groups(self):
        try:
            return self.service.listAll(self.credentials(
                self.endpoint_interface.getLogin(),
                self.endpoint_interface.getPassword()))
        except Fault as e:
            raise GroupException(e.message, e.detail)
