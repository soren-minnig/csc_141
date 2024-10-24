# From large_shirts:
def make_shirt(size, text='I love Python'):
    print(f'We will make you a {size} t-shirt with "{text}" printed on it.')

# From album:
def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album_title': album_title}

# From sandwiches:
def make_sandwich(*ingredients):
    print("\nWe'll make a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

# I would say that the programs above follow the styling guidelines.