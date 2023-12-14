# Raspberry Pi Pico BME280 Sensor Data to dweet.io

This simple Python script is designed for the Raspberry Pi Pico microcontroller equipped with a BME280 sensor to read temperature, humidity, and pressure data and send it to dweet.io, a simple messaging service for connected devices.

## Requirements

- Raspberry Pi Pico
- BME280 sensor
- MicroPython firmware with network and sensor library support - I've used this UF2 - https://github.com/pimoroni/pimoroni-pico/releases

## How it Works

1. **Connect to WiFi**: The script connects to a specified WiFi network using the provided SSID and password.
2. **Read Sensor Data**: It reads temperature, humidity, and pressure data from the BME280 sensor connected to the Raspberry Pi Pico via I2C.
3. **Send Data to dweet.io**: The script constructs a JSON object containing WiFi status and sensor readings, then sends it to dweet.io for storage and retrieval.

## Usage

1. Replace the placeholder values in the script:
   - Replace `"Wifi_name"` and `"Password"` with your WiFi network SSID and password.
   - Replace `"your_thing_name"` with your dweet.io thing name.

2. Upload the script to your Raspberry Pi Pico running MicroPython.

3. Run the script, and it will continuously read sensor data and send it to dweet.io in a loop.

## Adjustments

- Modify the delay (default: 5 seconds) in the script (`sleep(5)`) to adjust the frequency of data transmission to dweet.io.

## Note

Ensure the Raspberry Pi Pico is connected to the BME280 sensor and has the correct MicroPython firmware installed before running the script.

Feel free to adapt and modify the code to suit your specific requirements.
