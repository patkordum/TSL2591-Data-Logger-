#SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_tsl2591
from mysql.connector import connect, Error

try:
	connection=connect(host="localhost",user="schule", password="280188",database="tsl2591_data")

	if connection.is_connected():
		cursor=connection.cursor()
		sql_query="select * from sensor_readings"
		cursor.execute(sql_query)

		records=cursor.fetchall()
		for r in records:
			print(r)

except Error as e:
	print("Fehler:",e)

finally:
	if connection.is_connected():
		cursor.close()
		connection.close()
		print("MariaDB closed")
'''

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# Read the total lux, IR, and visible light levels and print it every second.
while True:
    # Read and calculate the light level in lux.
    lux = sensor.lux
    print("Total light: {0}lux".format(lux))
    # Infrared levels range from 0-65535 (16-bit)
    infrared = sensor.infrared
    print("Infrared light: {0}".format(infrared))
    # Visible-only levels range from 0-2147483647 (32-bit)
    visible = sensor.visible
    print("Visible light: {0}".format(visible))
    # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
    full_spectrum = sensor.full_spectrum
    print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
    time.sleep(1.0)
'''
