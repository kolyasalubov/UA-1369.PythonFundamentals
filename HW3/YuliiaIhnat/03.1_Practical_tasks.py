# Task №1


# Task №2
a = 2850
print("Number: ", a)
b = str(a)
c = list(b)
print("Separate numbers: ", c)
d = int(c[0]) * int(c[1]) * int(c[2]) * int(c[3])
print("The product of the digits:", d)
c.reverse()
print("Reverse numbers: ", c)
c.sort()
print("Sort number: ", c)

# Task №3
a = 8
b = 15
print("a = ", a, "b = ", b)
a, b = b, a
print("Value of a:", a)
print("Value of b:", b)
