from pyowm import OWM

def show_wether():
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
    try:
        observation = mgr.weather_at_place('London,GB')
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        result = (
            f"City: London,GB\n"
            f"Weather: {w.detailed_status}\n"
            f"Temperature: {temp} °C\n"
            f"Humidity: {w.humidity}%\n"
            f"Wind: {w.wind()['speed']} m/s\n"
            f"Clouds: {w.clouds}%\n"
            f"Rain: {w.rain}\n"
            f"Heat Index: {w.heat_index}"
        )
        return result
    except:
        return ("Can't get data for London weather")



