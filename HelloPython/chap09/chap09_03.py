# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:
import time

class User:
    
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            self.group = 'normal'
            self.last_login_time = '1970-01-01 00:00:00'
            self.__password = '123456'
            self.__login_attempt_times = 5

        def describe_user(self):
            print(f"First name: {self.first_name.title()}")
            print(f"Last name: {self.last_name.title()}")
            print(f"Group: {self.group}")
            print(f"Last login time: {self.last_login_time}")

        def greet_user(self):
            time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.last_login_time = time_now
            print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

        def login(self, password):
            if self.__password == password:
                self.greet_user()
            else:
                self.__login_attempt_times -= 1
                if self.__login_attempt_times == 0:
                    print("Login failed, please connect your administrator!")
                else:
                    print("Password Wrong, login failed!", end = ' ')
                    print(f"You can attempt {self.__login_attempt_times} times.")

        def set_password(self, password, new_password):
            if self.__password == password:
                self.__password = new_password
            else:
                print("Password Wrong, Change Password failed!")
        
        def set_group(self, group):
            self.group = group


# 设置并显示用户信息
user_1 = User("san", "zhang")
user_1.describe_user()

user_1.__password = '654321'
user_1.login('654321')

user_1._User__password = '654321'
user_1.login('123456')
user_1.login('654321')

print('\n')

user_1.set_password('123456', '654321')
user_1.set_group('admin')
user_1.login('123456')
user_1.describe_user()
print('\n')

user_2 = User("si", "li")
user_2.describe_user()
user_2.greet_user()
