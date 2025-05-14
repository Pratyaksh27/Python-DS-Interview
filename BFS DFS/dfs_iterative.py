from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.neighbors = []
    
    def add_neighbor(self, v):
        for node in v:
            self.neighbors.append(node)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeA.add_neighbor([nodeB, nodeD])
nodeB.add_neighbor([nodeC, nodeE, nodeF])
nodeF.add_neighbor([nodeG, nodeH])


def dfs_iterative(root):
    stack = deque()
    root.visited = True
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.value, " ")
        for neighbor in node.neighbors:
            stack.append(neighbor)

dfs_iterative(nodeA)

