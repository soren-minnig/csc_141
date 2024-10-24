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


# Creating multiple instances
restaurant1 = Restaurant('Han Dynasty', 'Chinese')
restaurant2 = Restaurant('Chipolte', 'Mexican')
restaurant3 = Restaurant('Popeyes', 'American')

# Calling a method for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()