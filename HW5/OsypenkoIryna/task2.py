n = int(input("Enter number = "))

fibonacci_num = [0, 1]

for i in range(2,n):
    fibonacci_num.append(fibonacci_num[i-1]+fibonacci_num[i-2])
print(fibonacci_num)