# Creating the class
class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers = 0

    # Describe the restaurant
    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    # Opens the restaurant
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    # Sets the number of customers served
    def set_number_served(self, served):
        self.customers = served

    # Increments the number of customers served
    def increment_number_served(self, new_served):
        self.customers += new_served


# Creating an instance
restaurant = Restaurant('Han Dynasty', 'Chinese')

# Printing the initial amount of served customers
print(f"Customers served so far: {restaurant.customers}")

# Changing the amount of served customers
restaurant.set_number_served(13)
print(f"Customers served so far: {restaurant.customers}")

# Incrementing the amount of served customers
restaurant.increment_number_served(22)
print(f"Customers served so far: {restaurant.customers}")