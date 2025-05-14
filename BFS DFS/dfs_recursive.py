class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')


graph = {
    A: [B, D],
    B: [C, E, F],
    C: [],
    D: [],
    E: [],
    F: [G, H],
    G: [],
    H: []
}

def DFS (graph, root):
    root.visited = True
    print("Entering" , root.value, " ")
    for node in graph[root]:
        if node.visited == False:
            DFS(graph, node)
    print("Exiting ", root.value, " ")

DFS(graph, A)
