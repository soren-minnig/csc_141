while True:
    # Prompting the user to enter their age
    age = int(input("\nWhat is your age? "))

    # Age conditionals
    if age < 3:
        print("Your movie ticket will be free.")
    elif age <= 12:
        print("Your movie ticket will be $10.")
    elif age > 12:
        print("Your movie ticket will be $15.")