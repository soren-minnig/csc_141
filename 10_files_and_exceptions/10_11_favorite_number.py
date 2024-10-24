from pathlib import Path
import json

# Creating a function to get a new number
def get_number(path):
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

# Creating a function to read an existing number
def read_number(path):
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None
    
# Creating a function to tie them together
def favorite_number():
    path = Path('10_files_and_exceptions/favorite_number.json')
    number = read_number(path)
    if number:
        print(f"I remember that your favorite number is {number}!")
    else:
        number = get_number(path)
        print(f"Okay...{number}. I'll remember that for next time!")

favorite_number()