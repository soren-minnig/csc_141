from pathlib import Path

# Replacing "Python" with "C"
path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text().rstrip()
contents = contents.replace('Python', 'C')

# Reading and printing the entire file
print(contents + '\n')