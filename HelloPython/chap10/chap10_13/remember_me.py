# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-22
# Function:
from pathlib import Path
import json

def get_stored_user_info(path):
    """如果存储了⽤户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def get_new_user_info(path):
    """提⽰⽤户输⼊⽤户名"""
    username = input("What is your name? ")
    age = input("How old are you? ")
    job = input("What is your job? ")
    user_info = {'username': username, 'age': age, 'job': job}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """问候⽤户，并指出其名字"""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info:
        for key, value in user_info.items():
            print(f"{key}: {value}")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember your informations when you come back, {user_info['username']}!")

greet_user()