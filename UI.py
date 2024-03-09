from vinylMachine import VinylMachine

vm = VinylMachine()

print("Type 'X' to stop adding.")

new_input = input("Add your item: ")

while new_input != "X":
    
    if new_input == "sys del all":
        print("THIS WILL DELETE EVERYTHING. Do you want to continue [y]/[n]? ")
        confirmation_input = input("")
        if confirmation_input == "y" or confirmation_input == "Y":
            vm.delete_everything()
            break
            
    vm.add_to_db(new_input)
    new_input = input("Add another item: ")
    
vm.write_to_file()

print("That was fun! Your items are safe with me.")