# Creating lists
messages = ['hello', 'how are you today?', 'goodbye']
sent_messages = []

# Creating the function
def show_messages():
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

# Calling the function
show_messages()