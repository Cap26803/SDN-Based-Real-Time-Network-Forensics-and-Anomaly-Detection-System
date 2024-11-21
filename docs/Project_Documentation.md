# SDN-Based Real-Time Network Forensics and Anomaly Detection System

This document provides a comprehensive overview of the project, including its problem statement, objectives, tools used, functional and non-functional requirements, and system architecture.

---

## 1. Introduction

In today’s increasingly interconnected world, the security of network infrastructures is paramount. This project addresses the need for proactive security measures by leveraging Software-Defined Networking (SDN) to monitor network traffic in real-time and detect anomalies. With a web-based dashboard, the system provides intuitive visualization and forensic analysis capabilities.

---

## 2. Problem Statement

This project aims to develop an SDN-based system that provides real-time network forensics and anomaly detection to enhance the security and visibility of network traffic. The system will log traffic flows, detect anomalies such as DDoS attacks, and allow for immediate forensic analysis and mitigation of security threats through an intuitive web-based dashboard.

---

## 3. Objectives

- To design and implement a real-time network forensics system using SDN that logs network traffic flows and detects security anomalies.
- To provide a user-friendly web-based interface that visualizes network traffic data, alerts on detected anomalies, and enables rapid forensic analysis and response.

---

## 4. Tools Used

1. **Mininet**: For simulating virtual networks.
2. **Ryu SDN Controller**: To manage real-time network flow.
3. **Wireshark**: To capture and analyze network traffic.
4. **Scapy**: Used for packet manipulation and responding to anomalies.
5. **Django/Flask**: For building a web-based dashboard.

---

## 5. Requirements

### 5.1 Functional Requirements

1. **Traffic Flow Logging**: The system must log all network traffic flows in real-time using the SDN controller.
   
2. **Anomaly Detection**: The system must detect security anomalies such as DDoS attacks and port scans.

3. **Web Dashboard**: The system must provide a web-based dashboard that visualizes traffic data, displays alerts, and enables forensic analysis.

### 5.2 Non-Functional Requirements

1. **Scalability**: The system should be able to handle a large number of traffic flows and scale as the network grows.

2. **Performance**: The system must detect anomalies and respond to them with minimal delay to maintain real-time functionality.

3. **Security**: The system should ensure that logs and sensitive data are protected from unauthorized access.

4. **Usability**: The dashboard should be intuitive and easy for security analysts to use, offering clear visualizations and actionable insights.

5. **Reliability**: The system should have minimal downtime and ensure consistent traffic logging and anomaly detection.

---

## 6. System Architecture

The architecture of the SDN-Based Real-Time Network Forensics and Anomaly Detection System consists of several key components working in conjunction to provide comprehensive monitoring, detection capabilities. The following diagrams illustrate the high-level architecture:

### 6.1 Context Diagram
![NFAD-Context-Diagram](https://github.com/user-attachments/assets/31ef20c3-965f-4d50-b147-c4c916cac222)

### 6.2 Activity Diagram
![NFAD-Activity-Diagram](https://github.com/user-attachments/assets/c254ffc9-af61-452e-900d-befa45d3376d)

### 6.3 Sequence Diagram
![NFAD-Sequence-Diagram](https://github.com/user-attachments/assets/d566c6af-6d9e-42a9-ae6c-f578be17410b)

### Components:

1. **Mininet**: Acts as the virtual network environment, simulating real network scenarios for testing and analysis.

2. **SDN Controller**: Serves as the central control point for managing the network flow and responding to detected anomalies.

3. **Wireshark**: Utilized for capturing and analyzing network traffic, providing visibility into the flow of data across the network.

4. **Scapy**: Responsible for packet manipulation, including crafting and sending packets to test the network, as well as responding to anomalies detected in the traffic.

5. **Flask Web Dashboard**: Offers a user-friendly interface for visualizing network data, alerts, and facilitating forensic analysis.

---
## 7. Implementation Details

-   **Topology Setup**: The Mininet topology includes multiple hosts and switches controlled by a custom SDN controller.
-   **Real-Time Monitoring**: The `realtime_attack_detection.py` script captures packets on the target host and logs anomalies.
-   **Web Interface**: Flask renders dynamic charts using Chart.js for easy threat visualization.

Usage Instructions
------------------

1.  Set up the Mininet topology and SDN controller.
2.  Deploy the anomaly detection script on the target host.
3.  Start the Flask server to visualize network traffic in real-time.
4.  Use `iperf` or `hping3` to simulate network attacks and observe system responses.

---

## 8. Project Summary

This project leverages SDN technology to offer real-time network forensics and anomaly detection. It enhances network security by monitoring threats like DDoS attacks or port scans. The use of tools like Mininet for simulation, SDN for control, Wireshark for analysis, and Scapy for traffic generation and anomaly detection ensures that the system offers robust monitoring features. Additionally, the Flask web interface provides easy access to traffic data and alerts, enabling quick responses and comprehensive forensic analysis.

---

### Contributors:
   - Chinmay Paranjape
   - Chandsab Engineer
   - Kushal Kaparatti
   - Prathamesh Chitnis
