number = input("Enter a four digit number = \n")
count_number = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print (f"Product of the digits of this number = \n{count_number}")


number_reverse = int(str(number)[::-1])
print(f"Number in reverse order \n{number_reverse}")


number_sort = "".join(sorted(number))
print(f"Number sorted in ascending order \n{number_sort}")