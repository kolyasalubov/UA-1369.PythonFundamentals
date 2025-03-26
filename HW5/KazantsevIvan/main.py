# TASK1
# Create a list that contains elements of integer type, then use the loop
# to change the type of these elements to a floating type


#int_num = list(map(int, input("TASK 1\nEnter integers separated by spaces:").split()))

int_num = [int(num) for num in input("TASK 1\nEnter integers separated by spaces:").split()]

print(int_num)

#using map func
float_num1 = list(map(float, int_num))
print("Map func: float_num1 = ",float_num1)

# using list comprehension
float_num2 = [float(item) for item in int_num]
print("List comprehension: float_num2 = ", float_num2)

# using for loop
float_num3 = []
for i in int_num:
    float_num3.append(float(i))

print("For loop: float_num3 = ", float_num3)

# TASK 2
# Print Fibonacci numbers up to the entered number n, using cycles

print("\nTASK 2")
fibonacci = 0
fibonacci_next = 1
n = 0
while n < 1:
    n = int(input("Please enter the number >=1:"))

#using for loop
print("For loop:")

for i in range(n):
    print(fibonacci, end=" ")
    fibonacci,fibonacci_next = fibonacci_next,fibonacci+fibonacci_next

# using while

print("\nWhile loop:")
fibonacci, c = 0, 0
fibonacci_next = 1
while c < n:
    print(fibonacci, end=" ")
    fibonacci,fibonacci_next = fibonacci_next,fibonacci+fibonacci_next
    c += 1

# TASK 3
# Write a script that will calculate the factorial of the entered number
# without using recursion

print("\nTASK 3\n")
num = -1
while num<0:
    num = int(input("Please enter the number >= 0:"))

factorial = 1
for i in range(1, num+1):
    factorial *= i

print("For loop\nfactorial =", factorial)

# using while loop
factorial = num
while num>1:
    num -= 1
    factorial *= num

if factorial == 0:
    factorial = 1

print("While loop\nfactorial =", factorial)
