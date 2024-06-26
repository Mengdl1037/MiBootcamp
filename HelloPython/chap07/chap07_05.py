# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

active = True
while active:
    age = input("Please enter your age: ")
    if age == "exit":
        active = False
    else:
        if int(age) < 3:
            print("The ticket is free for you.")
        elif int(age) < 12:
            print("The ticket is $10 for you.")
        else:
            print("The ticket is $15 for you.")