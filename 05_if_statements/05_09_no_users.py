# With users:
usernames = ['Oliver', 'John', 'Andrea', 'Catherine', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Greetings, {username}! Would you like to see a status"
                  "report?")
        else:
            print(f"Greetings, {username}! How are you today?")
else:
    print("We need to find some users!")

# No users:
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Greetings, {username}! Would you like to see a status"
                  "report?")
        else:
            print(f"Greetings, {username}! How are you today?")
else:
    print("We need to find some users!")