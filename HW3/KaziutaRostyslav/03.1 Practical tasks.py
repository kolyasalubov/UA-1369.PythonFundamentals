#03.1.1 Practical tasks
# philosophy = """
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# """
# count_better = 0
# count_never = 0
# count_is = 0
#
# for line in philosophy.splitlines():
#     for word in line.split():
#         word = word.strip(".,*-")
#         if word == "better":
#             count_better += 1
#         elif word == "never":
#             count_never += 1
#         elif word == "one":
#             count_is += 1
#
# print(f"Amount of words better: {count_better}")
# print(f"Amount of words never: {count_never}")
# print(f"Amount of words is: {count_is}")
#
# print(philosophy.upper())
# print(philosophy.replace("i", "&"))


#03.1.2 Practical tasks
# num = input("Enter a number: ")
# print("Reversed:", num[::-1])
# print("Sorted:", " ".join(sorted(num)))
# print("Product:", sum(int(digits) for digits in num))

#03.1.3 Practical tasks
# num1 = 19
# num2 = 37
# num1, num2 = num2, num1
# print(num1, num2)

# a=10
# b=6
#
# print(not(a>b) or 0 or None or [])