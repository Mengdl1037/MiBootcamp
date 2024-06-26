# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

# user_names = ['admin', 'father', 'mother', 'son', 'daughter', 'grandpa', 'grandma']
user_names = []

if user_names:
    for user in user_names:
        if user.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')