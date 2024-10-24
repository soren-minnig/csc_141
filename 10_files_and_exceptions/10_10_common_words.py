from pathlib import Path

def find_the(filename):
    book = Path('10_files_and_exceptions/' + filename)
    book_lines = book.read_text(encoding='utf-8').splitlines()

    total_count = 0

    try:
        for line in book_lines:
            count = int(line.lower().count('the '))
            total_count += count
    except FileNotFoundError:
        print(f"{filename} could not be found.")
    else:
        print(f'{filename} contains the word "the" {total_count} times.')

find_the('alice.txt')
find_the('jekyll.txt')
find_the('sawyer.txt')