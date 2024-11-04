# For first exercise
def print_city(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()

# For second exercise
def print_population(city, country, population=''):
    if population:
        formatted = f"{city}, {country} - population {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()