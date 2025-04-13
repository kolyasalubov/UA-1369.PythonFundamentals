#Переведення температури з вимірювання в Цельсіях в Фарангейти
temp_celsius = float(input("Enter the temperature in Celsius: "))
if temp_celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15 C)")
else:
    fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}C is equivalent to {fahrenheit}F")
