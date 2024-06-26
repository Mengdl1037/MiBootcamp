# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:
from user import User
from privileges import Privileges

"""A class that can be used to represent an administrator."""
class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()