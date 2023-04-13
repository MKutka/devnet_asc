import requests
import json
import vars
from pprint import pprint

url = f"https://{vars.host}/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": vars.username,
      "pwd": vars.password
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': vars.auth
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()

# pprint(response)
token = response['imdata'][0]['aaaLogin']['attributes']['token']
print(token)
cookies={}
cookies['APIC-cookie']=token


url = f"https://{vars.host}/api/node/mo/sys/intf/phys-[eth1/39].json"

payload = "{\n    \"l1PhysIf\":{\n        \"attributes\":{\n            \"descr\":\"Python API Test\"\n        }\n    }\n}"
headers = {
  'Authorization': vars.auth,
  'Content-Type': 'text/plain',
}

put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pprint(put_response)