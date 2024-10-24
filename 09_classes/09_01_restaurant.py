# Creating the class
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Describes the restaurant
    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    # Opens the restaurant
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")


# Creating an instance
restaurant = Restaurant('Han Dynasty', 'Chinese')

# Printing the attributes individually and calling both methods
print(f"There is a local restaurant called {restaurant.restaurant_name}.")
print(f"It serves {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()