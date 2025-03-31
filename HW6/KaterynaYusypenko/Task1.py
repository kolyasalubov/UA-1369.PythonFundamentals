even_numbers = []
odd_numbers_divisible_by_3 = []
other_numbers = []

for item in range(1, 11):
    if item % 2 == 0:
        even_numbers.append(item)
    elif item % 3 == 0:
        odd_numbers_divisible_by_3.append(item)
    else:
        other_numbers.append(item)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers divisible by 3: {odd_numbers_divisible_by_3}")
print(f"Other numbers (not divisible by 2 and 3): {other_numbers}")