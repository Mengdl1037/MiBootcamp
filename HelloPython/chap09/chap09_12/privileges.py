"""A class that can be used to represent the privileges of an administrator."""
class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)