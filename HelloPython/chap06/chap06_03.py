# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

key_words = {}

key_words['list'] = 'A collection of items in a particular order.'
key_words['tuple'] = 'A collection which is ordered and unchangeable.'
key_words['dictionary'] = 'A collection of key-value pairs.'
key_words['key'] = 'The first item in a key-value pair in a dictionary.'
key_words['value'] = 'An item associated with a key in a dictionary.'
key_words['loop'] = 'Work through a collection of items, one at a time.'
key_words['string'] = 'A series of characters.'
key_words['comment'] = \
    'A note in a program that the Python interpreter ignores.'
key_words['sorted'] = \
    'A function that returns a sorted list of the specified iterable object.'
key_words['reverse'] = 'A method that reverses the order of a list.'
key_words['range'] = 'A function that returns a sequence of numbers.'
key_words['len'] = 'A function that returns the length of an object.'

for key, value in key_words.items():
    print(f'{key}: {value}\n')