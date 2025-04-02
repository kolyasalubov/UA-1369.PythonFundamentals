num_1 = float(input("Enter first number -> \n"))
num_2 = float(input("Enter second number -> \n"))

def largest_number(num_1, num_2):
    """
    This function takes two numbers as input and returns the largest of the two.
    
    Parameters:
    num_1 (float): The first number to compare.
    num_2 (float): The second number to compare.
    
    Returns:
    float: The larger of the two input numbers. If both are equal, returns either of them.
    """
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2
    else:
        return num_1  

print("The largest number is:", largest_number(num_1, num_2))
