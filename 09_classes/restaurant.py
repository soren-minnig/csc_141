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