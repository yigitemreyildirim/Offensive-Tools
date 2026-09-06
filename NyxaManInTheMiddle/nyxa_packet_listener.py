#pip3 install scapy_http

import scapy.all as scapy
from scapy_http  import http

def handle_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_the_packets)

def analyze_the_packets(packet):
    packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)




handle_packet("eth0")
