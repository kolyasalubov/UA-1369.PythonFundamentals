#Write a script that will calculate the factorial of the entered
#number without using recursion.
#Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, 

n = int(input("Enter the number of circless: "))
factorial = 1 
while n > 1:
    factorial *=n
    n-=1
print (factorial)