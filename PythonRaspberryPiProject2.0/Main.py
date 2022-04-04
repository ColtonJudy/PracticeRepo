from tkinter.constants import BOTTOM, TOP
from Weather import Weather
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from Location import *

lat, lon = getLocation()

root = tk.Tk()
root.geometry('800x600')
root.title('Colton\'s Weather Program')

#TKinter labels
location_label = tk.Label(root)
location_label.pack(side=TOP)

lat_label = tk.Label(root)
lat_label.pack(side=TOP)

lon_label = tk.Label(root)
lon_label.pack(side=TOP)

weather_conditons_label = tk.Label(root)
weather_conditons_label.pack(side=TOP)

temp_label = tk.Label(root)
temp_label.pack(side=TOP)

feels_like_label = tk.Label(root)
feels_like_label.pack(side=TOP)

pressure_label = tk.Label(root)
pressure_label.pack(side=TOP)

humidity_label = tk.Label(root)
humidity_label.pack(side=TOP)

wind_speed_label = tk.Label(root)
wind_speed_label.pack(side=TOP)

hourly_rainfall_label = tk.Label(root)
hourly_rainfall_label.pack(side=TOP)

update_label = tk.Label(root)
update_label.pack(side=BOTTOM)

#method that loads the weather data to the labels
def loadWeatherData(lat, lon):
    #update weather variable
    weather = Weather(lat, lon)

    location_label['text'] = "Location: " + str(weather.info['location'])
    lat_label['text'] = "LAT: " + str(weather.settings['lat'])
    lon_label['text'] = "LON: " + str(weather.settings['lon'])
    temp_label['text'] = "Current Temperature: " + str(round(weather.current['temp'], 1)) + "°F"
    weather_conditons_label['text'] = "Current Weather: " + weather.current['weather_conditions']
    update_label['text'] = "Last updated: " + datetime.now().strftime("%H:%M")
    feels_like_label['text'] = "Feels like: " + str(round(weather.current['feels_like'], 1)) + "°F"
    pressure_label['text'] = "Barometric Pressure: " + str(weather.current['pressure'])
    humidity_label['text'] = "Humidity: " + str(weather.current['humidity']) + "%"
    wind_speed_label['text'] = "Wind speed: " + str(weather.current['wind_speed']) + " KPH"
    hourly_rainfall_label['text'] = "Hourly Rainfall: " + str(weather.current['hourly_rainfall']) + " MB"

loadWeatherData(lat, lon)

#Update Button
#TODO: API HAS A LIMITED NUMBER OF CALLS PER DAY, SO A LIMIT SHOULD BE ADDED OR THE PROGRAM SHOULD BE MADE TO ONLY AUTOMATICALLY UPDATE ~ EVERY MINUTE
update_button = tk.Button(root, text="Update",command=lambda: loadWeatherData(lat, lon))
update_button.pack(side=BOTTOM)

root.mainloop()