from tkinter.constants import TOP
from Weather import Weather
import tkinter as tk
import tkinter.ttk as ttk

weather = Weather(36.533221, -87.349698)

root = tk.Tk()
root.geometry('800x600')
root.title('Colton\'s Weather Program')

location_label = tk.Label(root, text = "Location: " + weather.info['location'])
location_label.pack(side=TOP)

lat_label = tk.Label(root, text = "LAT: " + str(weather.settings['lat']))
lat_label.pack(side=TOP)

long_label = tk.Label(root, text = "LON: " + str(weather.settings['lon']))
long_label.pack(side=TOP)

temp_label = tk.Label(root, text = "Current Temperature: " + str(round(weather.current['temp'], 2)))
temp_label.pack(side=TOP)

my_button = tk.Button(root, text="Update",command=weather.displayCurrent)
my_button.pack(side=TOP)

root.mainloop()