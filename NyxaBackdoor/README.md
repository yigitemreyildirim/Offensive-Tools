# Remote Command & File Control System (RAT-PoC)

This project is a Proof of Concept (PoC) demonstrating a client-server architecture for remote system administration using Python. It enables command execution and bidirectional file transfer over a TCP socket.

## Features

* **TCP Socket Communication:** Reliable data exchange between controller and target.
* **Remote Command Execution:** Execute shell commands on the target machine in real-time.
* **File Management:** * `download`: Retrieve files from the target machine.
    * `upload`: Send files to the target machine.
* **Data Serialization:** Uses `simplejson` for robust data packaging and `base64` for binary file transfer integrity.



[Image of client-server network architecture diagram]


## Architecture

* **`nyxa_socket_listener.py` (Controller):** The server-side script that listens for incoming connections and sends commands.
* **`nyxa_connection_socket.py` (Target):** The client-side script that executes system commands via `subprocess` and returns output.

## Setup & Usage

1. **Configure Network:** Edit the IP and Port in both `nyxa_socket_listener.py` and `nyxa_connection_socket.py` to match your local network settings.
2. **Start Listener:** ```bash
   python nyxa_socket_listener.py
3. **Start backdoor:** ```bash
   python nyxa_connection_socket.py
   
## Legal Disclaimer
This tool is intended strictly for educational purposes and ethical security research. It should only be used in controlled environments or on systems where you have explicit authorization. The developer assumes no responsibility for any misuse or illegal activities conducted with this software.
