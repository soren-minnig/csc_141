# Took the poll
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

# Pending
pending_poll = ['erin', 'john', 'jen', 'phil', 'sam']

# Checking if names in pending_poll already took the poll
for name in pending_poll:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking our poll!")
    else:
        print(f"{name.title()}, please take our poll!")