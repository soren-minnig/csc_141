# One million
numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)

# I added an empty space between the list and and the print function. It's the
# same idea for the next two.

# Summing a million
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Odd numbers
numbers = []

for values in range(1, 21, 2):
    numbers.append(values)
    print(numbers[-1])