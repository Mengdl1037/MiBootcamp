# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

bicycles = ('trek', 'cannondale', 'specialized', 'bianchi', 'pinarello')
for value in bicycles:
    print(value.title(), end=' ')
print('\n')

# You can't change the elements in a tuple, but you can assign a new value to a variable that represents a tuple.
# bicycles[0] = 'Giant'

bicycles = ('giant', 'cannondale', 'specialized', 'bianchi', 'merida')
for value in bicycles:
    print(value.title(), end=' ')
print('\n')