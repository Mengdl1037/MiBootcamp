# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:

from pathlib import Path

path = Path("guest.txt")
guest = input("Please enter your name: ")
path.write_text(guest)
print("Your name has been recorded.")