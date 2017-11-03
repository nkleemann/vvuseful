#! python3

"""Very, very simple Intrusion Detection Script.
	Detects MITM and DeAuth Attacks. (Linux, needs iwconfig)

	Usage: <wlanpolice.py> <iface>

	@Niklas Kleemann, 2017
"""

import time
import sys
from scapy.all import *

if len(sys.argv) < 2:
	print("Expected interface..")
	sys.exit(1)

iface = sys.argv[1]

mx_proberp  = 4
mx_deauth   = 8
deauth_time = 20
deauths     = {}
probe_resp  = {}


def handle_pkt(p):
	if p.haslayer(Dot11Deauth):
		deauths.setdefault(p.addr2, []).append(time.time())
		span = deauths[p.addr2][-1] - deauths[p.addr2][0]

		if len(deauths[pkt.addr2]) == mx_deauth and span <= deauth_time:
			print("[*] Got DeAuth from: %s" % (p.addr2))
			del deauths[pkt.addr2]

		elif p.haslayer(Dot11ProbeResp):
			probe_resp.setdefault(p.addr2, set()).add(p.info)

		if len(probe_resp[p.addr2]) == mx_proberp:
			print("[*] SSID Spoofing from: %s " % (pkt.addr2))

			for ssid in probe_resp[p.addr2]:
				print(ssid)

			print("")
			del probe_resp[p.addr2]



os.system("iwconfig " + iface + " mode monitor")
print("[*] Sniffing...")
sniff(iface=iface, prn=handle_pkt)