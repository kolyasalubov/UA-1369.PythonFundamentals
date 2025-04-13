from pyowm import OWM
import tkinter as tk
from tkinter import font


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()



def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        description = w.detailed_status
        temp = w.temperature('celsius')['temp']
        temp_min = w.temperature('celsius')['temp_min']
        temp_max = w.temperature('celsius')['temp_max']
        humidity = w.humidity
        wind = w.wind()['speed']
        clouds = w.clouds

        result = (
            f"Weather in {city}:\n"
            f"Status: {description}\n"
            f"Temperature: {temp}°C\n"
            f"Min: {temp_min}°C / Max: {temp_max}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s\n"
            f"Cloudiness: {clouds}%"
        )

    except Exception as e:
        result = f"Error: {str(e)}"

    label.config(text=result)



HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
