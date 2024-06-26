# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

bicycle = 'Giant'
print('Is bicycle == "Giant"? I predict True.')
print('Giant' == bicycle.title())

print('\nIs bicycle == "Merida"? I predict False.')
print('Merida' == bicycle.title())

bicycles = ('trek', 'cannondale', 'specialized', 'bianchi', 'merida')
print('\nIs bicycle in bicycles? I predict False.')
print(bicycle.lower() in bicycles)

print('\nIs bicycle not in bicycles? I predict True.')
print(bicycle not in bicycles)

friend_bicycle = 'Merida'
print('\nIs bicycle == friend_bicycle? I predict False.')
print(friend_bicycle.lower() == bicycle.lower())

print('\nIs bicycle != friend_bicycle? I predict True.')
print(bicycle.lower() == friend_bicycle.lower())

print('\nAre bicycle and friend_bicycle both in the bicycles? I predict False.')
print(bicycle.lower() in bicycles and friend_bicycle.lower() in bicycles)

print('\nAre bicycle or friend_bicycle in the bicycles? I predict True.')
print(bicycle.lower() in bicycles or friend_bicycle.lower() in bicycles)

height = 180
print('\nIs height >= 170? I predict True.')
print(height >= 170)

print('\nIs height <= 170? I predict False.')
print(height <= 170)

print('\nIs height == 180? I predict True.')
print(height == 180)

print('\nIs height != 180? I predict False.')
print(height != 180)

