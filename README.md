# SDN-Based Real-Time Network Forensics and Anomaly Detection System

This project leverages Software-Defined Networking (SDN) principles to monitor, detect, and respond to network traffic anomalies in real-time. The goal is to enhance network security, provide effective forensic analysis, and offer an intuitive dashboard for visualizing threats dynamically.

## Features
- Real-time network traffic monitoring using Mininet and SDN controllers.
- Anomaly detection focused on detecting SYN flood DDoS attacks.
- Alerts displayed both on the web interface and terminal.
- Traffic flow logging in JSON format for forensic analysis.
- Visualizations of threat data using real-time charts (line and pie charts) on a responsive Flask web interface.
- Easy navigation to view detailed logs and traffic summaries.

## Tools Used
- **Mininet**: For network emulation.
- **Custom SDN Controller**: For managing network traffic and implementing security policies.
- **Scapy**: For capturing and analyzing packets.
- **Wireshark**: For detailed packet inspection and validation.
- **Flask**: For a lightweight, responsive web interface.
- **Chart.js**: For dynamic chart visualizations on the web interface.

## Documentation
- [Project Documentation](./docs/Project_Documentation.md)

## How to Run
1. **Prerequisites**:
   - Ubuntu 22.04 environment (virtual machine recommended).
   - Python 3.10.6 installed with necessary libraries.
   - Mininet installed and configured.
   - `hping3`, `iperf`, and other required network tools installed.

2. **Steps**:
   - Launch the Mininet topology using the provided configuration.
   - Run the `realtime_attack_detection.py` script on the target host (e.g., h8).
   - Start the Flask server using `app.py` for real-time monitoring.
   - Generate traffic (e.g., using `hping3` or `iperf`) to simulate DDoS attacks and observe detections.
   - Navigate to the Flask web interface for visualizations and logs.

3. **Features in Action**:
   - Alerts for anomalies will appear on the web interface and logs.
   - Dynamic charts show SYN flood rates and attack sources in real-time.

---
