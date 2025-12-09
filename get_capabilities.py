import requests
import json
import urllib3
urllib3.disable_warnings()
from lehost import host,  capabilities_endpoint, username, password

url = host + capabilities_endpoint

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.get(url=url, headers=headers, auth=(
    username, password), verify=False)

if response.status_code == 200:
    response_dict = response.json()
    with open('capabilities.json', 'w') as f:
        json.dump(response_dict['ietf-netconf-monitoring:capabilities']['capability'], f, indent=2)
