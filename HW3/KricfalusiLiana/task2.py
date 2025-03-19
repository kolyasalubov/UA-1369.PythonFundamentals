number = 9753  
digits = [int(d) for d in str(number)] 
product = 1  # Initialize the product
for d in digits:
    product *= d # multiply each digit to get the product
reversed_number = int(str(number)[::-1]) # Reverse a number by converting it to a string and using slices

sorted_digits = sorted(digits) # sort the numbers in ascending order

#Display of results
print(f"The product of numbers: {product}") # digitization
print(f"Reverse number: {reversed_number}") # print the reversed number
print(f"Numbers in ascending order: {sorted_digits}")  # Output the sorted digits