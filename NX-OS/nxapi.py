import requests
import json

target = "https://172.16.101.5/ins"
username = "admin"
password = "admin"

requestheaders = {"content-type": "application/json"}
showcmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show ip int br",
    "output_format": "json"
  }
}
response = requests.post(target, 
                         data=json.dumps(showcmd), 
                         headers=requestheaders, 
                         auth=(username, password), 
                         verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))