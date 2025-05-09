import socket
import json
import time
import random
from datetime import datetime

def generate_sensor_data():
    sensors = ["temperature", "pressure", "humidity"]
    units_map = {"temperature": "°C", "pressure": "kPa", "humidity": "%"}
    sensor = random.choice(sensors)
    value = round(random.uniform(20, 100), 2)
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "deviceId": "machine-002",
        "sensorType": sensor,
        "value": value,
        "units": units_map[sensor]
    }

def main():
    host = 'localhost'
    port = 9090  # Adjust as needed

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Connected to {host}:{port} from machine-002")
            while True:
                data = generate_sensor_data()
                message = json.dumps(data) + "\n"
                s.sendall(message.encode('utf-8'))
                print(f"Sent: {message.strip()}")
                time.sleep(2)
        except ConnectionRefusedError:
            print(f"Failed to connect to {host}:{port}")

if __name__ == "__main__":
    main()