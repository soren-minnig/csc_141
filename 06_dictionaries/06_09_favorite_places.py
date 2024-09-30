# Creating dictionaries
# "Green Dragon" is a bit of an inside joke, but it definitely is a place.
favorite_places = {
    'Haley' : 'Green Dragon',
    'Anthony' : 'the beach',
    'Luna' : 'the cinema'
    }

# Printing keys and values
for name, location in favorite_places.items():
    print(f"{name}'s favorite place to visit is {location}.")