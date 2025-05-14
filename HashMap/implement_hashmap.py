# Assumptions:  Keys are strings, Values are strings
# In case of collissions, we will keep the list of strings in the same index
'''
Functions to implement:
put(key,value)
get(key) => returns value. list of values in case of collisions
keys() => list of keys
values() => list of values
contains(key) => True if the key contains a value

We will implement this as a list. We will "hash" the key into an index
Each element in the list is itself a list (to handle collisions)
'''

class HashMap:
    def __init__(self, size = 20):
        self.size = size
        self.map = [[] for i in range(self.size)]
    
    def put(self, key, value):
        index = self.get_index(key)
        self.map[index].append(value)
        print("Inserting value ", value, " at Index ", index)
    
    def get(self, key):
        index = self.get_index(key)
        if self.map[index]:
            return self.map[index]
        return None

    def get_index(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index = index % self.size
        return index
    
    def contains(self, key):
        index = self.get_index(key)
        if self.map[index]:
            return True
        return False


map = HashMap()
map.put("name", "Prat")
map.put("LN", "Sharma")
map.put("Course", "CS")
