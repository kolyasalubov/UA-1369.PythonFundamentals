# Create a list that contains elements of integer type, then use
#the loop to change the type of these elements to a floating type.
#(Hint: use the built-in float () function).
num = [4, 4, 5, 4, 6, 98]

for int_number in num:
   float_number = float(int_number)
   print (float_number)
print (type(float_number))