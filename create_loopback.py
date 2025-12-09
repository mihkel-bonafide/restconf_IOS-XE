import requests
import json
import urllib3
urllib3.disable_warnings()
from lehost import host, create_loopback_endpoint, username, password


url = host + create_loopback_endpoint

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# loopback config deets go 'ere:
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback66",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.100.1",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

response = requests.post(url=url, headers=headers, auth=(
    username, password), json=payload, verify=False)

if response.status_code == 201:
    print(f"Success: {response.status_code} - Loopback interface configured!")
else:
    print(f"Error: {response.status_code} - {response.text}")