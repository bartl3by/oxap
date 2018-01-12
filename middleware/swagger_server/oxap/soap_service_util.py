from zeep import helpers, Client
from requests import Session
from zeep.transports import Transport
from swagger_server.oxap.service_types import ContextService
from swagger_server.oxap.soap_types import SOAPStandard, SOAPReseller
from swagger_server.oxap.endpoint_interface_types import AppsuiteSOAP
from swagger_server.oxap.oxap_account import OXAPAccount
from swagger_server.oxap.endpoint_interface import EndpointInterface
import logging


def _getServiceName(service_type, soap_type) -> str:
    if soap_type == SOAPStandard:
        if service_type == ContextService:
            return "OXContextService"
    elif soap_type == SOAPReseller:
        if service_type == ContextService:
            return "OXResellerContextService"
    else:
        logging.error("Unknown SOAP type found: " + str(soap_type))

def _get_context_path(soap_base_path, soap_type, service_type) -> str:
    return soap_base_path + "/" + _getServiceName(service_type, soap_type)

def initiate_oxsoap_client(endpoint_interface: EndpointInterface, service_type):
    session = Session()
    session.verify = endpoint_interface.getSSLVerify()
    transport = Transport(session=session)
    return Client(
        _get_context_path(endpoint_interface.getLocation(), endpoint_interface.getSOAPType(), service_type) + "?wsdl",
        transport=transport)

def create_oxsoap_service(client, endpoint_interface, service_type) -> Client:
    binding_url = None
    if endpoint_interface.getSOAPType() == SOAPStandard:
        binding_url = "{http://soap.admin.openexchange.com}"
    elif endpoint_interface.getSOAPType() == SOAPReseller:
        binding_url = "{http://soap.reseller.admin.openexchange.com}"
    else:
        logging.error("Unknown SOAP type found: " + str(endpoint_interface.getSOAPType()))

    if endpoint_interface.getIgnoreBinding():
        return client.create_service(
            binding_url + _getServiceName(service_type, endpoint_interface.getSOAPType()) + "SoapBinding",
            endpoint_interface.getLocation() + "/" + _getServiceName(service_type, endpoint_interface.getSOAPType()))
    else:
        return client.service

def get_oxsoap_context_object(client, soap_type):
    if soap_type == SOAPStandard:
        return client.get_type('ns4:Context')
    elif soap_type == SOAPReseller:
        return client.get_type('ns4:ResellerContext')
    else:
        logging.error("Unknown SOAP type found: " + str(soap_type))

def get_oxsoap_credentials_object(client, soap_type):
    if soap_type == SOAPStandard:
        return client.get_type('ns5:Credentials')
    elif soap_type == SOAPReseller:
        return client.get_type('ns7:Credentials')
    else:
        logging.error("Unknown SOAP type found: " + str(soap_type))

def get_oxsoap_user_object(client, soap_type):
    if soap_type == SOAPStandard:
        return client.get_type('ns4:User')
    elif soap_type == SOAPReseller:
        return client.get_type('ns5:User')
    else:
        logging.error("Unknown SOAP type found: " + str(soap_type))

def get_oxsoap_schema_select_strategy_object(client, soap_type):
    if soap_type == SOAPStandard:
        return client.get_type('ns4:SchemaSelectStrategy')
    elif soap_type == SOAPReseller:
        return client.get_type('ns5:SchemaSelectStrategy')
    else:
        logging.error("Unknown SOAP type found: " + str(soap_type))
