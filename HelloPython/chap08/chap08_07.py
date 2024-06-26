# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def make_album(single, album, number=None):
    album_info = {'single': single, 'album': album}
    if number:
        album_info['number'] = number
    return album_info


album1 = make_album('San Zhang', 'The First Album')
album2 = make_album('Si Li', 'The Second Album')
album3 = make_album('Wu Wang', 'The Third Album', 10)

print(album1)
print(album2)
print(album3)