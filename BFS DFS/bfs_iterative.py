from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []
    
    def add_neighbor(self, v):
        for node in v:
            self.neighbors.append(node)


def bfs_iterative(root):
    if not root:
        return[]
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, " ")
        for neighbor in node.neighbors:
            queue.append(neighbor)


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

bfs_iterative(nodeA)



