'''
Contains Unique Elements
O(1) for insert, remove and contains
Assumption: We add Strings
'''

class HashSet:
    def __init__(self, size = 20):
        self.size = size
        self.set = [[] for i in range(self.size)] # List of Lists to handle collisions
    
    def add(self, value):
        index = self.get_index(value)
        list = self.set[index]
        if value in list:
            print(" Cannot have duplicates ")
            return
        self.set[index].append(value)
        return
    
    def remove(self, value):
        index = self.get_index(value)
        list = self.set[index]
        list.remove(value)

    def contains(self, value):
        index = self.get_index(value)
        list = self.set[index]
        if value in list:
            print(value, " is Found at index ", index)
            return True
        else:
            print(value, " Not Found")
        return False
    
    def get_index(self, value):
        index = 0
        for char in value:
            index += ord(char)
        index = index % self.size
        return index


set = HashSet()
set.add("Prat")
set.add("John")
set.add("Hair Cuts")

set.contains("Prat")
set.contains("John")
set.contains("Wayne")
