from pathlib import Path
import json

# From remember_me.py:
def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
    return username

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    path = Path('10_files_and_exceptions/username.json')
    username = get_stored_username(path)
    if username:
        # Verifying the user
        print(f"You're currently logged in as {username}.")
        verify = input("Is this correct? (Yes/No) ")
        if verify.lower() == 'no':
            get_new_username(path)
        else:
            print(f"Welcome back, {username}!")
    else:
        get_new_username(path)
        
greet_user()