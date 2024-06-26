# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

num = input("Please input a number, and I will tell you if it is a multiple of 10.\t")
num = int(num)
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")