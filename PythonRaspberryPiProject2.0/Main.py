from tkinter.constants import BOTTOM, TOP
from Weather import Weather
import tkinter as tk
import tkinter.ttk as ttk

lat = 35.155826
lon = -90.051063

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

temp_label = tk.Label(root)
temp_label.pack(side=TOP)

weather_conditons_label = tk.Label(root)
weather_conditons_label.pack(side=TOP)

#method that loads the weather data to the labels
def loadWeatherData(lat, lon):
    #update weather variable
    weather = Weather(lat, lon)

    location_label['text'] = "Location: " + str(weather.info['location'])
    lat_label['text'] = "LAT: " + str(weather.settings['lat'])
    lon_label['text'] = "LON: " + str(weather.settings['lon'])
    temp_label['text'] = "Current Temperature: " + str(round(weather.current['temp'], 2))
    weather_conditons_label['text'] = "Current Weather: " + weather.current['weather_conditions']

loadWeatherData(lat, lon)

#Update Button
#TODO: API HAS A LIMITED NUMBER OF CALLS PER DAY, SO A LIMIT SHOULD BE ADDED OR THE PROGRAM SHOULD BE MADE TO ONLY AUTOMATICALLY UPDATE ~ EVERY MINUTE
update_button = tk.Button(root, text="Update",command=lambda: loadWeatherData(lat, lon))
update_button.pack(side=BOTTOM)

root.mainloop()