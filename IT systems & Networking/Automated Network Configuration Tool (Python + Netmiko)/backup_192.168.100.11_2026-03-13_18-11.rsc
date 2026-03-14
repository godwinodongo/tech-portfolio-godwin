# 2026-03-13 21:12:02 by RouterOS 7.21.3
# software id = DYID-QKTZ
#
# model = RB951Ui-2HnD
# serial number = 8A3709BCA6B2
/interface bridge
add name=server
/interface wireless
set [ find default-name=wlan1 ] disabled=no mode=station-pseudobridge ssid="KeringNet Hotspot"
/interface vlan
add interface=server name=vlan10 vlan-id=10
add interface=server name=vlan20 vlan-id=20
add interface=server name=vlan30 vlan-id=30
add interface=server name=vlan40 vlan-id=40
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool1 ranges=192.168.100.2-192.168.100.254
add name=dhcp_pool2 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool3 ranges=192.168.10.2-192.168.10.254
/ip dhcp-server
add address-pool=dhcp_pool3 interface=server name=dhcp1
/interface bridge port
add bridge=server interface=ether2
/ip address
add address=192.168.10.1/24 interface=server network=192.168.10.0
/ip dhcp-client
add default-route-tables=main interface=ether1
/ip dhcp-server network
add address=192.168.10.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.10.1
add address=192.168.100.0/24 dns-server=192.168.100.1,8.8.8.8 gateway=192.168.100.1
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1
/system clock
set time-zone-name=Africa/Nairobi