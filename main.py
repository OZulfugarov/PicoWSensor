import requests
from machine import Pin, I2C
from time import sleep
import network
import bme280
import json

# WiFi credentials
SSID = "insert_yours"
PASSWORD = "insert_yours"
thing_name = "insert_yours"  # Replace with your dweet.io thing name

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)  # Station mode (client)
wifi.active(True)  # Activate the interface

if not wifi.isconnected():
    wifi.connect(SSID, PASSWORD)  # Connect to the WiFi network

    # Wait until the connection is established
    while not wifi.isconnected():
        print("Connecting to WiFi...")
        sleep(1)

    print("Connected to WiFi")
else:
    print("Already connected to WiFi")

# Establish I2C connection
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=10000)

# Function to send data to dweet.io
def send_data_to_dweet(data):
    dweet_url = f"https://dweet.io/dweet/for/{thing_name}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(dweet_url, headers=headers, json=data)

    if response.status_code == 200:
        print("Data sent successfully to dweet.io!")
    else:
        print("Failed to send data to dweet.io.")

# Function to read sensor data
def read_sensor_data():
    bme = bme280.BME280(i2c=i2c)
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    return {"temperature": temp, "humidity": hum, "pressure": pres}

# Continuous reading of sensor data and sending it to dweet.io
while True:
    sensor_data = read_sensor_data()
    sensor_reading = {
        "WiFi_status": "Connected" if wifi.isconnected() else "Not connected",
        "sensor_data": sensor_data
    }
    print(json.dumps(sensor_reading))  # Print sensor reading for verification

    send_data_to_dweet(sensor_reading)
    
    sleep(60)  # Adjust the delay as needed

