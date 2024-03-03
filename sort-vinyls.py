from re import findall

class SortVinyls():
    
    def __init__(self, filename):
        self.filename = filename
        self.data_base = []
        self.load_data_base()
    
    def load_data_base(self):
        file = open(self.filename, "r")
        for line in file:
            file.strip()
            self.data_base.append(line)
        file.close()
        self.data_base.sort()
    
    def add_vinyl(self, new_vinyl, old_vinyl):
        
        for i in range(len(self.original_list)):
            if new_vinyl[0] == original_list
    
class Vinyl():
    
    def __init__(self, vinyl):
        self.vinyl = vinyl.upper()
    
    def __eq__(self, other):
        return self.vinyl == other.vinyl
    
    def __str__(self):
        return self.vinyl
    
    def compare(self, other):
        len_vinyl = len(self.vinyl)
        
        for i, name in enumerate(len_vinyl):
            if self.vinyl[i] == other.vinyl[i]:
                
        
v = SortVinyls()
print(v.original_list)
# take name of album from list
# if the first letter of old album is smaller in ascii
    # insert before
# elif the first letter of old album is bigger
    # go to next album
# else (the letters are equal)
    # go back to step two, take away the first letters