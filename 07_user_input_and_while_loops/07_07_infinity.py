# Creating an infinite loop
count = 0

# There is a conditional statement, but we forgot to add "count += 1" to
# actually change the count.
# Thus, it will run forever.
while count <= 5:
    print(f"Your count is currently {count}.")
else:
    quit()