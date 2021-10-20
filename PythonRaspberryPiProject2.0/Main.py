import time
import requests
from pprint import pprint
from Location import getLocation

settings = {
    'api_key' : '${{secret.OpenWeather_API_KEY}}',
    'zip_code' : getLocation(),
    'country_code' : 'us',
    'temp_unit' : 'imperial'
}

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

while True:
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    pprint(weather_data)
    time.sleep(20) #get new data every 20 seconds
