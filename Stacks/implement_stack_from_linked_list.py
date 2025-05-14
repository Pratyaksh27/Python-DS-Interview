class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        
    
    def push(self,node):
        if not node:
            return
        if self.size == 0:
            self.top = node
            self.size += 1
            return
        top_node = self.top
        top_node.next = node
        node.prev = top_node
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Stack is Empty")
            return
        top_node = self.top
        prev_node = top_node.prev
        if prev_node:
            prev_node.next = None
        self.top = prev_node
        self.size-=1
        return top_node
    
    def printFromTop(self):
        if self.size == 0:
            print("Stack is Empty")
            return
        top_node = self.top
        print("Start of Stack")
        while top_node:
            print(top_node.value)
            top_node = top_node.prev
        print("End OF Stack")

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

stak = Stack()
stak.printFromTop()
stak.push(A)
stak.printFromTop()
stak.push(B)
stak.push(C)
stak.push(D)
stak.printFromTop()
stak.pop()
stak.printFromTop()
stak.pop()
stak.printFromTop()
stak.pop()
stak.printFromTop()
stak.pop()
stak.printFromTop()



