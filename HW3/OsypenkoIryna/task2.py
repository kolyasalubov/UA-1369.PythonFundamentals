number = 4967
print ("the number: ", number)

l = str(number)

#the number in reverse order
print ("the number in reverse order: ", int(l[::-1]))

#the product of the digits
product = eval ("*".join(l))
print ("the product of the digits: ", product)

#in ascending order
sorted_num = int("".join(sorted(l)))
print ("numbers in ascending order: ", sorted_num)