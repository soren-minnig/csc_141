# Importing function
from random import choice

# Creating lottery tuple
lottery = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'A', 'B', 'C', 'D', 'E')

# Printing random characters
print("\nAny ticket matching these four letters/numbers wins a prize:")
for i in range(1, 5):
    value = choice(lottery)
    print(value)