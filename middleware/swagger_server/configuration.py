#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from tornado.options import define


def define_configuration_options():

    define("config_file", default=os.path.join(os.getcwd(), "../configuration/middleware.conf"))

    # Server settings
    define("server_port", default="8080", help="Port of the tornado http server")

    # Caching Configuration
    define("cache_wsdl_store_path", default="wsdl_cache.db", help="Path to the SQLite WSDL cache database")
    define("cache_wsdl_timeout", default=60, help="Cache timeout in seconds for the WSDL caching")

    # OXAP Account Configurations
    define("oxap_account_config_dir", default=os.path.join(os.getcwd(), "../configuration/"))
