import sys

from backup import backup_devices
from vlan import deploy_vlans
from audit import run_audit

if len(sys.argv) < 2:

    print("Usage:")
    print("python netauto.py backup")
    print("python netauto.py vlan")
    print("python netauto.py audit")

else:

    command = sys.argv[1]

    if command == "backup":
        backup_devices()

    elif command == "vlan":
        deploy_vlans()

    elif command == "audit":
        run_audit()

    else:
        print("Unknown command")