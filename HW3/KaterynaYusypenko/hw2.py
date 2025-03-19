# Func input
num = int(input("Enter a four-digit number: "))

# Convert number to a list of digits
digits = [int(d) for d in str(num)]

# Product
product = digits[0] * digits[1] * digits[2] * digits[3]

#Reverse
reversed_num = int(str(num)[::-1])

#Sort in ascending order
sorted_digits = "".join(sorted(str(num)))

#Print results
print(f"Product: {product}")
print(f"Reverse: {reversed_num}")
print(f"Sort: {sorted_digits}")
