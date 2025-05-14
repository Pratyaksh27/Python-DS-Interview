from queue import PriorityQueue

# Input: Graph. Map of list of tuples
# Starting Node root
graph = {
    'A':[('B',3),('C',1)],
    'B':[('D',2),('E',3), ('A',3), ('C',1)],
    'C':[('A',1),('B',1), ('E',4)],
    'D':[('B',2), ('E',2)],
    'E':[('D',2), ('B',3), ('C',4)]
}

#Output
# distance: A Map {node, distance(int)}
# prev: A Map {node: node(nullable)}

# Algorithm
# We need a PQ instead of Q because at every step we take out the smallest 
# distance node out of PQ and its value is set forever. That is when we mark that node as visited
# 1. Put (0,root) in PQ
# 2. While pq is not empty
#  -- Take out the smallest distance node
#  -- Amongst all its neighbors, IF THEY HAVE NOT BEEN VISITED (akas their shortest distance is NOT YET FIXED),
#       :: Put them in PQ with dist = current_node.dist + weight of the edge

def dijkstra(graph, root):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    visited = set()

    pq = PriorityQueue()
    distances[root] = 0
    pq.put([0,root])

    while not pq.empty():
        current_distance, current_node = pq.get()
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_dist = current_distance + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                pq.put((new_dist, neighbor))
                previous[neighbor] = current_node
    return distances, previous


distances, previous = dijkstra(graph, 'A')
for key,value in distances.items():
    print(" Node ", key, " Distance from A: ", value)

for key, value in previous.items():
    print(" For Node ",key, " the Prev is ", value)



