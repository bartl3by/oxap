from tornado.options import options
import yaml
import os
from swagger_server.oxap.endpoint_interface import EndpointInterface
from swagger_server.oxap.endpoint_types import SOAPOXaaS, SOAPOnPrem


class OXAPAccount(object):

    def __init__(self, account_id):
        self.account_id = account_id
        self.configuration = None
        self._load_account_configuration()

    def getAccountId(self) -> str:
        return self.account_id

    def getEndpointInterface(self, endpointId):
        for currentEndpoint in self.configuration['OXAPAccount']['endpoint']:
            if currentEndpoint['id'] == endpointId:
                for currentInterface in currentEndpoint['interface']:
                    if currentInterface['endpoint_type'] in (SOAPOXaaS(), SOAPOnPrem()):
                        return EndpointInterface(
                            currentInterface['id'],
                            currentInterface['name'],
                            currentInterface['description'],
                            currentInterface['location'],
                            currentInterface['ssl_verify'],
                            currentInterface['login'],
                            currentInterface['password'],
                            currentInterface['ignore_binding'],
                            currentInterface['endpoint_type']
                        )

    def _load_account_configuration(self):
        with open(os.path.join(options.oxap_account_config_dir, str(self.account_id) + ".yaml"), 'r') as stream:
            self.configuration = yaml.load(stream)
