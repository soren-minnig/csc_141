# Importing function
from random import choice

# Creating lottery tuple and a specific ticket
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'A', 'B', 'C', 'D', 'E']
my_ticket = []

while len(my_ticket) < 4:
    ticket_element = choice(lottery)

    if ticket_element not in my_ticket:
        my_ticket.append(ticket_element)

# Printing random characters
ticket = []
attempts = 0
correct_elements = 0
won = False

while not won:
    attempts += 1
    while len(ticket) < 4:
        win_ticket_element = choice(lottery)

        if win_ticket_element not in ticket:
            ticket.append(win_ticket_element)

    for element in ticket:
        if element not in my_ticket:
            ticket = []
            correct_elements = 0
            continue

        elif element in my_ticket:
            correct_elements += 1
            
    if correct_elements == 4:
        print(f"It took {attempts} attempts to get a winning ticket.")
        won = True