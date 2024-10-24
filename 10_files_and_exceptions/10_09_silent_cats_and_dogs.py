from pathlib import Path

# Creating a function to make it quicker
def find_names(filename):
    try:
        contents = Path('10_files_and_exceptions/' + filename)
        names = contents.read_text().splitlines()
    except FileNotFoundError:
        pass
    else:
        for name in names:
            print(name)

# Reading the files
find_names('cats.txt')
find_names('dogs.txt')

# If you change the directory, nothing is displayed, and it "silently" fails.