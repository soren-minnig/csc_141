# Current and new users
current_users = ['Oliver', 'John', 'Andrea', 'Catherine', 'admin']
new_users = ['sren56', 'AnDrea', 'Cahri', 'wxl101', "JOHN"]

# Creating lowercase copy of existing users
current_users_lower = [x.lower() for x in current_users]

# Checking availability (case insensitive)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, but the username {new_user} is unavailable.")
    else:
        print(f"The username {new_user} is available.")