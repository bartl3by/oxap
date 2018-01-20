#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from tornado.options import define


def define_configuration_options():

    define("config_file", default=os.path.join(os.getcwd(), "../configuration/middleware.conf"))

    # Server settings
    define("server_port", default="8080", help="Port of the tornado http server")

    # Caching Configuration
    define("cache_wsdl_store_path", default="wsdl_cache.db",
           help="Path to the SQLite WSDL cache database")
    define("cache_wsdl_timeout", default=60, help="Cache timeout in seconds for the WSDL caching")
    define("cache_session_memcache_host", default="localhost",
           help="Host address of the Memcache server")
    define("cache_session_memcache_port", default=11211, help="Host port of the Memcache server")
    define("cache_session_memcache_timeout", default=60,
           help="Cache timeout in seconds used for the Memcache server connection")
    define("cache_session_memcache_noreply", default=True,
           help="Wether OXAP write requests towards Memcache should wait for an answer.")

    # Session Configuration
    define("session_timeout", default=3600, help="Session timeout in seconds for OXAP sessions")

    # OXAP Account Configurations
    define("oxap_account_config_dir", default=os.path.join(os.getcwd(), "../configuration/"))
