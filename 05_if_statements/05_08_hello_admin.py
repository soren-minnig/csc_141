usernames = ['Oliver', 'John', 'Andrea', 'Catherine', 'admin']

# Checking if user is an admin
for username in usernames:
    if username == 'admin':
        print(f"Greetings, {username}! Would you like to see a status report?")
    else:
        print(f"Greetings, {username}! How are you today?")