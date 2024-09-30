# Creating lists
sandwich_orders = ['chicken', 'tuna', 'egg']
finished_sandwiches = []

# Using a while loop to pop sandwich_orders and append them into
# finished_sandwiches (until the initial list is empty)
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"We've made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Printing the sandwiches made
print("\n--- Sandwiches Made Today ---\n")
for sandwich in finished_sandwiches:
    print(sandwich)