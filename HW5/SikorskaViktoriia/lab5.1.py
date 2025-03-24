list_int = list((input("Enter integers number separated by spaces  -> ")))
clean_list_int = [item for item in list_int if item.strip()]

print(clean_list_int, type(clean_list_int))

for i in range(len(clean_list_int)):
    clean_list_int[i] = float(clean_list_int[i])
print(clean_list_int,type(clean_list_int))
   