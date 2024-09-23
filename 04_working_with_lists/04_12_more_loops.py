# Creating initial list and making them equal
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Appending different items
my_foods.append('cannoli')
friend_foods.append('ice cream')

# Proving the lists are different
print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())