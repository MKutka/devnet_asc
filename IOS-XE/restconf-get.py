import requests
import json
from pprint import pprint

# set up connection paramters in a dictionary
router = {"ip": "sandbox-iosxe-latest-1.cisco.com", "port": "443", "user": "admin", "pass": "C1sco12345"}

# set REST API headers
headers = {"Accept": "application/yang-data+json", 
           "Content-type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(router["user"], router["pass"]), verify=False)

api_data = response.json()
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"][0]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"][0]["admin-status"] == "if-state-up":
    print("Interface is up")

