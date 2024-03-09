from machine import Machine

machine = Machine()

print("Type 'X' -> stop adding.")

new_input = input("What do you wanna add? ")

while new_input != "X":
    machine.add_to_db(new_input)
    new_input = input("What else you wanna add? ")
    
machine.write_to_file()

print("That was fun! Your items are safe with me.")