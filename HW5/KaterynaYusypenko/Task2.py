n = int(input("Enter the value of n "))
fib_list = [0, 1]
while fib_list[-1] +fib_list[-2] <= n:
    fib_list.append(fib_list[-1]+ fib_list[-2])
print("Fibonacci up to", n, fib_list)
