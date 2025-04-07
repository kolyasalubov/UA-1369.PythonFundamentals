def find_largest (num1, num2):
    """
    Finding the larger of two numbers:

    1. Initialize num1 and num2
    2. Compare num1 and num2.
    3. If num1 = num2, print the message: 
    The largest number is not found because these numbers are the same. 
    4. If num1 is greater, return num1.
    5. Otherwise, return num2.
    """
    if num1 == num2:
        print(f"The largest number is not found because these numbers are the same: {num1} = {num2}")
    elif num1 > num2:
        print(f"The largest number is: {num1}")
    else:
        print(f"The largest number is: {num2}")
find_largest (18, 25)