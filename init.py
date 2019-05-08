#!/usr/bin/env python3

import yaml

from config_validation import is_valid
from config_templating import execute_template

YAML_PATH="/config.yml"
TARGET_PATH="/etc/bind/named.conf"

try:
    with open(YAML_PATH, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    if(is_valid(config_data, "/config-schema.json")):
        print("Generating config ", TARGET_PATH)
        execute_template(config_data, "/config-template.j2", TARGET_PATH)

        if('zones' in config_data):
            for zone in config_data['zones']:
                zone['dns_servers'] = config_data['dns_servers']

                print("Generating config for zone", zone["name"])
                execute_template(zone, '/zone-template.j2', f'/var/bind/{ zone["name"] }.zone')

except FileNotFoundError:
     print(YAML_PATH, "not found, please mount the config file to", TARGET_PATH)