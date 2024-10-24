# Importing classes
from admin import User, Privileges, Admin

# Creating an instance
my_admin = Admin('John', 'Doe', '25', '2014')

# Displaying privileges
my_admin.privileges.show_privileges()