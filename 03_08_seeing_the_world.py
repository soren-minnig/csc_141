locations = ['Germany', 'Switzerland', 'Japan', 'Spain', 'Egypt']

# Original order
print("Original:")
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)

# Reversed
print("\nReversed:")
locations.reverse()
print(locations)

# Back to original
print("\nOriginal:")
locations.reverse()
print(locations)

# Alphabetical
print("\nAlphabetical:")
locations.sort()
print(locations)

# Reverse alphabetical
print("\nReverse alphabetical:")
locations.sort(reverse=True)
print(locations)