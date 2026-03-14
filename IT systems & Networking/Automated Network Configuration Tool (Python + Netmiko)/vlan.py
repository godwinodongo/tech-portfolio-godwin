from netmiko import ConnectHandler
from devices import devices

vlans = [
    {"id": 10, "name": "SALES"},
    {"id": 20, "name": "HR"},
    {"id": 30, "name": "CCTV"},
]

def deploy_vlans():

    for router in devices:

        print("Connecting to", router["host"])

        connection = ConnectHandler(**router)

        for vlan in vlans:

            command = f"/interface vlan add name=vlan{vlan['id']} vlan-id={vlan['id']} interface=server"

            connection.send_command(command)

            print(f"Created VLAN {vlan['id']}")

        connection.disconnect()