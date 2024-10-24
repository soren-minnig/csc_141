from pathlib import Path

# Creating a function to make it quicker
def find_names(filename):
    try:
        contents = Path('10_files_and_exceptions/' + filename)
        names = contents.read_text().splitlines()
    except FileNotFoundError:
        print("The file could not be found.")
    else:
        for name in names:
            print(name)

# Reading the files
find_names('cats.txt')
print('\n')
find_names('dogs.txt')

# If you change the directory, the user-friendly error message is displayed.