from scapy.all import *

sniff(prn=lambda x: print(x), count=1)
#sniff(prn=lambda x: x.show(), count=1)