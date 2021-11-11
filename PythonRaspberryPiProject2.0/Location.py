from geopy.geocoders import Nominatim

#Find the nearest city to the given coordinates using Nominatim API
def find_nearest_city(lat, lon):
    geolocator = Nominatim(user_agent="Colton's Weather Raspberry Pi Project")

    coords = (lat, lon)
    location = geolocator.reverse(coords)

    return location

#TODO implement receiving GPS data via PI dongle
def getLocation():
    return 'null'