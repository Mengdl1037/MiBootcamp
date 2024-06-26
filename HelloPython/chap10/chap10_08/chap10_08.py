# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:
from pathlib import Path

def show_pets(path):
    """Print the content of the file."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("The file does not exist.")
    else:
        lines = contents.splitlines()
        for line in lines:
            print(line)

path = Path("cats.txt")
show_pets(path)
print()

path = Path("dogs.txt")
show_pets(path)