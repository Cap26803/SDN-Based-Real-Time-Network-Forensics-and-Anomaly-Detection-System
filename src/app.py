from flask import Flask, render_template, jsonify
import json
import time
import os

app = Flask(__name__)

# Path to the JSON log file
LOG_FILE = "/home/chinmay/Projects/SDN-Based-Real-Time-Network-Forensics-and-Anomaly-Detection-System/src/logs/detection_logs.json"

# Ensure the log file exists and is initialized
def initialize_log_file():
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)

# Endpoint to serve real-time data for chart updates
@app.route('/realtime_data')
def realtime_data():
    try:
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
            if logs:
                # Return only the latest log entry
                return jsonify(logs[-1])
            else:
                return jsonify({})
    except Exception as e:
        return jsonify({"error": str(e)})
        
# Endpoint to serve logs
@app.route('/logs')
def logs():
    try:
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
        return jsonify(logs)
    except Exception as e:
        return f"Error reading logs: {e}", 500


# Endpoint to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    initialize_log_file()  # Initialize the log file at the start
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run Flask app

