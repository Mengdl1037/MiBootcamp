# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

favorite_num = {}
favorite_num['zhang'] = [66, 99]
favorite_num['li'] = [99, 88]
favorite_num['wang'] = [88, 77]
favorite_num['zhao'] = [77, 88, 42]
favorite_num['luo'] = [42, 6, 8]

for name, nums in favorite_num.items():
    print(f'{name.title()}\'s favorite numbers are: ')
    for num in nums:
        print(f'\t{num}', end='')
    print('\n')
