# Real-Time DDoS Attack Detection Test

## Overview

This test demonstrates real-time detection of a distributed SYN flood DDoS attack on host `h8` in the Mininet network. We use a custom Python script (`realtime_ddos_detection.py`) that monitors incoming SYN packets to identify potential DDoS attacks and provides alerts when SYN packet counts exceed a specified threshold.

## Topology Setup

The network topology consists of:
- **Controller**: `c0` (Protocol: TCP, Port: 6633)
- **Switches**: `s1`, `s2`, `s3`, `s4`
- **Hosts**: `h1` to `h8` with IPs `10.0.0.1` to `10.0.0.8`
  
Link structure between switches and hosts:
- **Switch-to-Switch Links**: `s1 <-> s2`, `s2 <-> s3`, `s3 <-> s4`
- **Switch-to-Host Links**: `s1 <-> h1`, `s1 <-> h2`, `s2 <-> h3`, `s2 <-> h4`, `s3 <-> h5`, `s3 <-> h6`, `s4 <-> h7`, `s4 <-> h8`

Refer to the main topology script (`main_topology.py`) for detailed topology creation.

## Steps for Real-Time Detection Test

1. **Start Network Topology**: Run the `main_topology.py` script to initiate the network and ensure connectivity.
   
2. **Run Detection Script on h8**:
   - Use Mininet's `xterm` command to open a terminal for `h8` and execute `realtime_ddos_detection.py`:
     ```bash
     sudo python3 realtime_ddos_detection.py
     ```
   - The script will begin monitoring for SYN packets directed to `h8` and will alert if SYN traffic exceeds the threshold.

3. **Basic Reachability Test**:
   - From host `h1`, ping `h8` to confirm network reachability:
     ```bash
     ping 10.0.0.8
     ```

4. **Simulate DDoS Attack**:
   - From hosts `h2`, `h4`, and `h6`, run a SYN flood attack targeting `h8` using `hping3`:
     ```bash
     hping3 -S --flood -p 80 10.0.0.8
     ```

5. **Observation**:
   - Monitor the output on `h8` where `realtime_ddos_detection.py` is running. If SYN packets exceed the alert threshold, the script will print a DDoS alert message, detailing the source IPs and the packet count for each.

6. **Capture SYN Flood Traffic (Optional)**:
   - Open Wireshark on `h8` to capture and analyze SYN traffic.

## Expected Outcome

- **DDoS Alert**: The `realtime_ddos_detection.py` script should detect a SYN flood and display an alert with the source IP addresses and packet counts.