temperature_celsius = float(input("Enter the temperature in Celsius -> \n"))

if temperature_celsius >= (-273.15):
    convert_in_fehrenheit = (temperature_celsius * 9/5) + 32
    print("{0} C is equivalent to {1}".format(temperature_celsius,convert_in_fehrenheit))
elif temperature_celsius < (-273.15):
    print("error: Temperature below absolute zero -273.15")
else :
    print("Invalid value")