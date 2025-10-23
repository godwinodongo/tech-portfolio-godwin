<H1>🏢 Enterprise Network Infrastructure Lab</H1>

<b>Author: Godwin Odongo

Tools: Cisco Packet Tracer 8.2, pfSense, Draw.io, Windows Server

Status: Completed ✅

Date: May 2025</b>


<b>🔧 Project Overview</b>

This project simulates a multi-site enterprise network connecting an HQ and Branch via a site-to-site VPN.
It demonstrates VLAN segmentation, centralized DHCP, inter-VLAN routing, and secure communication between sites — a realistic model of how large companies manage distributed networks.

<b>🧩 Network Objectives</b>

Design scalable VLAN-based LANs for HQ and Branch sites.

Centralize DHCP service at HQ while relaying requests from Branch.

Implement Router-on-a-Stick for inter-VLAN routing.

Configure static routing and simulate VPN between sites.

Verify cross-site communication and DNS resolution.

<b>🌐 Topology</b>

<b>HQ Site:</b>

VLAN10 – IT (192.168.10.0/24)

VLAN20 – HR (192.168.20.0/24)

VLAN30 – Production (192.168.30.0/24)

DHCP/DNS Server – 192.168.10.10

pfSense Gateway – 172.16.1.1

<b>Branch Site:</b>

VLAN40 – SALES (192.168.40.0/24)

VLAN50 – ACC (192.168.50.0/24)

VLAN60 – SEC (192.168.60.0/24)

R2-Branch Router with IP Helper to HQ DHCP

Site-to-Site VPN via 10.0.0.0/30 link

<b>⚙️ Key Configurations</b>

<b>HQ Router (Router0):</b>

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

<b>Branch Router (R2):</b>

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

<b>📡 Testing & Validation</b>

✅ PCs in all VLANs automatically receive IPs from centralized DHCP server.

✅ Inter-VLAN communication verified via router-on-a-stick.

✅ Successful pings from Branch VLAN PCs to HQ server (192.168.10.10).

✅ VPN (10.0.0.0/30) stable for site-to-site traffic.

✅ DHCP leases visible from HQ DHCP management console.


<b>🚀 Skills Demonstrated</b>

VLAN design & segmentation

DHCP relay and centralized IP management

Router-on-a-Stick and static routing

VPN and WAN design

Enterprise network documentation

Troubleshooting and verification methodology


<b>🧠 Lessons Learned</b>

The importance of IP helper-address for cross-site DHCP.

How routing and VLAN tagging work together for scalability.

Designing networks for redundancy and centralized control.


<b>📂 Project Files</b>

<a href="https://github.com/godwinodongo/tech-portfolio-godwin/raw/refs/heads/main/enterprise-network-infrastructure-lab/packet_tracer/enterprise_network_lab.pkt" target="_blank">Packet Tracer Simulation</a>

<a href="/configs" target="_blank">Router & Switch Configs</a>

<a href="/tests" target="_blank">Testing Results</a>


<b>🏁 Future Enhancements</b>

Add OSPF routing for dynamic route updates.

Integrate Syslog and SNMP monitoring.

Implement redundancy with HSRP/VRRP.

<b>📊 Screenshots</b>

Topology
<img width="1811" height="675" alt="Topology" src="https://github.com/user-attachments/assets/68fe7bcd-1c8d-4b6b-88a5-2635b476ed2f" />

DHCP leases
<img width="873" height="889" alt="image" src="https://github.com/user-attachments/assets/7a1787b6-6922-46df-9880-52ac9b6d46a8" />

Successful ping between sites
<img width="878" height="891" alt="image" src="https://github.com/user-attachments/assets/2500e697-f93b-4082-8584-fb10c75ce8c1" />

<img width="879" height="890" alt="image" src="https://github.com/user-attachments/assets/0af2c4a2-9e99-47bb-a24b-a8ee8baa7037" />

<img width="880" height="885" alt="image" src="https://github.com/user-attachments/assets/4be8e98f-6ae1-49cd-ad67-affbab135bec" />

<img width="877" height="888" alt="image" src="https://github.com/user-attachments/assets/bfe5483f-b1de-4ef9-8177-5851d5641b3d" />
VLAN config output
<img width="872" height="891" alt="image" src="https://github.com/user-attachments/assets/b55b9978-618f-4a45-99ec-1ffbf5d9de5a" />

<img width="869" height="889" alt="image" src="https://github.com/user-attachments/assets/c79a10d6-a554-479c-8f5d-163f5b252a8d" />
Router routes
<img width="880" height="887" alt="image" src="https://github.com/user-attachments/assets/86d1aa6a-a0af-4f58-a571-168281be60da" />

<img width="874" height="882" alt="image" src="https://github.com/user-attachments/assets/f38817d0-8948-40c7-a84a-6bef909a5fdf" />


<img width="879" height="886" alt="image" src="https://github.com/user-attachments/assets/8946e2b9-9dd7-46da-8efb-8eeabe6ad472" />

Traceroute via VPN link
<img width="864" height="890" alt="image" src="https://github.com/user-attachments/assets/70f6c745-389f-42e6-8e02-0653f377aab5" />











