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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = list(flavors)

    # Displays flavors
    def display_flavors(self):
        print(f"Here are the flavors available:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


# Creating an instance
ice_stand = IceCreamStand("Rita's", 'ice cream',
                          'cherry', 'lemon', 'blue raspberry')

# Displaying flavors
ice_stand.display_flavors()