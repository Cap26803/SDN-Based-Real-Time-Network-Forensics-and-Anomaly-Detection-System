DDoS Attack Test on Mininet Topology
====================================

Overview
--------

This document provides the details and results of the DDoS attack simulation performed on the Mininet topology. The attack was targeted at host `h8` and distributed from multiple hosts (`h2`, `h4`, and `h6`) to simulate a Distributed Denial of Service (DDoS) attack.

Test Setup
----------

-   **Target Host**: `h8` (IP: `10.0.0.8`)
-   **Attacking Hosts**: `h2` (IP: `10.0.0.2`), `h4` (IP: `10.0.0.4`), `h6` (IP: `10.0.0.6`)
-   **Tools Used**:
    -   `iperf`: Used to generate high-traffic UDP flows.
    -   `flood`: Used to flood the network with packets for simulating a realistic DDoS attack.
-   **Objective**: To observe and analyze the effect of a DDoS attack on the network, specifically monitoring SYN traffic directed at `h8` using Wireshark.

Command Execution
-----------------

1.  **Start the iperf Server on `h8`**:

    `h8 iperf -s -u`

2.  **Initiate Traffic from Attacking Hosts**:

    -   **From `h2`**:

        `h2 iperf -c 10.0.0.8 -u -b 100M`

    -   **From `h4`**:

        `h4 iperf -c 10.0.0.8 -u -b 100M`

    -   **From `h6`**:

        `h6 iperf -c 10.0.0.8 -u -b 100M`

3.  **Flood Command for Additional Load**:

    `h3 flood 10.0.0.8
    h5 flood 10.0.0.8
    h7 flood 10.0.0.8`

Results and Observations
------------------------

### Terminal Output

-   The terminal output confirmed high traffic directed at `h8`, indicating the DDoS attack was effective.
-   A screenshot (`ddos_attack_network_flood.png`) of the terminal output captures the flooding activity.

### Network Analysis (Wireshark)

-   **Observed Traffic**: SYN packets and UDP traffic surges, consistent with a typical DDoS attack.
-   **Captured Data**: Wireshark log shows a high volume of SYN packets targeted at `h8`, reflecting successful flooding.

Conclusion
----------

The DDoS attack simulation was successful, with `h8` experiencing significant packet traffic, visible through Wireshark. This test serves as a foundation for further anomaly detection and forensics analysis in the SDN-based network.