class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, start):
        if not start:
            print(" Start Node not provided")
            return
        self.start = start
        self.end = start
        self.size = 1
    
    def enque(self, node):
        if not node:
            print(" Node not provided to Enque")
            return
        last_node = self.end
        last_node.next = node
        self.end = node
        node.prev = last_node
        self.size+=1
    
    def deque(self):
        if self.size == 0:
            print(" Queue is Empty")
            return None
        removed_node = self.start
        self.start = removed_node.next
        if self.start:
            self.start.prev = None
        else:
            self.end = None
        self.size -=1
        return removed_node
    
    def printQueue(self):
        str = ""
        if self.size == 0:
            print("Queue is empty")
        node = self.start
        while node:
            str = str + node.value + "-->"
            print(node.value, "-->", end = ' ')
            node = node.next
        print()
        # print(str)

A = Node('A')
B = Node('B')
C = Node('C')

# Queue = LinkedList(None)
Queue = LinkedList(A)
Queue.printQueue()
Queue.enque(B)
Queue.printQueue()
Queue.enque(C)
Queue.printQueue()
Queue.deque()
Queue.printQueue()
Queue.deque()
Queue.printQueue()
Queue.deque()
Queue.printQueue()
