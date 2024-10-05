from fastapi import FastAPI, HTTPException
from service.forecast import forecast_temperature_service, forecast_windspeed_service
# from model.schemas import TemperatureForecastInputModel

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
    
@app.get("/forecast/windspeed")
async def forecast_windspeed(year:int, month:int, day:int, hour:int, lat:float, long:float, temperature:float, humidity:float, precipitation:float):
    try:
        windspeed_forecasted = await forecast_windspeed_service(year, month, day, hour, lat, long, temperature, humidity, precipitation)
        return {"status": "OK", "data": float(windspeed_forecasted[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))