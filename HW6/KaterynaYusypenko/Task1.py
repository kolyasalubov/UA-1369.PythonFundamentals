even_numbers = []
odd_numbers_divisible_by_3 = []
other_numbers = []

for item in range(1, 11):
    if item % 2 == 0:
        even_numbers.append(item)
    if item % 3 == 0:
        odd_numbers_divisible_by_3.append(item)
    if item % 2 != 0 and item % 3 != 0:
        other_numbers.append(item)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers divisible by 3: {odd_numbers_divisible_by_3}")
print(f"Other numbers: {other_numbers}")