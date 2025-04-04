#Print Fibonacci numbers up to the entered number n, using cycles.
#(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Enter the number of circless: "))
a ,b = 0, 1

print (a, b , end= " ")
while n > 2:
    a , b = b , a + b 
    print (b, end= " ")
    n -=1
