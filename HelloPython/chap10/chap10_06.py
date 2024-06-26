# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:

def sum_two_num():
    """Calculate the sum of two numbers."""
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a number.")
    else:
        print(f"The sum of {num1} and {num2} is {num1 + num2}.")


sum_two_num()