from print_city import print_city

# Testing function
def test_print_city():
    printed_city = print_city('santiago', 'chile')
    assert printed_city == 'Santiago, Chile'