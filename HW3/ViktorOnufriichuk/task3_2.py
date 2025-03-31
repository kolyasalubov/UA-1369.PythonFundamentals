# Задано чотиризначне число:
# - знайти добуток цифр цього числа
# - запишіть число у зворотному порядку
# - у порядку зростання потрібно відсортувати числа, що входять до заданого числа

a = input("enter a four-digit number:")
# a = int(input("enter a four-digit number:"))
# a = str(a)
# a = str(1234)

# n1 = int(a[0])
# n2 = int(a[1])
# n3 = int(a[2])
# n4 = int(a[3])
# print('Multiplication:', n1 * n2 * n3 * 4)
# print('reverse =', a[::-1])
# print(sorted(a))
# print('Multiplication:', n1 * n2 * n3 * n4, '\nreverse:', a[::-1], '\nsorted:', sorted(a))

print('Multiplication:', int(a[0]) * int(a[1]) * int(a[2]) * int(a[3]), '\nreverse:', a[::-1], '\nsorted:', sorted(a))