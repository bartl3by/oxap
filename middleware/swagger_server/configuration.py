from tornado.options import define
import os


def define_configuration_options():

    define("config_file", default=os.path.join(os.getcwd(), "../configuration/middleware.conf"))

    # Server settings
    define("server_port", default="8080", help="Port of the tornado http server")

    # OXAP Account
    define("oxap_account_id", default="")
    define("oxap_account_endpoint_type", default="")
    define("oxap_account_endpoint_soap_baseurl", default="")
    define("oxap_account_endpoint_soap_sslverify", default=False)
    define("oxap_account_endpoint_soap_login", default="")
    define("oxap_account_endpoint_soap_password", default="")
