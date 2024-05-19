# TSL2591 Lux Sensor Data Logger

This project enables logging of ambient light intensity (lux) readings from a TSL2591 sensor to a MySQL database using a Raspberry Pi. It also provides a simple web interface to view the latest sensor readings.

## Usage

1. **Hardware Setup:**
   - Connect the TSL2591 sensor to your Raspberry Pi via I2C.
   - Ensure that your Raspberry Pi is connected to the internet and has access to a MySQL database.

2. **Software Installation:**
   - Clone this repository to your Raspberry Pi.
   - Install the required Python libraries using pip: `pip install adafruit-circuitpython-tsl2591 mysql-connector-python`.

3. **Database Setup:**
   - Create a MySQL database with the name `tsl2591_data`.
   - Update the database connection details (`host`, `user`, `password`, `database`) in both the Python and PHP scripts.

4. **Run the Python Script:**
   - Execute the Python script `lux_sensor_logger.py` to start logging sensor data to the database.

5. **View Sensor Readings:**
   - Access the web interface hosted on your Raspberry Pi to view the latest sensor readings.
   - Open a web browser and navigate to `http://<your_pi_ip_address>/sensor_readings.php`.
   - The web page will automatically refresh every 5 seconds to display updated sensor readings.

## Directory Structure
lux_sensor_logger/
├── lux_sensor_logger.py # Python script for logging sensor data
├── sensor_readings.php # PHP script to display sensor readings
└── README.md # Project documentation


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
