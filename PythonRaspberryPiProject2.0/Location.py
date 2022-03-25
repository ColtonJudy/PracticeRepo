from geopy.geocoders import Nominatim
import gpsd
from time import sleep
import os

#Find the nearest city to the given coordinates using Nominatim API
def find_nearest_city(lat, lon):
    geolocator = Nominatim(user_agent="Colton's Weather Raspberry Pi Project")

    coords = (lat, lon)
    location = geolocator.reverse(coords)

    return location

#TODO implement receiving GPS data via PI dongle
def getLocation():

    #LAUNCH GPSD
    os.system("gpsd -D 5 -N -n /dev/cu.usbmodem1101")

    gpsd.connect()

    while True:
        packet = gpsd.get_current()
        try:
            print(packet.position())
            return packet.position()
        except:
            print("Position could not be determined")
        sleep(5)