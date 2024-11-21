from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# Path to the JSON log file
LOG_FILE = "/home/chinmay/Projects/SDN-Based-Real-Time-Network-Forensics-and-Anomaly-Detection-System/src/logs/detection_logs.json"

@app.route('/')
def home():
    """Homepage with alert if logs exist."""
    alert = False
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        alert = True
    return render_template('index.html', alert=alert)

@app.route('/logs', methods=['GET'])
def get_logs():
    """Fetch logs from the JSON log file."""
    try:
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
            with open(LOG_FILE, 'r') as f:
                logs = json.load(f)
            return jsonify(logs), 200
        else:
            return jsonify({"message": "No logs available"}), 200
    except Exception as e:
        return jsonify({"error": f"Error reading logs: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

