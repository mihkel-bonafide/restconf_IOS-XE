import requests
import json
import urllib3
urllib3.disable_warnings()
from lehost import host,  get_interfaces_endpoint, username, password

url = host + get_interfaces_endpoint

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.get(url=url, headers=headers, auth=(
    username, password), verify=False)

if response.status_code == 200:
    response_dict = response.json()['ietf-interfaces:interfaces']['interface']
    print(json.dumps(response_dict, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
