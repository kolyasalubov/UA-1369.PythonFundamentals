even_number = [ ]
odd_number = [ ]
not_divisible = [ ]

for i in range (1,11):
    if i % 2 == 0: 
        even_number.append(i)
    elif i % 3 == 0 and i % 2 !=0: 
        odd_number.append(i)
    else:
        not_divisible.append(i)
print("Even number:" ,even_number)
print("Odd number:" ,odd_number)
print("Else number:" ,not_divisible)