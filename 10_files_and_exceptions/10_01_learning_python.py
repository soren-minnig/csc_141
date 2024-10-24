from pathlib import Path

# I had to specify the file for some reason; it wouldn't run otherwise
path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text().rstrip()

# Reading and printing the entire file
print(contents + '\n')

# Printing the lines individually
lines = contents.splitlines()
for line in lines:
    print(line)