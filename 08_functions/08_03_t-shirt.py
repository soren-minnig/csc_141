# Defining the function
def make_shirt(size, text):
    print(f'We will make you a {size} t-shirt with "{text}" printed on it.')

# Positional argument
make_shirt("medium", "Albright College")

# Keyword argument
make_shirt(text="Albright College", size="medium")