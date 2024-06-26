# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

num_list = list(range(1, 10))

for num in num_list:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')