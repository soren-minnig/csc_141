names = ['Yoshitaka Amano', 'Rokuro Saito', 'Shigenori Soejima']
removed_guest = names.pop(2)
names.append('Temmie Chang')

print(f"Hello {names[0]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[1]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"Hello {names[2]}! I'd like to invite you to dinner. Hope to see you there!")

print(f"\nUnfortunately, {removed_guest} could not make it.")