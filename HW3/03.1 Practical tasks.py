#03.1.2 Practical tasks
num = input("Enter a number: ")
print("Reversed:", num[::-1])
print("Sorted:", " ".join(sorted(num)))
print("Product:", sum(int(digits) for digits in num))

#03.1.3 Practical tasks
num1 = 19
num2 = 37
num1, num2 = num2, num1
print(num1, num2)



