# From 3-6:

# Original names

names = ['Yoshitaka Amano', 'Rokuro Saito', 'Shigenori Soejima']
removed_guest = names.pop(2)
names.append('Temmie Chang')

# New names

names.insert(0, 'Masayoshi Soken')
names.insert(2, 'Daisuke Ishiwatari')
names.append('Masahiro Sakurai')

print("Number of guests:")
print(len(names))