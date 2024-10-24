# Creating the class
class User:

    def __init__(self, first_name, last_name, age, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_joined = date_joined

    # Describes the user
    def describe_user(self):
        print("\n--- User Info ---\n")
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Date joined: {self.date_joined}")

    # Greets the user
    def greet_user(self):
        print(f"\nHi, {self.first_name}! How are you today?")


# Creating users
user1 = User('John', 'Doe', '25', '2014')
user2 = User('Navn', 'Navnesen', '32', '2019')
user3 = User('Max', 'Mustermann', '29', '2020')

users = [user1, user2, user3]

# Calling both methods for each instance
for user in users:
    user.describe_user()
    user.greet_user()