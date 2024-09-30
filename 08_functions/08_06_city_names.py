# Defining the function
def city_country(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()

# Calling the function
print(city_country('nuuk', 'greenland'))
print(city_country('akureyri', 'iceland'))
print(city_country('oslo', 'norway'))