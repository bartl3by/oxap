from tornado.options import options
import yaml
import os
from typing import List
from swagger_server.oxap.endpoint_interface import EndpointInterface
from swagger_server.oxap.endpoint import Endpoint
from swagger_server.oxap.endpoint_interface_types import AppsuiteSOAP
from swagger_server.oxap.soap_types import SOAPStandard, SOAPReseller
from swagger_server.oxap.service_types import ContextService


class OXAPAccount(object):

    def __init__(self, oxap_account_id: str):
        self.oxap_account_id = oxap_account_id

        self.configuration = None
        self._load_account_configuration()

        self.endpoints = None
        self._load_endpoints()

    def getAccountId(self) -> str:
        return self.oxap_account_id

    def getAccountName(self) -> str:
        return self.configuration['OXAPAccount']['name']

    def getAccountDescription(self) -> str:
        return self.configuration['OXAPAccount']['description']

    def getEndpointList(self) -> List[str]:
        return list(self.endpoints)

    def getEndpoint(self, endpoint_id: str) -> Endpoint:
        return self.endpoints[endpoint_id]

    def getEndpointInterfaceList(self, endpoint_id: str) -> List[str]:
        return list(self.endpoints[endpoint_id].getEndpointInterfaces())

    def getEndpointInterface(self, endpoint_interface_id: str) -> EndpointInterface:
        for endpoint_id in self.endpoints:
            if self.getEndpointInterface(endpoint_id, endpoint_interface_id) != None:
                return self.getEndpointInterface(endpoint_id, endpoint_interface_id)

    def getEndpointInterface(self, endpoint_id: str, endpoint_interface_id: str) -> EndpointInterface:
        return self.endpoints[endpoint_id].getEndpointInterfaces()[endpoint_interface_id]

    def getEndpointInterfaceByType(self, endpoint_id: str, service_type) -> EndpointInterface:
        for endpoint_interface_id in self.endpoints[endpoint_id].getEndpointInterfaces():
            if self.endpoints[endpoint_id].getEndpointInterfaces()[endpoint_interface_id].getType() == service_type:
                return self.endpoints[endpoint_id].getEndpointInterfaces()[endpoint_interface_id]

    def _load_account_configuration(self):
        with open(os.path.join(options.oxap_account_config_dir, str(self.oxap_account_id) + ".yaml"), 'r') as stream:
            self.configuration = yaml.load(stream)

    def _load_endpoints(self):
        """
        ..todo:: Add EndpointInterface implementation for all interface types
        """
        self.endpoints = dict()

        for endpoint in self.configuration['OXAPAccount']['endpoint']:
            endpoint_interfaces = dict()

            for endpoint_interface in endpoint['interface']:
                if endpoint_interface['type'] in (AppsuiteSOAP()):
                    endpoint_interfaces[endpoint_interface['id']] = EndpointInterface(
                        self.oxap_account_id,
                        endpoint['id'],
                        endpoint_interface['id'],
                        endpoint_interface['name'],
                        endpoint_interface['description'],
                        endpoint_interface['location'],
                        endpoint_interface['ssl_verify'],
                        endpoint_interface['login'],
                        endpoint_interface['password'],
                        endpoint_interface['ignore_binding'],
                        endpoint_interface['reseller'],
                        endpoint_interface['type']
                        )
            self.endpoints[endpoint['id']] = Endpoint(
                self.oxap_account_id,
                endpoint['id'],
                endpoint['name'],
                endpoint['description'],
                endpoint['oxaas'],
                endpoint_interfaces
                )
