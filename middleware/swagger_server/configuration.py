#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tornado.options import define
import os


def define_configuration_options():

    define("config_file", default=os.path.join(os.getcwd(), "../configuration/middleware.conf"))

    # Server settings
    define("server_port", default="8080", help="Port of the tornado http server")

    # OXAP Account Configurations
    define("oxap_account_config_dir", default=os.path.join(os.getcwd(), "../configuration/"))
