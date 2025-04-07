from OWM import *
import tkinter as tk
from tkinter import font

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather():
    city = entry_field.get()
    if not city:
        label.config(text="Enter a city name", font=('Courier', 12), justify="center")
        return

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        wind = w.wind()
        temperature = w.temperature('celsius')

        weather_info = (
            f"Weather: {w.detailed_status}\n"
            f"Wind: {wind.get('speed', 0)} m/s\n"
            f"Humidity: {w.humidity}%\n"
            f"Temperature: {temperature['temp']}°C\n"
            f"Min: {temperature['temp_min']}°C, Max: {temperature['temp_max']}°C\n"
            f"Clouds: {w.clouds}%\n"
            f"Rain: {w.rain if w.rain else 'No rain'}"
        )

        label.config(text=weather_info, font=('Courier', 12), justify="left", anchor="w")
    except Exception as e:
        label.config(text=f"Error: {e}", font=('Courier', 12), justify="center")


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)





lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

