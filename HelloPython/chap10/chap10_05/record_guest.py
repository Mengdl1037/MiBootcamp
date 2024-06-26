# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:

from pathlib import Path

path = Path("guest_book.txt")

guest = ""
while True:
    guest += input("Please enter your name: ")
    guest += "\n"
    if input("Would you like to continue? (yes/no) ") == "no":
        break

path.write_text(guest)
print("Your name has been recorded.")