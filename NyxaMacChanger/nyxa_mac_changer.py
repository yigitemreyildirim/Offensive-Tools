# Note: you must be root
# The code required to run: python3 nyxa_mac_changer.py
import subprocess
import optparse
import re

def getUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", default="eth0",help="Interface to change mac address")
    parse_object.add_option("-m", "--mac", dest="mac_address", default="00:11:22:33:33:55", help="new mac address")
    return parse_object.parse_args()

def changeMacAddress(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])
    subprocess.call(["clear"])

def controlNewMac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig",interface]).decode()
    new_mac = re.search(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}",ifconfig_output)
    if new_mac:
        return new_mac.group(0)
    else:
        return None


def displayInfo():
    print("[+]Nyxa Mac Changer Started")

    (user_input, arguments) = getUserInput()
    changeMacAddress(user_input.interface, user_input.mac_address)
    finalized_mac = controlNewMac(user_input.interface)

    if finalized_mac == user_input.mac_address:
        print("[+]Mac Address Changed Successfully")
        print("=" * 32)
        print(f"Interface of the changed MAC address: {user_input.interface}")
        print(f"Changed mac address: {user_input.mac_address}")
        print("=" * 50)
        subprocess.call(["ifconfig",user_input.interface])
        print("=" * 75)
    else:
        print("[+]Mac Address Changed Failed")
        print("=" * 32)

displayInfo()
