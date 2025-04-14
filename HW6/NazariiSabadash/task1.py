range10 = [i + 1 for i in range(10)]

even_nums = []
odd_nums = []
others = []

for i in range10:
    if i % 2 == 0:
        even_nums.append(i)
    elif i % 3 == 0:
        odd_nums.append(i)
    elif i % 3 != 0 and i % 2 != 0:
        others.append(i)

print(even_nums)    # [2, 4, 6, 8, 10]
print(odd_nums)     # [3, 9]
print(others)       # [1, 5, 7]
