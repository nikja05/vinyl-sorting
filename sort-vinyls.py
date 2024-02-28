from re import findall
import string

alphabet = string.ascii_uppercase
# regex pattern
pattern = ",(\s[A-Za-z0-9]+\s?)?\s([A-Za-z0-9]+)"

def create_lists():
    
def add_album(vinyl):
    
    # loop through list
    book = open("vinyls.txt", "r")
    for item in book:
        
        if item == vinyl:
            print("You have already added this album.")
            
        else:
            # findall returns two dimensional list (theoretically tuple inside of list)
            # [0][1] finds second item (first might be empty or not)
            name = findall(pattern, item)[0][1]
        
            # look at last names, alphabetically, loop through first letters (get index from alphabet)
            
            # insert into list

print("Hi. Please type in the required names. Make sure to write the artist's name as [first_name last_name].")
# get input from user (ask for album title, artist/band name)
# vinyl = input("[album name], [artist/band name]: ")
album_and_artist = "coco, channel"
find_album(album_and_artist)