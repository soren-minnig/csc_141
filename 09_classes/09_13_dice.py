# Import function
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# 6-sided die
die1 = Die()

print("\nDice 1:")
for i in range(1, 11):
    die1.roll_die()

# 10-sided die
die2 = Die(10)

print("\nDice 2:")
for i in range(1, 11):
    die2.roll_die()

# 20-sided die
die3 = Die(20)

print("\nDice 3:")
for i in range(1, 11):
    die3.roll_die()