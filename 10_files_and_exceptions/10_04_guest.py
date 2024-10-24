from pathlib import Path

# Prompting user for their name
contents = input("What is your name? ")

# Adding their name to a file
path = Path('10_files_and_exceptions/guest.txt')
path.write_text(contents)