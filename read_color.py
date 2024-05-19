# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_tsl2591
from mysql.connector import connect, Error
from datetime import datetime

# Initialize I2C and the sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_tsl2591.TSL2591(i2c)

try:
    connection = connect(
        host="localhost",
        user="schule",
        password="280188",
        database="tsl2591_data"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Ensure there is one row in the table
        cursor.execute("""
            INSERT INTO sensor_readings (id, time, lux)
            VALUES (1, NOW(), 0)
            ON DUPLICATE KEY UPDATE time=VALUES(time), lux=VALUES(lux);
        """)
        connection.commit()

        sql_update_query = """
            UPDATE sensor_readings
            SET time = %s, lux = %s
            WHERE id = 1
        """
        
        while True:
            # Read and calculate the light level in lux
            lux = round(sensor.lux, 2)
            time.sleep(1.0)
            
            # Get current time
            current_time = datetime.now()
            f_time = current_time.strftime('%Y%m%d%H%M%S')
            
            # Create the data tuple with the formatted datetime
            data = (f_time, lux)
            cursor.execute(sql_update_query, data)
            connection.commit()
            print(f"Successfully updated {data}")
            
            # Get all data from table
            sql_query = "SELECT * FROM sensor_readings"
            cursor.execute(sql_query)
            records = cursor.fetchall()
            for r in records:
                print(r)

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MariaDB connection closed")
