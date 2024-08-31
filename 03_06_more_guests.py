# Original names
names = ['Yoshitaka Amano', 'Rokuro Saito', 'Shigenori Soejima']
removed_guest = names.pop(2)
names.append('Temmie Chang')

# New names
names.insert(0, 'Masayoshi Soken')
names.insert(2, 'Daisuke Ishiwatari')
names.append('Masahiro Sakurai')

# Original invitations
print(f"Hello {names[0]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[1]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[2]}! I'd like to invite you to dinner. Hope to see you there!")

# Additional invitations
print(f"Hello {names[3]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[4]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[5]}! I'd like to invite you to dinner. Hope to see you there!")

# Extra messages
print(f"\nUnfortunately, {removed_guest} could not make it.")

print(f"\n...But since we found a bigger table, {names[0]}, {names[2]}, and {names[-1]} could join us!")