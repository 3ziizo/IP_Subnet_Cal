import ipaddress
print("Enter the ip address followed by the subnet mask\ne.g. 192.168.10.1/21")
a= input()
network = ipaddress.IPv4Network(a, strict=False)

print("Network Address:       ",network.network_address)
print("Broadcast Address:     ",network.broadcast_address)

print("Number of Hosts:       ",network.num_addresses)
print("Number of Usable Hosts:",network.num_addresses-2)
print("Subnet Mask:           ",network.netmask)
print("Wildcard Mask:         ",network.hostmask)

a=""

if network.is_global:
    a="Global"
elif network.is_private:
    a = "Private"
elif network.is_multicast:
    a = "Multicast"
elif network.is_loopback:
    a = "Loopback"
elif network.is_reserved:
    a = "reserved"
elif network.is_link_local:
    a = "Local"
else:
    a = "unspecified"

print("IP Type:               ", a)
