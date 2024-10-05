from service.load_model import temperature_model, windspeed_model, humidity_model, precipitation_model
# from model.schemas import TemperatureForecastInputModel

import numpy as np


async def forecast_temperature_service(year:int, month:int, day:int, hour:int, lat:float, long:float, windspeed:float, humidity:float, precipitation:float):
    print("kepanggil",year, month, day, hour, windspeed, humidity, precipitation,lat, long)
    input_data = np.array([[year, month, day, hour, windspeed, humidity, precipitation,lat, long]])
    forecasted_temperature = temperature_model.predict(input_data)
    return forecasted_temperature

async def forecast_windspeed_service(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, humidity:float, precipitation:float):
    print("kepanggil",year, month, day, hour, temperature, humidity, precipitation,lat, long)
    input_data = np.array([[year, month, day, hour, temperature, humidity, precipitation,lat, long]])
    forecasted_windspeed = windspeed_model.predict(input_data)
    return forecasted_windspeed