from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    
    def add_neighbor(self, neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)

def bfs_print_at_levels(root):
    level = 0
    lists_by_levels = []
    dummy = Node("dummy")
    if not root:
        return
    print("Level ",level, " Nodes :")
    queue = deque([root])
    queue.append(dummy)
    while queue:
        node = queue.popleft()
        print(node.value, " ")
        for neighbor in node.neighbors:
            queue.append(neighbor)
        if(node.value == "dummy" and queue):
            queue.append(dummy)
            level+=1
            print("\n")
            print("Level ", level, " Nodes: ")


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

bfs_print_at_levels(nodeA)
        

