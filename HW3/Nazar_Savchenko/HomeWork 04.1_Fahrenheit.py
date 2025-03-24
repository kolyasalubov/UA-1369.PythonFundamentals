absolute_zero = float(-273.15)
temp = float(input("Enter the temperature in Celsius: "))

if temp <= absolute_zero:
    print ("Error: Temperature below absolute zero (-273.15°C)")
else:
    fah = temp*9/5+32
    print (f"{temp}\u00B0C is equivalnet to {fah}\u00B0F")

print ("Thanks for trying, see you later!")