n = int(input("Enter a number: "))

def factorial(n):
    result = 1  
    for i in range(1, n + 1):  
        result *= i 
    return result
print(f"Factorial of {n} is {factorial(n)}")