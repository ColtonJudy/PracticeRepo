from requests import get
import json
from pprint import pprint
from haversine import *

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()['items']

#pprint(stations)
print(haversine(74.0059, 40.7128, 0.1278, 51.5074))