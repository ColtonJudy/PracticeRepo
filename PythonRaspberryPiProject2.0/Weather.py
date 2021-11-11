import requests
import json
from pprint import pprint

class Weather:
    settings = {
        'api_key' : '040e13ce7de9dadb243f29cde3be44f1',
        'temp_unit' : 'imperial',
        'lat' : 0,
        'long' : 0,
        'url' : 'NULL'
    }

    info = {
        'location' : 'NULL'
    }

    current = {
        'temp' : 0,
        'feels_like' : 0
    }

    #TODO: Implement overrided constructor taking zipcode as a parameter and finding location based on that
    def __init__(self, lat, lon):
        self.settings['lat'] = lat
        self.settings['lon'] = lon

        self.settings['url'] = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=%s" % (self.settings['lat'], self.settings['lon'], self.settings['api_key'], self.settings['temp_unit'])

        response = requests.get(self.settings['url'])
        data = json.loads(response.text)
        print(self.settings['url'])

        self.current['temp'] = data["current"]["temp"]
        self.current['feels_like'] = data["current"]["feels_like"]

    def displayCurrent(self):
        for entry in self.current.items():
            print(entry)
