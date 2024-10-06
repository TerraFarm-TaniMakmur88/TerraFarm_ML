from service.load_model import temperature_model, windspeed_model, humidity_model, precipitation_model
from service.load_model import temperature_forecast_model, windspeed_forecast_model, humidity_forecast_model, precipitation_forecast_model
from service.load_model import temperature_scaler,windspeed_scaler, humidity_scaler, precipitation_scaler
# from model.schemas import TemperatureForecastInputModel

import numpy as np


async def forecast_temperature_service(year:int, month:int, day:int, hour:int, lat:float, long:float, windspeed:float, humidity:float, precipitation:float):
    input_data = np.array([[year, month, day, hour, windspeed, humidity, precipitation,lat, long]])
    forecasted_temperature = temperature_model.predict(input_data)
    return forecasted_temperature

async def forecast_temperature_timeseries_service(year:int, month:int, day:int, hour:int,lat:float, long:float, temperature:float):
    input_data = np.array([temperature_scaler.transform(np.array([[temperature, lat, long]]))])
    prediction = temperature_forecast_model.predict(input_data) 
    forecasted_temperature = temperature_scaler.inverse_transform(np.array([[prediction[0,0], None, None]]))[0][0]
    return forecasted_temperature  

async def forecast_windspeed_service(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, humidity:float, precipitation:float):
    input_data = np.array([[year, month, day, hour, temperature, humidity, precipitation,lat, long]])
    forecasted_windspeed = windspeed_model.predict(input_data)
    return forecasted_windspeed

async def forecast_windspeed_timeseries_service(year:int, month:int, day:int, hour:int,lat:float, long:float, windspeed:float):
    input_data = np.array([windspeed_scaler.transform(np.array([[windspeed, lat, long]]))])
    prediction = windspeed_forecast_model.predict(input_data) 
    forecasted_windspeed = windspeed_scaler.inverse_transform(np.array([[prediction[0,0], None, None]]))[0][0]
    return forecasted_windspeed  

async def forecast_humidity_service(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, windspeed:float, precipitation:float):
    input_data = np.array([[year, month, day, hour, temperature, windspeed, precipitation,lat, long]])
    forecasted_humidity = humidity_model.predict(input_data)
    return forecasted_humidity

async def forecast_humidity_timeseries_service(year:int, month:int, day:int, hour:int,lat:float, long:float, humidity:float):
    input_data = np.array([humidity_scaler.transform(np.array([[humidity, lat, long]]))])
    prediction = humidity_forecast_model.predict(input_data) 
    forecasted_humidity = humidity_scaler.inverse_transform(np.array([[prediction[0,0], None, None]]))[0][0]
    return forecasted_humidity  

async def forecast_precipitation_service(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, windspeed:float, humidity:float):
    input_data = np.array([[year, month, day, hour, temperature, windspeed, humidity,lat, long]])
    forecasted_precipitation = precipitation_model.predict(input_data)
    return forecasted_precipitation

async def forecast_precipitation_timeseries_service(year:int, month:int, day:int, hour:int,lat:float, long:float, precipitation:float):
    input_data = np.array([precipitation_scaler.transform(np.array([[precipitation, lat, long]]))])
    prediction = precipitation_forecast_model.predict(input_data) 
    forecasted_precipitation = precipitation_scaler.inverse_transform(np.array([[prediction[0,0], None, None]]))[0][0]
    return forecasted_precipitation  