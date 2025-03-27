# Check if the list contains odd number.
# (Hint: use the break statement)


list_numbers = [2, 48, 191, 200, 303]

def get_first_odd(numbers):
    for num in list_numbers:
        if num % 2 == 1:
            print("First odd number found:", num)
            break
get_first_odd(list_numbers)