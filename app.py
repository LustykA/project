from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

def predict_bike_rentals(hour, temperature, humidity, wind_speed, visibility, dew_point_temp, solar_radiation, rainfall, snowfall, model_path='random_forest_model.pkl'):
    
    features = pd.DataFrame({
            'Hour': [hour],
            'Temperature(°C)': [temperature],
            'Humidity(%)': [humidity],
            'Wind speed (m/s)': [wind_speed],
            'Visibility (10m)': [visibility],
            'Dew point temperature(°C)': [dew_point_temp],
            'Solar Radiation (MJ/m2)': [solar_radiation],
            'Rainfall(mm)': [rainfall],
            'Snowfall (cm)': [snowfall]
        })

    with open('model1.pkl', 'rb') as file:
        model1 = joblib.load(file)

    
        prediction = model1.predict(features)
    
    return round(prediction[0])

@app.route('/predict', methods=['GET'])
def predict_page():
    hourP = request.args.get("hour", 0, type=int)
    temperatureP = request.args.get("temperature", 0, type=float)
    humidityP = request.args.get("humidity", 0, type=float)
    wind_speedP = request.args.get("humidity", 0, type=float)
    visibilityP = request.args.get("humidity", 0, type=float)
    dew_point_tempP = request.args.get("humidity", 0, type=float)
    solar_radiationP = request.args.get("humidity", 0, type=float)
    rainfallP = request.args.get("humidity", 0, type=float)
    snowfallP= request.args.get("humidity", 0, type=float)    

    predicted_rentals = predict_bike_rentals(
    hour=hourP,
    temperature=temperatureP,
    humidity=humidityP,
    wind_speed=wind_speedP,
    visibility=visibilityP,
    dew_point_temp=dew_point_tempP,
    solar_radiation=solar_radiationP,
    rainfall=rainfallP,
    snowfall=snowfallP
    )
    
    return jsonify(predicted_rentals)

if __name__ == '__main__':
    app.run(debug=True)