# temperature converter

temp = int(input('enter temperature in Celsius: '))
if temp < -273.15:
    print('error message. could not be so low')
else:
    fahrenheit = (temp * 9/5) + 32
    print(f'{temp} Celsius = {fahrenheit} Fahrenheit')
