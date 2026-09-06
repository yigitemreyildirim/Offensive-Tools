# NyxaMacChanger

**NyxaMacChanger** is a Python-based utility designed to modify the Media Access Control (MAC) address of a network interface. This project is a practical tool for network security professionals and students to understand how hardware addresses are handled at the Data Link Layer (OSI Layer 2).

## ⚠️ Ethical & Legal Disclaimer
**This project is created strictly for educational and cybersecurity research purposes.** Changing a MAC address on systems without explicit authorization can violate network policies or terms of service. Use this tool only on your own hardware or in authorized testing environments. The developer assumes no responsibility for any misuse of this code.

## Overview
A MAC address is a unique identifier assigned to a network interface controller (NIC). Changing (spoofing) this address is a common technique used for:
* **Privacy:** Reducing the traceability of a device on a network.
* **Security Testing:** Bypassing MAC-based access control lists (ACLs) or network filtering.
* **Anonymity:** Performing authorized security audits without exposing the true hardware identity.

## Key Features
* **Interface Selection:** Allows the user to specify which network interface (e.g., `eth0`, `wlan0`) to modify.
* **Randomization:** Supports generating and applying a new, random MAC address.
* **Verification:** Displays the interface status before and after the change to confirm the operation was successful.

## How It Works
The script utilizes the Linux `subprocess` module to execute system-level commands that interact with the network interface configuration. It performs the following sequence:
1. **Shutdown:** Disables the network interface.
2. **Change:** Updates the MAC address using `ifconfig` or `ip` commands.
3. **Bring Up:** Re-enables the network interface to apply the changes.



## Setup & Usage
This tool requires root/administrator privileges to modify network interface settings.

```bash
# Clone the repository
git clone https://github.com/yigitemreyildirim/NyxaMacChanger
cd NyxaMacChanger

# Usage
sudo python3 nyxa_mac_changer.py -i <interface> -m <new_mac_address>

# Example (for random MAC generation)
sudo python3 nyxa_mac_changer.py -i eth0 -m random
