rivers = {'amazon' : 'brazil', 'nile' : 'egypt', 'yangtze' : 'china'}

# Print sentence
for river, location in rivers.items():
    print(f"The {river.title()} River runs through {location.title()}.")

# Rivers
print("\n")
for river in rivers:
    print(river.title())

# Locations
print("\n")
for location in rivers.values():
    print(location.title())