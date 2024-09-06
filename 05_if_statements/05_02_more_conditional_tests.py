# Testing for equality and inequality
number_1 = 5
print("Is the number I'm thinking of less than or equal to 3?")
print(number_1 <= 3)

print("\nIs the number I'm thinking of greater than or equal to 5?")
print(number_1 <= 5)

# Using "and" and "or"
number_2 = 10
print("\nIs number_1 >= 7 and number_2 <=12?")
print(number_1 >= 7 and number_2 <= 12)

print("\nIs number_1 >= 7 or number_2 <=12?")
print(number_1 >= 7 or number_2 <= 12)

# Test using lower()
name = 'John'
print("\nDoes the name == john?")
print(name.lower() == 'john')

# List testing
animals = ['cat', 'dog', 'fish']
print("\nIs there a cat in the list of animals?")
print('cat' in animals)

print("\nIs there a turtle in the list of animals?")
if 'turtle' not in animals:
    print("No, there is not a turtle in the list.")