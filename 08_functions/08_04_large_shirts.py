# Defining the function
def make_shirt(size, text='I love Python'):
    print(f'We will make you a {size} t-shirt with "{text}" printed on it.')

# Using the default message
make_shirt('medium')
make_shirt('large')

# Using a different message
make_shirt('x-large', 'I love Rust')