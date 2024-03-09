# from re import findall

class VinylMachine():
    
    def __init__(self):
        self.data_base = []
        self.filename = "vinyls.txt"
        self.load_db()
    
    def load_db(self):    
        file = open(self.filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                self.data_base.append(line)
        file.close()

    def sort_db(self):
        self.data_base.sort(key = str.casefold)

    def add_to_db(self, new_item):
        self.data_base.append(new_item)
    
    def delete_everything(self):
        self.data_base = []
        
    def write_to_file(self):
        self.sort_db()
    
        file = open(self.filename, "w")
        for line in self.data_base:
            line += "\n"
            file.write(line)
        file.close()