# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:
from pathlib import Path
import json

def get_stored_num(path):
    if path.exists():
        content = path.read_text()
        return json.loads(content)
    else:
        return None

def store_num(path, num):
    content = json.dumps(num)
    path.write_text(content)

path = Path("favorite_number.json")
num = get_stored_num(path)
if num:
    print(f"I know your favorite number! It's {num}")
else:
    num = input("Please input your favorite number: ")
    store_num(path, int(num))


