# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

bicycles = ['trek', 'cannondale', 'specialized']

# Copy the list bicycles to friend_bicycles
friend_bicycles = bicycles[:]

bicycles.append('bianchi')
print("My favorite bicycles are:")
for value in bicycles:
    print(value.title(), end=' ')
print("\n")

friend_bicycles.append('giant')
print("My friend's favorite bicycles are:")
for value in friend_bicycles:
    print(value.title(), end=' ')
print("\n")