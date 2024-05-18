#SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_tsl2591
from mysql.connector import connect, Error
from datetime import datetime


i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# Read the total lux, IR, and visible light levels and print it every second.
#while True:


try:
	connection=connect(host="localhost",user="schule", password="280188",database="tsl2591_data")

	if connection.is_connected():
		cursor=connection.cursor()
		sql_insert_query=	"""
					INSERT INTO sensor_readings (id, time, lux)
					VALUES(%s,%s,%s)
					ON DUPLICATE KEY UPDATE
						time=VALUES(time),
						lux=VALUES(lux);

					"""

		i=0
		while True:
			# Read and calculate the light level in lux.
			lux =round(sensor.lux,2)
			#print("Total light: {0}lux".format(lux))
			time.sleep(1.0)
			# Get current time
			current_time = datetime.now()
			f_time = current_time.strftime('%Y%m%d%H%M%S')

			# Create the data tuple with the formatted datetime
			data =(i, f_time, lux)
			cursor.execute(sql_insert_query,data)
			connection.commit()
			print(f"Successfully inserted {data}")
			i+=1

		'''# Get all Data from table
		sql_query="select * from sensor_readings"
		cursor.execute(sql_query)

		records=cursor.fetchall()
		for r in records:
			print(r)
		'''
except Error as e:
	print("Fehler:",e)

finally:
	if connection.is_connected():
		cursor.close()
		connection.close()
		print("MariaDB closed")

