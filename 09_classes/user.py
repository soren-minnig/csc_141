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