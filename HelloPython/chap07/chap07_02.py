# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

people_num = input("How many people come to have lunch?\t")
people_num = int(people_num)
if people_num > 8:
    print("Sorry, there is no table available.")
else:
    print("There is a table available.")