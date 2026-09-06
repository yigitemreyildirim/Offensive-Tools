# NyxaNetScanner

**NyxaNetScanner** is a network discovery tool developed in Python to identify active devices on a local area network (LAN). This project serves as an educational resource for cybersecurity researchers and students interested in understanding network protocols (specifically ARP) and network reconnaissance techniques.

## ⚠️ Ethical & Legal Disclaimer
**This project is created strictly for educational and cybersecurity research purposes.** Performing network scans on systems or networks without explicit authorization is illegal. Use this software only within your own network or in isolated, authorized lab environments. The developer assumes no responsibility for any misuse of this code.

## Overview
Network scanning is a fundamental step in both offensive and defensive security operations. By studying this tool, you can analyze:
* **Active Host Discovery:** Efficiently listing devices connected to the local network.
* **IP-to-MAC Mapping:** Correlating IP addresses with their physical (MAC) hardware addresses.
* **Network Reconnaissance:** Gaining visibility into the topography of a specific subnet.

## Key Features
* **ARP Scanning:** Uses the Address Resolution Protocol (ARP) for faster and more reliable device detection compared to traditional ICMP (ping) sweeps.
* **Scapy Integration:** Built using the powerful `scapy` library for low-level packet crafting and manipulation.
* **Structured Output:** Displays discovered devices in a clear format to facilitate network auditing.

## How It Works
The scanner sends an ARP request packet to every IP address within the specified range. When a device receives an ARP request for its IP, it responds with its MAC address. `NyxaNetScanner` listens for these responses and reports the active assets found on the network.

## Setup & Usage
To run this tool locally, ensure you have the necessary dependencies:

```bash
# Clone the repository
git clone https://github.com/yigitemreyildirim/NyxaNetScanner
cd NyxaNetScanner

# Install dependencies
pip install scapy

# Usage (Requires root/sudo privileges for raw socket access)
sudo python3 nyxa_net_scanner.py -t <IP_RANGE>
