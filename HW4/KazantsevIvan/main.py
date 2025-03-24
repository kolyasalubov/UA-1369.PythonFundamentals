#Temperature Converter

celsiusTemp = float(input("Enter the temperature in Celsius: "))

if celsiusTemp <-273.15:
    print("Error: The temperature is below absolute zero (-273.15°C)")
else:
    fahrenheitTemp = celsiusTemp * 1.8 + 32
    print(f"{celsiusTemp:.2f}°C is equivalent to {fahrenheitTemp:.2f}°F")

