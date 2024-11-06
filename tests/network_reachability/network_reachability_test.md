Network Reachability Test for Mininet Topology
==============================================

Overview
--------

This document details the reachability test conducted on the Mininet topology using the specified Python script.

### Script Path

`topology/main_topology.py`

The topology includes a single SDN controller and four switches, each connected to a set of hosts. We verified network connectivity by running the `pingall` command in the Mininet CLI.

* * * * *

Topology Structure
------------------

-   **Controller**: `c0`

    -   Protocol: **TCP**
    -   Port: **6633**
-   **Switches**:

    -   `s1`, `s2`, `s3`, `s4`
-   **Hosts**:

    -   `h1` - `h8` with IP addresses ranging from `10.0.0.1` to `10.0.0.8`
-   **Links**:

    -   **Switch-to-Switch** connections:
        -   `s1 <-> s2`
        -   `s2 <-> s3`
        -   `s3 <-> s4`
    -   **Switch-to-Host** connections:
        -   `s1 <-> h1`, `s1 <-> h2`
        -   `s2 <-> h3`, `s2 <-> h4`
        -   `s3 <-> h5`, `s3 <-> h6`
        -   `s4 <-> h7`, `s4 <-> h8`

* * * * *

Test Execution
--------------

To verify network reachability among all hosts, the following command was executed within the Mininet CLI:

`pingall`

### Expected Outcome

Each host should be able to reach every other host if the topology and links are functioning correctly.