from service.load_model import temperature_model, windspeed_model, humidity_model, precipitation_model
# from model.schemas import TemperatureForecastInputModel

import numpy as np


async def forecast_temperature_service(year:int, month:int, day:int, hour:int, lat:float, long:float, windspeed:float, humidity:float, precipitation:float):
    print("kepanggil",year, month, day, hour, windspeed, humidity, precipitation,lat, long)
    input_data = np.array([[year, month, day, hour, windspeed, humidity, precipitation,lat, long]])
    # data_sample =  np.array([[2024, 10, 7, 13, 31.0 , 49.0, 0, -6.914744, 107.609810]]) # bandung
    forecasted_temperature = temperature_model.predict(input_data)
    return forecasted_temperature