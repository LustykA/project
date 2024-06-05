import json
import random
import sys
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer


if __name__ == "__main__":
    SERVER = "broker:9092"

    producer = KafkaProducer(
        bootstrap_servers=[SERVER],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        api_version=(3, 7, 0),
    )
    
    try:
        while True:
            
            conn = sqlite3.connect("data.db")
            result = pd.read_sql("SELECT * FROM data", conn)
            data = result.sample()

            message = {
                "Date" : data['Date'].iloc[0],
                "Rented_bike_count" : data['Rented Bike Count'].iloc[0], 
                "Hour" : data['Hour'].iloc[0],
                "Temperature" : data["Temperature"].iloc[0],
                "Humidity" : data["Humidity"].iloc[0],
                "Windspeed" : data["Wind speed"].iloc[0],
                "Visibility" : data["Visibility"].iloc[0],
                "Dew_point_temperature" : data["Dew point temperature"].iloc[0],
                "Solar_radiation" : data["Solar Radiation"].iloc[0],
                "Rainfall" : data["Rainfall"].iloc[0],
                "Snowfall" : data["Snowfall"].iloc[0],
                "Seasons" : data["Seasons"].iloc[0],
                "Holiday" : data["Holiday"].iloc[0],
                "Functional_day" : data["Functioning Day"].iloc[0]
            }
            producer.send("streaming", value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()