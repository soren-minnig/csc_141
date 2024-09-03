# Using the previous program, and showing full list
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# First three
print("\nThe first three items in the list are:")
for cube in cubes[:3]:
    print(cube)

# Middle three
print("\nThe items from the middle of the list are:")
for cube in cubes[4:7]:
    print(cube)

# Last three
print("\nThe last three items in the list are:")
for cube in cubes[-3:]:
    print(cube)