# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def make_shirt(size='L', words='I love Python!'):
    message = "The size of the shirt is " + size
    message += ", and the words on the shirt are " + words + "."
    print(message)


make_shirt()
make_shirt('M')
make_shirt('S', 'Hello, Python!')