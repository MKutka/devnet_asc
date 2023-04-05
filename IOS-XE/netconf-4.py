from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
# import logging
# logging.basicConfig(level=logging.DEBUG)


router = {"host": "sandbox-iosxe-latest-1.cisco.com", 
          "port": "830", 
          "username": "admin", 
          "password": "C1sco12345"}

print(router["host"])
print(router["port"])
print(router["username"])
print(router["password"])

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <interface xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>GigabitEthernet2</name>
  </interface>
 </interface>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>GigabitEthernet2</name>
  </interface>
 </interfaces-state>
 </filter>"""

with manager.connect(host=router["host"], port=router["port"], 
                     username=router["username"], password=router["password"], 
                     hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    # get the running confog on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running config')
    print(interface_netconf)

#below, xml is a property of interface_conf

# XMLDOM for formatting output to xml
# -----UNCOMMENT BELOW
# xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
# print(xmlDom.toprettyxml(indent="  "))
# print("*" * 25 + 'Break' + "*" * 50)
# -----UNCOMMENT ABOVE

#XMLTODICT for converting xml output to python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python)
print("*" * 50)
name = interface_python["interfaces-state"]["interface"]["name"]
print(name)

config = interface_python["interfaces-state"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']}")
print(f"Description: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")

m.close_session()