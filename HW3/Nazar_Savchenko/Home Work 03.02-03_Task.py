import math
'''num = (input("Write 4 digital natural number :" ))
digil = [int(sep_num) for sep_num in num]
prod = math.prod(digil)
print (prod)'''# знайшов простіший підхід бо можна змінювати цифри 

#Підхід з tuple. 
num = input("Write 4 digital natural number :" )
num_tuple = tuple(num)
digit = [int(d) for d in num_tuple]
prod = math.prod(digit)
print (prod)

#Reverse Number 
revers_num = (num[::-1])
print (revers_num)
#List sort Method
clean_tuple =''.join(num_tuple)
sort_tuple = sorted(clean_tuple)
clean_sort = ''.join(sort_tuple)
result = int(clean_sort)
print (result)

# interchange the values of two variables
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
print ("Original numbers","A =",num1, "B =",num2 )
num1,num2 = num2,num1
print ("After swap","A =",num1, "B =",num2 )