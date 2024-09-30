# I've been going back through the exercises again to improve the code
# formatting.

# This mostly consisted of fixing indentation within dictionaries.
# For instance, from favorite_numbers.py:
favorite_numbers = {
    'soren': '8', 
    'haley': '4', 
    'anthony': '1', 
    'cain': '7', 
    'luna': '5'
    }

# This is after I changed it, but previously, it looked something like this:
favorite_numbers = {
                'soren': str(8), 
                'haley': str(4), 
                'anthony': str(1), 
                'cain': str(7), 
                'luna': str(5)
}

# I don't know why I felt obligated to use str(), but I realized my mistake
# later. Then, I got rid of some of the indentations and changed the location of
# the end bracket. It makes the code easier to read.