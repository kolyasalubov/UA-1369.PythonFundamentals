temperature = float(input("Enter a temperature in Celsius: "))
if temperature > -273.15:
    fahrenheit = (temperature * 9/5) + 32
    print (f"The temperature in Fahrenheit is {fahrenheit}°F")
else:
    print("Temperature below absolute zero (-273.15°C)")