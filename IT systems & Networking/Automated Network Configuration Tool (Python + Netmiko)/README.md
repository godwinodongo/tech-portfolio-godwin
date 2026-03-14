# Network Automation Toolkit (Python + Netmiko)

A Python-based network automation toolkit designed to manage MikroTik routers using SSH automation.

This project demonstrates how network engineers can automate common operational tasks such as configuration backups, VLAN deployment, and compliance auditing across multiple devices.

---

## Project Overview

Managing network devices manually becomes inefficient and error-prone as infrastructure grows. This toolkit automates repetitive tasks using Python and Netmiko, allowing engineers to interact with routers programmatically.

The tool connects to devices via SSH and executes RouterOS commands automatically.

---

## Features

### 1. Automated Configuration Backup

Creates timestamped backups of router configurations.

Command:

```
python netauto.py backup
```

Output example:

```
Backup saved: backup_192.168.100.11_2026-03-14_10-20.rsc
```

---

### 2. VLAN Deployment Automation

Automatically creates VLAN interfaces across devices.

Command:

```
python netauto.py vlan
```

Example VLANs deployed:

* VLAN10 – SALES
* VLAN20 – HR
* VLAN30 – CCTV

---

### 3. Network Compliance Audit

Checks network configuration against required standards.

Command:

```
python netauto.py audit
```

Example output:

```
Auditing 192.168.100.11
✔ SSH enabled
✔ DNS configured
✔ VLAN10 exists
```

---

## Project Architecture

```
network-automation-toolkit
│
├── devices.py        # Network device inventory
├── backup.py         # Configuration backup module
├── vlan.py           # VLAN automation module
├── audit.py          # Compliance auditing module
├── netauto.py        # Main CLI automation tool
│
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Technologies Used

* Python
* Netmiko
* SSH Automation
* MikroTik RouterOS

---

## Requirements

Python 3.8+

Install dependencies:

```
pip install -r requirements.txt
```

---

## Device Inventory

Devices are defined inside:

```
devices.py
```

Example:

```
devices = [
    {
        "device_type": "mikrotik_routeros",
        "host": "192.168.100.11",
        "username": "admin",
        "password": ""
    }
]
```

Multiple routers can be added to automate larger networks.

---

## Example Use Cases

This toolkit can be used for:

* Automated router configuration backups
* VLAN deployment across branch networks
* Infrastructure compliance auditing
* Network operations automation

---

## Future Improvements

Planned enhancements:

* Parallel execution for faster automation
* HTML compliance reporting
* Scheduled backups
* CSV/JSON device inventory
* Configuration version control

---

## Author: Odongo Oduor Godwin

Network Automation Project built using Python and Netmiko for infrastructure management.

---
