celsius = float(input("Enter the temperature in Celsius: "))
F = (celsius * 9 / 5) + 32
if celsius <= -273.15:
    print("Eror: Temperature below absolute zero (-273.15°C)")
elif celsius > -273.15:
    print(celsius, "°C is equivalent to", F, "°F")
else:
    print("Syntaxis eror, please enter temperature again")
