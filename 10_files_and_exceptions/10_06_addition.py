active = True

while active:
    print("\nEnter two numbers to add together.")
    print('(Enter "q" to quit.)\n')

    # Checking if the input is q
    number1 = input("First number: ")
    if number1 == 'q':
        quit()
    number2 = input("Second number: ")
    if number2 == 'q':
        quit()

    # Managing the ValueError exception
    try:
        value = int(number1) + int(number2)
    except ValueError:
        print("Could not compute: please enter a valid number.")
    else:
        print(value)