from airport_graph import *

graph = []

graph.append(Node('Tenter', 'Concourse T', Dir.E, Type.Joint))
graph.append(Node('T8', 'Gate T8', Dir.E, Type.Gate))
graph.append(Node('T9', 'Gate T9', Dir.E, Type.Gate))
graph.append(Node('T10', 'Gate T10', Dir.E, Type.Gate))
graph.append(Node('T11', 'Gate T11', Dir.E, Type.Gate))

# These Distance Values are Not Accurate
graph[0].add_path('T8', 100, Dir.S, Path.NORMAL)
graph[0].add_path('T9', 100, Dir.N, Path.NORMAL)
graph[2].add_path('T10', 100, Dir.N, Path.NORMAL)
graph[3].add_path('T11', 100, Dir.N, Path.NORMAL)

find_path(graph, 'Tenter', 'T11')
