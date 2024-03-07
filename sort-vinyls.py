# from re import findall

data_base = []
filename = "vinyls.txt"
new_input = ""

def load_db():    
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        if line != "":
            data_base.append(line)
    file.close()

def sort_db():
    data_base.sort()

def add_to_db(item):
    data_base.append(item)
    
def out_to_file():
    sort_db()
    
    file = open(filename, "w")
    for line in data_base:
        line += "\n"
        file.write(line)
    file.close()

load_db()
new_input = input("Type STOP to stop adding.\nWhat do you wanna add? ")
while new_input != "STOP":
    add_to_db(new_input)
    out_to_file()
    new_input = input("\nType STOP to stop adding.\nWhat do you wanna add? ")
print("That was fun! Your items are safe with me.")