import requests
import json
import urllib3
urllib3.disable_warnings()
from lehost import host, config_int_gig2_endpoint, username, password

"""
Use lehost.py to select any configurable interface (we're doing GigabitEthernet2 in this script for demo purposes)

Important note: for the PUT method, we're assigning the payload to the variable "json" as per the "requests" library's documentation
on sending JSON data in a PUT request cleanly. 
(see: https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests)

Additional note: One of the cool things about this operation is that you must configure any interface that is NOT our ingress interface (Gig1)
on a different network/subnet, otherwise this will throw an error, and the local device will revert back to its previous IPv4 configuration (GOOD!).
"""

url = host + config_int_gig2_endpoint

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# configuration for target interface goes 'ere:
payload = {
        "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.50.200",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

response = requests.put(url=url, headers=headers, auth=(
    username, password), json=payload, verify=False)

if response.status_code == 204:
    print(f"Success: {response.status_code} - Interface GigabitEthernet2 configured.")
else:
    print(f"Error: {response.status_code} - {response.text}")