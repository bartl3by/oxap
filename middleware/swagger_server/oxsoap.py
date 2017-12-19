from tornado.options import options
from zeep import helpers, Client
from requests import Session
from zeep.transports import Transport
from swagger_server.service_types import ContextService


def getServiceName(endpointType, serviceType):
    if endpointType == "oxaas":
        if serviceType == ContextService:
            return "OXResellerContextService"
    elif endpointType == "onpremise":
        if serviceType == ContextService:
            return "OXContextService"

def get_context_path(soapBasePath, endpointType, serviceType):
    return soapBasePath + "/" + getServiceName(endpointType, serviceType)

def initiate_client(endpointType, serviceType):
    session = Session()
    session.verify = options.oxap_account_endpoint_soap_sslverify
    transport = Transport(session=session)
    client = Client(
        get_context_path(options.oxap_account_endpoint_soap_baseurl, endpointType, serviceType) + "?wsdl",
        transport=transport)
    return client

def create_service(client, endpointType, serviceType):
    return client.create_service(
        "{http://soap.reseller.admin.openexchange.com}" + getServiceName(endpointType, serviceType) + "SoapBinding",
         options.oxap_account_endpoint_soap_baseurl + "/" + getServiceName(endpointType, serviceType))

def get_credentials_object(client, endpointType):
    if endpointType == "oxaas":
        return client.get_type('ns7:Credentials')
    elif endpointType == "onpremise":
        return client.get_type('ns5:Credentials')
