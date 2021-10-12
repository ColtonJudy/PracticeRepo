from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 52.194504
my_lon = 0.134708

all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036

    for station in all_stations:
        print(station)

find_closest()