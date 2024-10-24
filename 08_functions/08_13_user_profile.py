# Creating the function
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Calling the function to build a user profile
user_profile = build_profile('soren', 'minnig',
                             age='17',
                             state='PA',
                             major='computer science'
                             )

# Printing the user profile
print(user_profile)