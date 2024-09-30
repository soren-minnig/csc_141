active = True

# Creating the function
def make_album(artist_name, album_title):
    album = {'artist name': artist_name, 'album_title': album_title}
    print(album)

# Creating the loop
while active:
    artist_name = input("\nWhat is the artist's name? ")
    album_title = input("What is the album title? ")
    make_album(artist_name, album_title)