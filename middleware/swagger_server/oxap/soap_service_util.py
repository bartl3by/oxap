from zeep import helpers, Client
from requests import Session
from zeep.transports import Transport
from swagger_server.oxap.service_types import ContextService
from swagger_server.oxap.endpoint_types import SOAPOXaaS, SOAPOnPrem
from swagger_server.oxap.endpoint_interface import EndpointInterface


def getServiceName(endpointType, serviceType):
    if endpointType == SOAPOXaaS():
        if serviceType == ContextService:
            return "OXResellerContextService"
    elif endpointType == SOAPOnPrem():
        if serviceType == ContextService:
            return "OXContextService"

def get_context_path(soapBasePath, endpointType, serviceType):
    return soapBasePath + "/" + getServiceName(endpointType, serviceType)

def initiate_client(endpointInterface, serviceType):
    session = Session()
    session.verify = endpointInterface.getSSLVerify()
    transport = Transport(session=session)
    client = Client(
        get_context_path(endpointInterface.getLocation(), endpointInterface.getEndpointType(), serviceType) + "?wsdl",
        transport=transport)
    return client

def create_service(client, endpointInterface, serviceType):
    if endpointInterface.getIgnoreBinding():
        return client.create_service(
            "{http://soap.reseller.admin.openexchange.com}" + getServiceName(endpointInterface.getEndpointType(), serviceType) + "SoapBinding",
             endpointInterface.getLocation() + "/" + getServiceName(endpointInterface.getEndpointType(), serviceType))
    else:
        return client.service

def get_credentials_object(client, endpointType):
    if endpointType == SOAPOXaaS():
        return client.get_type('ns7:Credentials')
    elif endpointType == SOAPOnPrem():
        return client.get_type('ns5:Credentials')
