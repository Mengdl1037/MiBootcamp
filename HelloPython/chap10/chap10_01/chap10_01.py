# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:

from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text(encoding='utf-8').rstrip()

# 直接显示内容
print(contents)
print()

# 逐行显示内容
for line in contents.splitlines():
    print(line)
print()


# 逐行替换单词并显示内容
for line in contents.splitlines():
    print(line.replace("Python", "C"))
print()
