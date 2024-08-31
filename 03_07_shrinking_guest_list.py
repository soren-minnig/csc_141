# Original names
names = ['Yoshitaka Amano', 'Rokuro Saito', 'Shigenori Soejima']
removed_guest = names.pop(2)
names.append('Temmie Chang')

# New names
names.insert(0, 'Masayoshi Soken')
names.insert(2, 'Daisuke Ishiwatari')
names.append('Masahiro Sakurai')

# The popping
print("Since the table won't arrive on time, only two guests will be able to fit.\n")

uninvited = names.pop()
print(f"Sorry {uninvited}, but due to unforeseen circumstances, we won't have enough room for you.")

uninvited = names.pop()
print(f"Sorry {uninvited}, but due to unforeseen circumstances, we won't have enough room for you.")

uninvited = names.pop()
print(f"Sorry {uninvited}, but due to unforeseen circumstances, we won't have enough room for you.")

uninvited = names.pop()
print(f"Sorry {uninvited}, but due to unforeseen circumstances, we won't have enough room for you.\n")

# Remaining invites
print(f"Hello {names[0]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[1]}! I'd like to invite you to dinner. Hope to see you there!\n")

# Emptying list
del names[0]
del names[0]

# Final
print(names)
