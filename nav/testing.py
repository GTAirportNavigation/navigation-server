from domestic_terminal import Node, Dir, Type

graph = []

graph.append(Node(id='Tenter', 'Concourse T'))
graph.append(Node(id='T8', 'Gate T10'))
graph.append(Node(id='T9', 'Gate T9'))

# These Distance Values are Not Accurate
graph[0].add_path('T8', 100, Dir.S, Type.Normal)
graph[0].add_path('T9', 100, Dir.N, Type.Normal)