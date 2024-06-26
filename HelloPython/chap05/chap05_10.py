# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

current_users = ['admin', 'father', 'mother', 'son', 'daughter', 'grandpa', 'grandma']
new_users = ['uncle', 'aunt', 'cousin', 'father', 'mother']

current_users_lower = [user.lower() for user in current_users]

if new_users:
    for user in new_users:
        if user.lower() in current_users_lower:
            print(f'Hello {user.title()}, please enter a new username.')
        else:
            print(f'Hello {user.title()}, your username is available.')