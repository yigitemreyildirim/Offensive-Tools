# NyxaKeylogger (Educational PoC)

**NyxaKeylogger** is a proof-of-concept (PoC) project designed to demonstrate the fundamental mechanisms of keystroke logging. This project is intended for cybersecurity researchers and students to understand how such software operates and, more importantly, to develop effective detection and defense strategies against these threats.

## ⚠️ Ethical & Legal Disclaimer
**This project is created strictly for educational and cybersecurity research purposes.** Using this code on any system without explicit authorization is illegal and can lead to severe legal consequences. Use this software only within isolated, controlled virtual environments that you have created yourself. The developer is not responsible for any misuse of this code.

## Overview
Keyloggers are a common form of spyware. By studying this PoC, you can learn:
* **Input Interception:** How libraries like `pynput` hook into system keyboard events.
* **Data Processing:** How captured keystrokes are processed and formatted in memory.
* **Data Exfiltration:** How automated scripts utilize protocols like SMTP to transmit data to a remote server.
* **Threat Detection:** How modern EDR (Endpoint Detection and Response) systems identify and block such processes.

## Key Features
* **Event Hooking:** Captures real-time keystrokes using `pynput`.
* **Standardization:** Converts special keys (Space, Enter, Backspace) into readable text.
* **Automated Exfiltration:** Includes a background thread that periodically emails captured data.
* **Lightweight Architecture:** Designed as a simple, easy-to-analyze structure for local laboratory testing.

## Security Best Practices
If you are building or contributing to this project, please adhere to these security standards:
1. **Environment Variables:** **Never hardcode** email credentials. Use `.env` files or system environment variables to manage sensitive data securely.
2. **Focus on Defense:** Treat this project as a laboratory experiment. Focus your research on how to detect this activity through process monitoring, network traffic analysis, and system logs.

## Contributing
This is an educational project. Contributions that focus on defensive measures, detection techniques, or code quality improvements are highly encouraged. Please submit a pull request if you wish to contribute.
