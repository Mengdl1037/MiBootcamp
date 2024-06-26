# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:
from pathlib import Path
import json

num = input("Please input your favorite number: ")
content = json.dumps(int(num))
path = Path("favorite_number.json")
path.write_text(content)

content = path.read_text()
print(f"I know your favorite number! It's {json.loads(content)}")