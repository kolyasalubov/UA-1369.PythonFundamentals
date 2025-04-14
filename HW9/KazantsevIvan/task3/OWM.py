from pyowm import OWM
from key import *

API_KEY = weather_key
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details



# def get_weather(place):
#     observation = mgr.weather_at_place(place)
#     w = observation.weather
#     print(w.detailed_status)         # 'clouds'
#     print(w.wind())                  # {'speed': 4.6, 'deg': 330}
#     print(w.humidity)                # 87
#     print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#     print(w.rain)                    # {}
#     print(w.heat_index)              # None
#     print(w.clouds)                  # 75






def get_weather(place):
    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
        return (f"City: {place.title()}\n"
                f"Status: {w.detailed_status}\n"
                f"Wind speed: {w.wind()['speed']}\n"
                f"Humidity: {w.humidity}\n"
                f"Temp: {w.temperature('celsius')['temp']}\n"+
                (f"Rain: {w.rain}\n" if w.rain else "No rain\n")+
                (f"Heat index: {w.heat_index}\n" if w.heat_index else "No heat\n")+
                f"Clouds: {w.clouds}")
    except:
        return "Seems like place is spelled wrong..."
