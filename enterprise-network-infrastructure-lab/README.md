🏢 Enterprise Network Infrastructure Lab

Author: Godwin Oduor
Tools: Cisco Packet Tracer 8.2, pfSense, Draw.io, Windows Server
Status: Completed ✅
Date: May 2025

🔧 Project Overview

This project simulates a multi-site enterprise network connecting an HQ and Branch via a site-to-site VPN.
It demonstrates VLAN segmentation, centralized DHCP, inter-VLAN routing, and secure communication between sites — a realistic model of how large companies manage distributed networks.

🧩 Network Objectives

Design scalable VLAN-based LANs for HQ and Branch sites.

Centralize DHCP service at HQ while relaying requests from Branch.

Implement Router-on-a-Stick for inter-VLAN routing.

Configure static routing and simulate VPN between sites.

Verify cross-site communication and DNS resolution.

🌐 Topology

HQ Site:

VLAN10 – IT (192.168.10.0/24)

VLAN20 – HR (192.168.20.0/24)

VLAN30 – Production (192.168.30.0/24)

DHCP/DNS Server – 192.168.10.10

pfSense Gateway – 172.16.1.1

Branch Site:

VLAN40 – SALES (192.168.40.0/24)

VLAN50 – ACC (192.168.50.0/24)

VLAN60 – SEC (192.168.60.0/24)

R2-Branch Router with IP Helper to HQ DHCP

Site-to-Site VPN via 10.0.0.0/30 link

⚙️ Key Configurations
HQ Router (Router0):
interface g0/1.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface g0/1.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0

interface g0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0

interface g0/1.99
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0

interface g0/0
 ip address 172.16.1.2 255.255.255.252
 ip route 0.0.0.0 0.0.0.0 172.16.1.1

Branch Router (R2):
interface g0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ip helper-address 192.168.10.10

interface g0/0.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ip helper-address 192.168.10.10

interface g0/0.60
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ip helper-address 192.168.10.10

interface g0/1
 ip address 10.0.0.2 255.255.255.252
 ip route 0.0.0.0 0.0.0.0 10.0.0.1

📡 Testing & Validation

✅ PCs in all VLANs automatically receive IPs from centralized DHCP server.

✅ Inter-VLAN communication verified via router-on-a-stick.

✅ Successful pings from Branch VLAN PCs to HQ server (192.168.10.10).

✅ VPN (10.0.0.0/30) stable for site-to-site traffic.

✅ DHCP leases visible from HQ DHCP management console.

📊 Screenshots

VLAN Configuration on Switch

DHCP Lease Table on HQ Server

Ping Test from Branch PC → HQ Server

Traceroute via VPN link


🚀 Skills Demonstrated

VLAN design & segmentation

DHCP relay and centralized IP management

Router-on-a-Stick and static routing

VPN and WAN design

Enterprise network documentation

Troubleshooting and verification methodology


🧠 Lessons Learned

The importance of IP helper-address for cross-site DHCP.

How routing and VLAN tagging work together for scalability.

Designing networks for redundancy and centralized control.


📂 Project Files

Packet Tracer Simulation

Router & Switch Configs

Testing Results


🏁 Future Enhancements

Add OSPF routing for dynamic route updates.

Integrate Syslog and SNMP monitoring.

Implement redundancy with HSRP/VRRP.
