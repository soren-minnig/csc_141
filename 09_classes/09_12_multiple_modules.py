import user
import admin as ad

# Creating an instance
my_admin = ad.Admin('John', 'Doe', '25', '2014')

# Displaying privileges
my_admin.privileges.show_privileges()