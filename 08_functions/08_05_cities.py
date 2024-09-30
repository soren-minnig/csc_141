# Defining the function
def describe_city(city, country='Spain'):
    print(f"The city of {city} is in {country}.")

# Using the default country
describe_city('Madrid')
describe_city('Bilbao')

# Using a different country
describe_city('Puebla', 'Mexico')