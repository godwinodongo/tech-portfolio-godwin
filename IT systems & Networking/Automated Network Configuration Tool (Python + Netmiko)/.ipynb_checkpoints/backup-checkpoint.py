from netmiko import ConnectHandler
from datetime import datetime
from devices import devices

def backup_devices():

    for router in devices:

        print(f"Connecting to {router['host']}")

        connection = ConnectHandler(**router)

        config = connection.send_command("/export")

        time = datetime.now().strftime("%Y-%m-%d_%H-%M")

        filename = f"backup_{router['host']}_{time}.rsc"

        with open(filename, "w") as file:
            file.write(config)

        print("Backup saved:", filename)

        connection.disconnect()