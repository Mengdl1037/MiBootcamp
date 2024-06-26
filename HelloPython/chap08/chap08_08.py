# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def make_album(single, album, number=None):
    album_info = {'single': single, 'album': album}
    if number:
        album_info['number'] = number
    return album_info


while True:
    print("\nPlease enter the information of the album:")
    print("(Enter 'q' at any time to quit.)")

    single = input("Single: ")
    if single == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    number = input("Number of songs: ")
    if number == 'q':
        break

    album_info = make_album(single, album, number)
    print(album_info)