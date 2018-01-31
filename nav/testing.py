from airport_graph import *

graph = []

graph.append(Node('Tenter', 'Concourse T', Dir.E))
graph.append(Node('T8', 'Gate T8', Dir.E))
graph.append(Node('T9', 'Gate T9', Dir.E))
graph.append(Node('T10', 'Gate T10', Dir.NE))
# These Distance Values are Not Accurate
graph[0].add_path('T8', 100, Dir.S, Type.NORMAL)
node = Node('T9', 'Gate T9', Dir.N)
graph[0].add_neighbour(node, Dir.S, 10, Type.NORMAL)
graph[0].add_neighbour(node, Dir.N, 10, Type.NORMAL)
print(graph[0])


graph[0].add_path('T9', 100, Dir.N, Type.NORMAL)
graph[2].add_path('T10', 100, Dir.NE, Type.NORMAL)

find_path(graph, 'Tenter', 'T10')