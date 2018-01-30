from domestic_terminal import Node, Dir, Type

graph = []

graph.append(Node('Tenter', 'Concourse T', Dir.E))
graph.append(Node('T8', 'Gate T10', Dir.E))
graph.append(Node('T9', 'Gate T9', Dir.E))

# These Distance Values are Not Accurate
graph[0].add_path('T8', 100, Dir.S, Type.NORMAL)
graph[0].add_path('T9', 100, Dir.N, Type.NORMAL)

for node in graph:
    print(node)