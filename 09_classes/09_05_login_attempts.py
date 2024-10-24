# Creating the class
class User:

    def __init__(self, first_name, last_name, age, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_joined = date_joined
        self.login_attempts = 0

    # Describes the user
    def describe_user(self):
        print("\n--- User Info ---\n")
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Date joined: {self.date_joined}")

    # Greets the user
    def greet_user(self):
        print(f"\nHi, {self.first_name}! How are you today?")

    # Increments the amount of login attempts
    def increment_login_attempts(self):
        self.login_attempts += 1

    # Resets the amount of login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0


# Creating user
user1 = User('John', 'Doe', '25', '2014')

# Incrementing amount of login attempts several times
for i in range(3):
    user1.increment_login_attempts()
    print(f"Current amount of login attempts: {user1.login_attempts}")

# Resetting the amount of login attempts
user1.reset_login_attempts()
print(f"Current amount of login attempts: {user1.login_attempts}")