from queue import PriorityQueue

def dikstra(graph, root):
    # Will Log distances of EACH node with a distance Value
    dist = {node: float('inf') for node in graph}
    dist[root] = 0
    # Will keep the prev node for every node. For root it will be None
    prev = {node: None for node in graph}
    visited = set()
    pq = PriorityQueue()
    pq.put([0,root])

    while not pq.empty():
        current_distance, current_node = pq.get()
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor,weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_dist = current_distance + weight
            if (new_dist < dist[neighbor]):
                dist[neighbor] = new_dist
                prev[neighbor] = current_node
                pq.put((new_dist, neighbor))
    
    return dist, prev



graph = {
    'A':[('B',3),('C',1)],
    'B':[('D',2),('E',3), ('A',3), ('C',1)],
    'C':[('A',1),('B',1), ('E',4)],
    'D':[('B',2), ('E',2)],
    'E':[('D',2), ('B',3), ('C',4)]
}

distance, previous = dikstra(graph, 'A')

print("Shortest distances from A:")
for node, d in distance.items():
    print(f"A -> {node} = {d}")