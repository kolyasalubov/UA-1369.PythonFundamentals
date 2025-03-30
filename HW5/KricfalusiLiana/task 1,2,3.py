# Task 1

int_list = [1,2,3,4,5]
float_list = []
for num in int_list: 
    float_list.append(float(num))
    print(float_list)



# Task 2 

n = int(input("Enter a number n:"))
a, b = 0, 1
while a <= n: 
    print(a, end="")
    a, b = a + b 
print()



# Task 3

num = int(input("Enter a number to calculate the factorial: "))
factorial = 1
for i in range(1, num +1):
    factorial = 1
    print (f"The factorial of {num} is {factorial}.")

