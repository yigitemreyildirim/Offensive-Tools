# must be root
# The code required to run: python nyxa_net_scanner.py -i 192.168.1.1/24
# For python3 = pip3 install scapy

import scapy.all as scapy
import optparse as opt

def getUserInput():
    parse_object = opt.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Enter IP address")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Please enter an IP address")
        exit()

    return user_input



def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    brodcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = brodcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()



user_ip_address = getUserInput().ip_address
scan_network(user_ip_address)


