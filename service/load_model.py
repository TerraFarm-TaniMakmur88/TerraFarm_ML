import xgboost as xgb
from keras.models import load_model
import pickle

# Temperature
temperature_model = xgb.XGBRegressor()
temperature_model.load_model("model/temperature_model.json")

# Load the scaler from the file
with open('model/temperature_scaler.pkl', 'rb') as f:
    temperature_scaler = pickle.load(f)

temperature_forecast_model = load_model('model/temperature_forecast_model.h5')

# Windspeed
windspeed_model = xgb.XGBRegressor()
windspeed_model.load_model("model/windspeed_model.json")
with open('model/windspeed_scaler.pkl', 'rb') as f:
    windspeed_scaler = pickle.load(f)
windspeed_forecast_model = load_model('model/windspeed_forecast_model.h5')

# Humidity
humidity_model = xgb.XGBRegressor()
humidity_model.load_model("model/humidity_model.json")
with open('model/humidity_scaler.pkl', 'rb') as f:
    humidity_scaler = pickle.load(f)
humidity_forecast_model = load_model('model/humidity_forecast_model.h5')

# Precipitation
precipitation_model = xgb.XGBRegressor()
precipitation_model.load_model("model/precipitation_model.json")
with open('model/precipitation_scaler.pkl', 'rb') as f:
    precipitation_scaler = pickle.load(f)
precipitation_forecast_model = load_model('model/precipitation_forecast_model.h5')