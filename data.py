import pandas as pd

DATA_PATH = "https://archive.ics.uci.edu/static/public/560/data.csv?fbclid=IwZXh0bgNhZW0CMTAAAR0scsOgt76uOIPlmHzq9a48WuZDyXqb73qvv1TB-Qufz3iW9izUZXvEDRw_aem_AY0r2RUpXkodcuCuJHlVWMBFk27iGkPchxVLviucBm_z2rwjHa6MBvX3EOTFQdFJcaQ4z_vkp8ST9Jz_Kx1YXgSf"
col_names = ["Date", "Rented Bike Count", "Hour", "Temperature", "Humidity", "Wind speed", "Visibility", "Dew point temperature", "Solar Radiation", "Rainfall", "Snowfall", "Seasons", "Holiday", "Functioning Day"]
df = pd.read_csv(DATA_PATH, names=col_names)

# save to sqlite
import sqlite3
# generate database
conn = sqlite3.connect("data.db")
# pandas to_sql

try:
    df.to_sql("data", conn, index=False)
except:
    print("tabela już istnieje")

