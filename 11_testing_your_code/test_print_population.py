from print_city import print_population

# Testing function
def test_print_population():
    printed_population = print_population('santiago', 'chile')
    assert printed_population == 'Santiago, Chile'

def test_city_country_population():
    printed_population = print_population('santiago', 'chile',
                                          population='5000000')
    assert printed_population == 'Santiago, Chile - Population 5000000'