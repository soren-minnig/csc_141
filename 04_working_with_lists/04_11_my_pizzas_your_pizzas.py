pizzas = ['cheese', 'pepperoni', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())