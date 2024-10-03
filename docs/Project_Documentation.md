# SDN-Based Real-Time Network Forensics and Anomaly Detection System

This document provides a comprehensive overview of the project, including its problem statement, objectives, tools used, functional and non-functional requirements, and system architecture.

---

## 1. Introduction

In today’s increasingly interconnected world, the security of network infrastructures is paramount. This project addresses the need for proactive security measures by leveraging Software-Defined Networking (SDN) to monitor network traffic in real-time, detect anomalies, and automate threat mitigation. With a web-based dashboard, the system provides intuitive visualization and forensic analysis capabilities.

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

3. **Automated Response**: Upon detecting an anomaly, the SDN controller should modify flow rules to block or mitigate malicious traffic.

4. **Web Dashboard**: The system must provide a web-based dashboard that visualizes traffic data, displays alerts, and enables forensic analysis.

5. **API for External Integration**: The system should expose APIs to allow external systems or tools to retrieve traffic logs and anomaly alerts.

### 5.2 Non-Functional Requirements

1. **Scalability**: The system should be able to handle a large number of traffic flows and scale as the network grows.

2. **Performance**: The system must detect anomalies and respond to them with minimal delay to maintain real-time functionality.

3. **Security**: The system should ensure that logs and sensitive data are protected from unauthorized access.

4. **Usability**: The dashboard should be intuitive and easy for security analysts to use, offering clear visualizations and actionable insights.

5. **Reliability**: The system should have minimal downtime and ensure consistent traffic logging and anomaly detection.

---

## 6. System Architecture

The architecture of the SDN-Based Real-Time Network Forensics and Anomaly Detection System consists of several key components working in conjunction to provide comprehensive monitoring, detection, and response capabilities. The following diagram illustrates the high-level architecture:

![NFAD-Context-Diagram](https://github.com/user-attachments/assets/41f3f65e-2f78-4cda-9fea-9c12eb9b6840)

![NFAD-Activity-Diagram](https://github.com/user-attachments/assets/4131bb92-eec7-48a9-840d-28e6c9ae58eb)

![NFAD-Sequence-Diagram](https://github.com/user-attachments/assets/e28cacbd-e90e-4cc1-b403-aa9af3cfe74f)


### Components:

1. **Mininet**: Acts as the virtual network environment, simulating real network scenarios for testing and analysis.

2. **Ryu SDN Controller**: Serves as the central control point for managing the network flow and responding to detected anomalies.

3. **Wireshark**: Utilized for capturing and analyzing network traffic, providing visibility into the flow of data across the network.

4. **Scapy**: Responsible for packet manipulation, including crafting and sending packets to test the network, as well as responding to anomalies detected in the traffic.

5. **Django/Flask Web Dashboard**: Offers a user-friendly interface for visualizing network data, alerts, and facilitating forensic analysis.

---

## 7. Project Summary

This project leverages SDN technology to offer real-time network forensics and anomaly detection. It enhances network security by monitoring and responding to threats like DDoS attacks and port scans. The use of tools like Mininet for simulation, Ryu for control, Wireshark for analysis, and Scapy for response ensures that the system offers robust monitoring and mitigation features. Additionally, the Django/Flask web interface provides easy access to traffic data and alerts, enabling quick responses and comprehensive forensic analysis.

---

This document serves as the initial foundation for the **SDN-Based Real-Time Network Forensics and Anomaly Detection System** project. It will evolve as the project progresses, adding details about implementation, architecture, and testing.
