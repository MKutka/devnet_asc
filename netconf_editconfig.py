from ncclient import manager
from eve_router_info import router
# import logging
# logging.basicConfig(level=logging.DEBUG)

config_template = open('ios_config.xml').read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Kutka was here"
    )

with manager.connect(host=router["host"], port=router["port"], 
                     username=router["username"], password=router["password"], 
                     hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)