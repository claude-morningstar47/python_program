from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Weather App')
root.geometry('800x400+200+100')
root.resizable(False, False)


def getWeather():
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent="geoapiExerciss")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        # ADD API KEY WEATHER
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            city+"&appid=b22d3628518662b"
        json_data = requests.get(api).json()
        t.config(text=str(json_data['main']['temp']-273.15))
        c.config(text=json_data['weather'][0]['main'])
        w.config(text=json_data['wind']['speed'])
        h.config(text=json_data['main']['humidity'])
        d.config(text=json_data['weather'][0]['description'])
        p.config(text=json_data['main']['pressure'])

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")


image_search = PhotoImage(file="search_bar.png")
searchbar_image = Label(image=image_search)
searchbar_image.place(x=20, y=10)
text_field = tk.Entry(root, justify="center", width=17, font=(
    "poppins", 18, bold), bg="#147886", border=0, fg='white')
text_field.place(x=20, y=20)
text_field.focus()

image_search_icon = PhotoImage(file='search_icon.png')
search_icon = Button(image=image_search_icon, borderwidth=0,
                     cursor="hand2", bg="#147886", command=getWeather)
search_icon.place(x=250, y=18)


image_logo = PhotoImage(file="weather_logo.png")
weather_logo = Label(image=image_logo)
weather_logo.place(x=250, y=90)
