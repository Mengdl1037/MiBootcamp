# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

# The list comprehension is used to generate a list of odd numbers from 1 to 20.
odd_num_list = [value for value in range(1, 21, 2)]

print("The list of odd numbers from 1 to 20 is:")
print(odd_num_list)

print("The first three numbers in the list are:")
print(odd_num_list[:3])

print("Three numbers from the middle of the list are:")
length = len(odd_num_list)
print(odd_num_list[(length >> 1):(length >> 1) + 3])

print("The last three numbers in the list are:")
print(odd_num_list[-3:])
