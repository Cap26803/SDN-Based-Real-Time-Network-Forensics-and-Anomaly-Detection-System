import json
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import os
import time

# Initialize counters and parameters
syn_count = defaultdict(int)
ALERT_THRESHOLD = 100  # Customize this threshold based on expected traffic
TIME_WINDOW = 10       # Time window in seconds to reset counters

# Path to the JSON log file
LOG_FILE = "/home/chinmay/Projects/SDN-Based-Real-Time-Network-Forensics-and-Anomaly-Detection-System/src/logs/detection_logs.json"

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Store the start time
start_time = time.time()

def initialize_log_file():
    """Ensure the log file starts with valid JSON and set permissions."""
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        print(f"Initializing log file: {LOG_FILE}")
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)
        # Set permissions to 777
        os.chmod(LOG_FILE, 0o777)
        print(f"Set permissions to 777 for log file: {LOG_FILE}")

def write_to_log(log_entry):
    """Append a log entry to the JSON log file."""
    try:
        with open(LOG_FILE, 'r+') as f:
            logs = json.load(f)  # Load existing logs
            logs.append(log_entry)  # Add the new entry
            f.seek(0)  # Move to the beginning of the file
            json.dump(logs, f, indent=4)  # Write updated logs
    except Exception as e:
        print(f"Error writing to log file: {e}")

def analyze_packet(packet):
    global start_time
    # Check if packet has IP and TCP layers
    if packet.haslayer(IP) and packet.haslayer(TCP):
        if packet[TCP].flags == 'S' and packet[IP].dst == '10.0.0.8':
            src_ip = packet[IP].src
            syn_count[src_ip] += 1

            # Check the time elapsed
            current_time = time.time()
            if current_time - start_time > TIME_WINDOW:
                total_syns = sum(syn_count.values())
                if total_syns > ALERT_THRESHOLD:
                    log_entry = {
                        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                        "alert": "Potential DDoS attack detected on host 8!",
                        "total_syns": total_syns,
                        "sources": dict(syn_count)
                    }
                    print("Alert detected:", log_entry)
                    write_to_log(log_entry)
                syn_count.clear()
                start_time = current_time

# Initialize the log file at the start
initialize_log_file()

print("Starting real-time DDoS detection and logging on host 8...")
sniff(iface='h8-eth0', prn=analyze_packet)
