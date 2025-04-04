# Task №1
zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print("Better in zen - ", zen.find("better"))
print("Never in zen - ", zen.find("never"))
print("is in zen - ", zen.find("is"))
print("Zen in uppercase -", zen.upper())
print("Replace 'i' with '&' in zen - ", zen.replace("i", "&"))

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
