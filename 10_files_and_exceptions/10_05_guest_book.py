from pathlib import Path

# Defining path, a list to store names and a string to put them in the file
path = Path('10_files_and_exceptions/guest_book.txt')
contents = []
string = ""

while True:
    print("\nPlease check-in to our guestbook.")
    print('(Enter "q" to quit.)\n')

    # Prompting user(s) for their name(s)
    content = input('Enter your name: ')
    if content == 'q':
        break
    contents.append(content)

# Putting each name on a new line
for name in contents:
    string += f"{name}\n"

# Publishing to guest_book.txt
path.write_text(string)