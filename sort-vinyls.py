from re import findall
import string

original_list = []
last_name_list = []
alphabet = string.ascii_uppercase
# regex pattern
pattern = ",(\s[A-Za-z0-9]+\s?)?\s([A-Za-z0-9]+)"


def create_arrays():
    # loop through vinyls.txt
    book = open("vinyls.txt", "r")
    for item in book:
         
        # findall returns two dimensional list (theoretically tuple inside of list)
        # [0][1] finds second item (first might be empty or not)
        # (the CROOKS, michael JACKSON, QUEEN)
        last_name = findall(pattern, item)[0][1]
        
        original_list.append(item)
        last_name_list.append(last_name)
        
def search_index(new_last_name):

    for i in range(len(last_names_list)):
        
        if alphabet.index(new_last_name[0].capitalize()) == alphabet.index(last_names_list[i][0].capitalize()):
            search_index(new_last_name[1:0])
            
        else if alphabet.index(new_last_name[0].capitalize()) < alphabet.index(last_names_list[i][0].capitalize()):
            continue
        
        else if alphabet.index(new_last_name[0].capitalize()) > alphabet.index(last_names_list[i][0].capitalize()):
            # insert method

print("Hi. Please type in the required names. Make sure to write the artist's name as [first_name last_name].")
# get input from user (ask for album title, artist/band name)
# vinyl = input("[album name], [artist/band name]: ")
album_and_artist = "coco, channel"
new_last_name = findall(pattern, album_and_artist)
search_index(new_last_name)
create_arrays()