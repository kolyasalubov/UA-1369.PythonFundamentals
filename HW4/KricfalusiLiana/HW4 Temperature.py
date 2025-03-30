def celsius_to_fahrenheit(celsius):
    """Counverts temperature from Celsius to Fahrenheit."""
    return (celsius*9/5)+32
celsius = float(input("Enter temperature in Celsius: ")) 
if celsius < -237.15:
        print ("Error: Temperature below absolute zero (-237.15°C).")
else:
    fahrenheit = celsius_to_fahrenheit(celsius)
    print (f"{celsius}°C is equal to {fahrenheit} °F.")
    
