from netmiko import ConnectHandler
from devices import devices

def run_audit():

    for router in devices:

        print("\nAuditing:", router["host"])

        connection = ConnectHandler(**router)

        ssh = connection.send_command("/ip service print")

        if "ssh" in ssh:
            print("✔ SSH enabled")
        else:
            print("✖ SSH missing")

        dns = connection.send_command("/ip dns print")

        if "servers" in dns:
            print("✔ DNS configured")
        else:
            print("✖ DNS missing")

        connection.disconnect()