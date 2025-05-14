
class TrieNode:
    def __init__(self, charval = ''):
        self.char = charval
        self.children = {}
        self.end_of_word = False
    
    def insert(self,word):
        parent = self
        for char in word:
            if char in parent.children:
                parent = parent.children[char]
            else:
                new_node = TrieNode(char)
                parent.children[char] = new_node
                parent = new_node
        parent.end_of_word = True
        return
    
    def search(self, word):
        parent = self
        for char in word:
            if char in parent.children:
                parent = parent.children[char]
            else:
                return False
        return parent.end_of_word
    
    def search_prefix(self,pre):
        parent = self
        for char in word:
            if char in parent.children:
                parent = parent.children[char]
            else:
                return False
        return True
    
    def print_trie(self, level=0):
        indent = "  " * level
        marker = "*" if self.end_of_word else ""
        if self.char:  # skip printing root's empty char
            print(f"{indent}{self.char}{marker}")
        for child in self.children.values():
            child.print_trie(level + 1)

    

    

trie = TrieNode()
trie.print_trie()
insert_list = ["car", "cat", "dog"]
search_list = ["cap", "cat", "ca", "c", "dog", ""]
for word in insert_list:
    trie.insert(word)

for word in search_list:
    if trie.search(word):
        print(" Word ", word, " Found")
    else:
        print(" Word ", word, " NOT Found")

for word in search_list:
    if trie.search_prefix(word):
        print(" Prefix ", word, " Found")
    else:
        print(" Prefix ", word, " NOT Found")

'''
Test Cases:
insert "cat", "car", "dog"
'''