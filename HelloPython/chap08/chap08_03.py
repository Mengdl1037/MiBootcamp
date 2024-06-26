# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def make_shirt(size, words):
    message = "The size of the shirt is " + size
    message += ", and the words on the shirt are " + words + "."
    print(message)


make_shirt('M', 'Long May the Sun Shine!')
make_shirt(words='Long May the Sun Shine!', size='L')