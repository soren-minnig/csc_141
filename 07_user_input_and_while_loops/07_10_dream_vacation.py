# Creating initial dictionary
dream_locations = {}
active = True

while active:
    # Prompting the user for a response
    name = input("\nWhat is your name? ")
    response = input("If you could go anywhere in the world, where would you "
                     "go? ")  
    
    # Storing response in the dictionary
    dream_locations[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active = False

# Printing poll results
print("\n--- Poll Results ---\n")
for name, response in dream_locations.items():
    print(f"{name} would like to go to {response} someday.")