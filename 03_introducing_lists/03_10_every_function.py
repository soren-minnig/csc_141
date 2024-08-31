# Creating list
cities = ['Beijing', 'Shanghai', 'Chengdu', 'Guangzhou']
print("The original list:")
print(cities)

# Temporary alphabetical order(+ reverse alphabetical order), and proving the list hasn't changed
print("\nUsing sorted() function:")
print(sorted(cities))
print(cities)
print(sorted(cities, reverse=True))
print(cities)

# Permanent reverse, and proving the list has changed
print("\nUsing reverse() function:")
cities.reverse()
print(cities)

# Permanent alphabetical order, and proving the list has changed
print("\nUsing sort():")
cities.sort()
print(cities)

# Del
del cities[-1]

# Pop
tooFar = cities.pop(-1)
print(f"\nSince we don't want to travel too far, we eliminated {tooFar} from the list...\n")

# Append
cities.append('Chongqing')
print(cities)
print(f"\n...and added Chongqing instead.\n")

# Len
amount = len(cities)
print (f"Now, there are {amount} cities in the list.")

# Remove
print("\nLet's narrow it down.\n")
cities.remove('Chongqing')
cities.remove('Beijing')

# End list
print(cities)

# Modifying a value and using insert
cities[0] = 'Chengdu, China'
cities.insert(0, 'Meishan')
print(f"\nI've always wanted to go to {cities[-1]}. Since {cities[0]} is nearby, we might as well stop there, too.")