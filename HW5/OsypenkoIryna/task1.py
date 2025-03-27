numbers = [3, 7, 'hhbbg', 15, 19.3, 27, 30.78, 135]
list_num = [num for num in numbers if isinstance(num, int)]
for i in range(len(list_num)):
    list_num[i] = float(list_num[i])
print(list_num)