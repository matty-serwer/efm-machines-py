import os

def generate_machine_simulator(machine_number, output_dir="."):
    filename = f"machine_simulator_{machine_number}.py"
    filepath = os.path.join(output_dir, filename)
    code = f'''
import socket
import json
import time
import random
from datetime import datetime

def generate_sensor_data():
    sensors = ["temperature", "pressure", "humidity"]
    units_map = {{"temperature": "°C", "pressure": "kPa", "humidity": "%"}}
    sensor = random.choice(sensors)
    value = round(random.uniform(20, 100), 2)
    return {{
        "timestamp": datetime.utcnow().isoformat(),
        "deviceId": "machine-{machine_number:03}",
        "sensorType": sensor,
        "value": value,
        "units": units_map[sensor]
    }}

def main():
    host = 'localhost'
    port = 9090  # Adjust as needed

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Connected to {{host}}:{{port}} from machine-{machine_number:03}")
            while True:
                data = generate_sensor_data()
                message = json.dumps(data) + "\\n"
                s.sendall(message.encode('utf-8'))
                print(f"Sent: {{message.strip()}}")
                time.sleep(2)
        except ConnectionRefusedError:
            print(f"Failed to connect to {{host}}:{{port}}")

if __name__ == "__main__":
    main()
    '''
    with open(filepath, "w") as file:
        file.write(code.strip())
    print(f"Generated {filename}")

def generate_multiple_machines(count, output_dir="."):
    for i in range(1, count + 1):
        generate_machine_simulator(i, output_dir)

# Example: Generate 5 machine simulators
generate_multiple_machines(5)