from ncclient import manager
import xml.dom.minidom

router = {"host": "sandbox-iosxe-latest-1.cisco.com", 
          "port": "830", 
          "username": "admin", 
          "password": "C1sco12345"}

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

        interface_netconf = m.get(netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent="  "))
        print("*" * 25 + 'Break' + "*" * 50)

        print('*' * 50)