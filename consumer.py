from kafka import KafkaConsumer
import json
import requests
 
# Kafka consumer
def kafka_consumer():
    consumer = KafkaConsumer('streaming', bootstrap_servers=['broker:9092'], 
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        # Process incoming messages, e.g., perform real-time analysis
        data = message.value
        date = data['Date']
        hour = data['Hour']
        temperature = data['Temperature']
        humidity = data['Humidity']
        wind_speed = data['Windspeed']
        visibility = data['Visibility']
        dew_point_temp = data['Dew_point_temperature']
        solar_radiation = data['Solar_radiation']
        rainfall = data['Rainfall']
        snowfall = data['Snowfall']
        url = f'http://127.0.0.1:5000/predict?hour={hour}&temperature={temperature}&humidity={humidity}&wind_speed={wind_speed}&visibility={visibility}&dew_point_temp={dew_point_temp}&solar_radiation={solar_radiation}&rainfall={rainfall}&snowfall={snowfall}'

        response = requests.get(url)
        prediction = response.content
        prediction = prediction.decode('utf-8')
        response_data = json.loads(prediction)
        print("Predicted Rented Bike Count:" + str(response_data))

        
if __name__ == "__main__":
    kafka_consumer()

