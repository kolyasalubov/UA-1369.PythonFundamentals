#знайти кількість цифр в числі та порахувати їх добуток
number = 8214
digits = [int(a) for a in str(number)]

# Кількість цифр
count = len(digits)

# Добуток цифр
product = 1
for digit in digits:
    product *= digit

# Цифри написані у зворотному порядку
reversed_digits = digits[::-1]

# Відсортовані цифри по зростанню
sorted_digits = sorted(digits)

print("Кількість цифр:", count)
print("Добуток цифр:", product)
print("Цифри в зворотному порядку:", reversed_digits)
print("Цифри відсортовані по зростанню:", sorted_digits)
