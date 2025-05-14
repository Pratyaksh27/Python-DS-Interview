from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.distance = -1

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


def bfs_set_distances(graph, root):
    if not root:
        return
    root.visited = True
    root.distance = 0
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(" Node ", node.value, " is at distance ", node.distance, " from root ", root.value)
        for neighbor in graph[node]:
            if neighbor.distance == -1 or neighbor.distance < node.distance +1:
                neighbor.distance = node.distance+1
                queue.append(neighbor)

bfs_set_distances(graph, A)