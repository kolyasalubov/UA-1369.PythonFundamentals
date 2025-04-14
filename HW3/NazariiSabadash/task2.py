number = input('enter a number: ')

digits = [int(digit) for digit in number]

product = 1
for digit in digits:
    product *= digit

print(f'product -> {product}')
print(f'reversed -> {number[::-1]}')
print(f'ascending order -> {''.join(map(str, sorted(digits)))}')
