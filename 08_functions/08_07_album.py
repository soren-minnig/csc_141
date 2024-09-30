# Creating the function
def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album_title': album_title}

    # Creating an optional value
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    print(album)

# Calling the function
make_album('Red Vox', 'Another Light')
make_album('Red Vox', 'Another Light', '14')