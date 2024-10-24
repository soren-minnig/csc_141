# Creating the function
def make_sandwich(*ingredients):
    print("\nWe'll make a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

# Calling the function with a different number of arguments each time
make_sandwich('ham',)
make_sandwich('chicken', 'lettuce',)
make_sandwich('turkey', 'tomatoes', 'pickles',)