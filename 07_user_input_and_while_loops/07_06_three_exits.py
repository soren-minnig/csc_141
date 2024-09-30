# From pizza_toppings:
# Creating list of toppings and setting count to 0
topping_list = []
active = True

# Using active variable
while active:
    new_topping = input("\nWhat pizza topping would you like to add? \n"
                    "(Enter 'quit' to end the program.) ")
    
    # Ending the program
    if new_topping == 'quit':
        break

    # Using conditional
    elif len(topping_list) >= 4:
        topping_list.append(new_topping)
        print("\nOkay, we'll add that topping to your pizza.\n"
              "That's the maximum amount of toppings you can order.\n"
              "Here's your final list:\n")
        for topping in topping_list:
            print(topping)

        active = False

    # Appending a new topping to the list
    else:
        topping_list.append(new_topping)
        print("\nOkay, we'll add that topping to your pizza.\n"
            "So far, we have...\n")
        for topping in topping_list:
            print(topping)