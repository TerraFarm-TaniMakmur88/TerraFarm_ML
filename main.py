from fastapi import FastAPI, HTTPException
from service.forecast import forecast_temperature_service, forecast_windspeed_service, forecast_humidity_service, forecast_precipitation_service
from service.forecast import forecast_temperature_timeseries_service, forecast_windspeed_timeseries_service, forecast_humidity_timeseries_service, forecast_precipitation_timeseries_service

app = FastAPI()

@app.get("/")
async def index():
    return "Hello world"

@app.get("/forecast/temperature")
async def forecast_temperature(year:int, month:int, day:int, hour:int, lat:float, long:float, windspeed:float, humidity:float, precipitation:float):
    try:
        temperature_forecasted = await forecast_temperature_service(year, month, day, hour, lat, long, windspeed, humidity, precipitation)
        return {"status": "OK", "data": float(temperature_forecasted[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/temperature/timeseries")
async def forecast_temperature_timeseries(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float):
    try:
        temperature_forecasted = await forecast_temperature_timeseries_service(year, month, day, hour, lat, long, temperature)
        return {"status": "OK", "data": temperature_forecasted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/windspeed")
async def forecast_windspeed(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, humidity:float, precipitation:float):
    try:
        windspeed_forecasted = await forecast_windspeed_service(year, month, day, hour, lat, long, temperature, humidity, precipitation)
        return {"status": "OK", "data": float(windspeed_forecasted[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/windspeed/timeseries")
async def forecast_windspeed_timeseries(year:int, month:int, day:int, hour:int, lat:float, long:float, windspeed:float):
    try:
        windspeed_forecasted = await forecast_windspeed_timeseries_service(year, month, day, hour, lat, long, windspeed)
        return {"status": "OK", "data": windspeed_forecasted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/humidity")
async def forecast_humidity(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, windspeed:float, precipitation:float):
    try:
        humidity_forecasted = await forecast_humidity_service(year, month, day, hour, lat, long, temperature, windspeed, precipitation)
        return {"status": "OK", "data": float(humidity_forecasted[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/humidity/timeseries")
async def forecast_humidity_timeseries(year:int, month:int, day:int, hour:int, lat:float, long:float, humidity:float):
    try:
        humidity_forecasted = await forecast_humidity_timeseries_service(year, month, day, hour, lat, long, humidity)
        return {"status": "OK", "data": humidity_forecasted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/precipitation")
async def forecast_precipitation(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, windspeed:float, humidity:float):
    try:
        precipitation_forecasted = await forecast_precipitation_service(year, month, day, hour, lat, long, temperature, windspeed, humidity)
        return {"status": "OK", "data": float(precipitation_forecasted[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/forecast/precipitation/timeseries")
async def forecast_precipitation_timeseries(year:int, month:int, day:int, hour:int, lat:float, long:float, precipitation:float):
    try:
        precipitation_forecasted = await forecast_precipitation_timeseries_service(year, month, day, hour, lat, long, precipitation)
        return {"status": "OK", "data": precipitation_forecasted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))