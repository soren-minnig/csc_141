# Taking code from favorite_numbers.py and adding more values
# Creating dictionary of favorite numbers
favorite_numbers = {
    'soren': ['8', '13'], 
    'haley': ['4', '2'], 
    'anthony': ['1', '23'], 
    'cain': ['7', '15'], 
    'luna': ['5', '21']
    }

# Printing dictionary of favorite numbers
print("\nFavorite numbers:\n")

# I shortened the original code by using a loop.
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}: {numbers}")