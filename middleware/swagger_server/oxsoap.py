from tornado.options import options
from zeep import helpers, Client
from requests import Session
from zeep.transports import Transport


def get_context_path(soapBasePath, endpointType):
    if endpointType == "oxaas":
        return soapBasePath + "/OXResellerContextService?wsdl"
    elif endpointType == "onpremise":
        return soapBasePath + "/OXContextService?wsdl"

def initiate_client(endpointType):
    if endpointType == "oxaas":
        session = Session()
        session.verify = options.oxap_account_endpoint_soap_sslverify
        transport = Transport(session=session)
        client = Client(get_context_path(options.oxap_account_endpoint_soap_baseurl, options.oxap_account_endpoint_type),
            transport=transport)
        return client

def get_credentials_object(client, endpointType):
    if endpointType == "oxaas":
        return client.get_type('ns7:Credentials')
    elif endpointType == "onpremise":
        return client.get_type('ns5:Credentials')
