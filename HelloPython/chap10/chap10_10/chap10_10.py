# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:
from pathlib import Path

path = Path("RomeoAndJuliet.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    num_of_the = 0
    for line in contents.splitlines():
        num_of_the += line.lower().count('the ')
    print(f"The word 'the ' appears {num_of_the} times in the file.")