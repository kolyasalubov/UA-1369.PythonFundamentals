import math

#1 You need to write Python's philosophy in the string format:
#find separately the number of occurences of the
#words "better", "never" and "is" in the given line

zen = """The Zen of Python, by Tim Peters
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!"""

print(zen)

print("\nAmount of 'better' appearance:",zen.lower().count("better"))
print("Amount of 'never' appearance:",zen.lower().count("never"))
print("Amount of 'is' appearance:", zen.lower().count("is"))

lines = zen.lower().strip().split("\n")
line = int(input("Choose line where to count amount of 'better' word:"))
print("better:",lines[line].count("better"))
line = int(input("Choose line where to count amount of 'never' word:"))
print("never:",lines[line].count("never"))
line = int(input("Choose line where to count amount of 'is' word:"))
print("is:",lines[line].count("is"))

#you need to display all text in uppercase (all letters in uppercase)
print("\nAll text upper:\n",zen.upper())

#replace all occurences of the symbol "i" with "&"
print("\nReplace 'i' with '&':\n", zen.replace("i","&"))

#2 A four-digit natural number is specified
#Find the product of the digits of this number
a = []
while len(a) != 4:
    a = list(map(int, input("Enter 4-digit number for var a: ")))

#using math library
print("\nProduct using math lib:", math.prod(a))

#using for loop
result = 1
for i in a:
    result *= i

print("Product using for loop:", result)

#write the number in reverse order
print("\nReverse order using ::-1 :", a[::-1])

#or using other method
a.reverse()
print("Reverse order using .reverse() :", a)

#in ascending order, you need to sort the numbers included in the given number
a.sort()
print("\nAscending order sort :", a)

#3. Interchange the values of two variables without using the third variable
a = input("\nEnter any number for var a: ")
b = input("Enter any number for var b: ")
a, b = b, a
print('"a" after change =', a)
print('"b" after change =', b)

