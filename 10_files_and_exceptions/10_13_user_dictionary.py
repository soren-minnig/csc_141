from pathlib import Path
import json

# Creating a function to get user info
def get_info(path):
    # Initial dictionary
    user_info = {}

    user_info['name'] = input("What is your name? ")
    user_info['age'] = input("How old are you? ")
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"Goodbye, {user_info['name']}! We hope to see you again soon.")
    return user_info

# Creating a function to read existing info
def read_info(path):
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
# Creating a function to tie them together
def user_info():
    path = Path('10_files_and_exceptions/user_dictionary.json')
    user_info = read_info(path)
    if user_info:
        print(f"Name: {user_info['name']}")
        print(f"Age: {user_info['age']}")
    else:
        user_info = get_info(path)

user_info()