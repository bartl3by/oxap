
class EndpointInterface(object):

    def __init__(self, endpoint_interface_id, name, description, location, ssl_verify, login, password, ignore_binding, endpoint_type):
        self.endpoint_interface_id = endpoint_interface_id
        self.name = name
        self.description = description
        self.location = location
        self.ssl_verify = ssl_verify
        self.login = login
        self.password = password
        self.ignore_binding = ignore_binding
        self.endpoint_type = endpoint_type

    def getEndpointInterfaceId(self) -> int:
        return self.endpoint_interface_id

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getLocation(self) -> str:
        return self.location

    def getSSLVerify(self) -> bool:
        return self.ssl_verify

    def getLogin(self) -> str:
        return self.login

    def getPassword(self) -> str:
        return self.password

    def getIgnoreBinding(self) -> bool:
        return self.ignore_binding

    def getEndpointType(self) -> str:
        return self.endpoint_type
