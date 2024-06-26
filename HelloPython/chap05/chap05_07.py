# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

bicycles = ['trek', 'cannondale', 'specialized', 'pinarello', 'giant', 'merida']
my_favorite_bicycles = ['giant', 'merida', 'bianchi', 'canyon', 'cannondale']

for bicycle in bicycles:
    if bicycle in my_favorite_bicycles:
        print(f'{bicycle.title()} is my favorite bicycle!')
    else:
        print(f'{bicycle.title()} is not my favorite bicycle.')