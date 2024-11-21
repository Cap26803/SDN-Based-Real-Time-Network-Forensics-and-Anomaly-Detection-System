from scapy.all import sniff, IP, TCP
from collections import defaultdict
import os
import time

# Initialize counters and parameters
syn_count = defaultdict(int)
ALERT_THRESHOLD = 100  # Customize this threshold based on expected traffic
TIME_WINDOW = 10       # Time window in seconds to reset counters

# Store the start time
start_time = time.time()

def block_ip(ip_address):
    # Command to block IP using iptables
    os.system(f"iptables -A INPUT -s {ip_address} -j DROP")
    print(f"Blocked IP: {ip_address} due to suspicious activity.")

def analyze_packet(packet):
    global start_time
    # Check if packet has IP and TCP layers
    if packet.haslayer(IP) and packet.haslayer(TCP):
        # Check if it's a SYN packet directed to host 8
        if packet[TCP].flags == 'S' and packet[IP].dst == '10.0.0.8':
            src_ip = packet[IP].src
            syn_count[src_ip] += 1  # Count SYN packet from each source IP

            # Check the time elapsed
            current_time = time.time()
            if current_time - start_time > TIME_WINDOW:
                # Calculate total SYNs in the time window
                total_syns = sum(syn_count.values())

                # Check if total SYNs exceed threshold
                if total_syns > ALERT_THRESHOLD:
                    print(f"Alert: Potential DDoS attack detected on host 8!")
                    print(f"Total SYN packets in the last {TIME_WINDOW} seconds: {total_syns}")
                    print("Blocking attacking IPs:")
                    
                    # Block each attacking IP
                    for ip, count in syn_count.items():
                        if count > ALERT_THRESHOLD / len(syn_count):  # Customize per-IP threshold if needed
                            block_ip(ip)

                # Reset counters for the next time window
                syn_count.clear()
                start_time = current_time

# Start continuous packet sniffing on host 8
print("Starting real-time DDoS detection and IP blocking on host 8...")
sniff(iface='h8-eth0', prn=analyze_packet)

