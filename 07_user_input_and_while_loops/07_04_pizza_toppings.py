# Creating list of toppings
topping_list = []

while True:
    new_topping = input("\nWhat pizza topping would you like to add? \n"
                    "(Enter 'quit' to end the program.) ")
    
    # Ending the program
    if new_topping == 'quit':
        break

    # Appending a new topping to the list
    else:
        topping_list.append(new_topping)
        print("Okay, we'll add that topping to your pizza.\n"
              "So far, we have...\n")
        for topping in topping_list:
            print(topping)