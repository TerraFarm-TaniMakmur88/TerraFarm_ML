import xgboost as xgb

# Temperature
temperature_model = xgb.XGBRegressor()
temperature_model.load_model("model/temperature_model.json")

# Windspeed
windspeed_model = xgb.XGBRegressor()
windspeed_model.load_model("model/windspeed_model.json")

# Humidity
humidity_model = xgb.XGBRegressor()
humidity_model.load_model("model/humidity_model.json")

# Precipitation
precipitation_model = xgb.XGBRegressor()
precipitation_model.load_model("model/precipitation_model.json")