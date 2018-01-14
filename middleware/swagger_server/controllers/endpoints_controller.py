#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fnmatch
import os
from tornado.options import options
import yaml


def get_all_endpoints():
    """
    Get a list of all Open-Xchange Admin Panel account endpoints
    Get a list with restricted (public) information of all Open-Xchange Admin Panel account endpoints

    :rtype: None
    """
    response = []

    for file in os.listdir(options.oxap_account_config_dir):
        if fnmatch.fnmatch(file, '*.yaml'):
            with open(os.path.join(options.oxap_account_config_dir, file), 'r') as stream:
                configuration = yaml.load(stream)
                for currentEndpoint in configuration['OXAPAccount']['endpoint']:
                    endpoint = {}
                    endpoint['oxap_account_id'] = configuration['OXAPAccount']['id']
                    endpoint['oxap_account_name'] = configuration['OXAPAccount']['name']
                    endpoint['oxap_account_description'] = configuration['OXAPAccount']['description']
                    endpoint['endpoint_id'] = currentEndpoint['id']
                    endpoint['endpoint_name'] = currentEndpoint['name']
                    endpoint['endpoint_description'] = currentEndpoint['description']
                    response.append(endpoint)
                    
    return response
