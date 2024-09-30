# User input
people = int(input("How many people are in your dinner group? "))

# Checking input
if people > 8:
    print("\nSorry, you'll have to wait for a table.")
else:
    print("\nWe have a table available for you!")