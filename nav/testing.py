from airport_graph import *

domestic = []

domestic.append(Node('Tenter', 'Concourse T', Type.Joint))
domestic.append(Node('T8', 'Gate T8', Type.Gate))
domestic.append(Node('T9', 'Gate T9', Type.Gate))
domestic.append(Node('T10', 'Gate T10', Type.Gate))
domestic.append(Node('T11', 'Gate T11', Type.Gate))
domestic.append(Node('T12', 'Gate T12', Type.Gate))

# These Distance Values are Not Accurate
domestic[0].add_path('T8', 100, Dir.S, Path.NORMAL)
domestic[1].add_path('Tenter', 100, Dir.N, Path.NORMAL)
domestic[0].add_path('T9', 100, Dir.N, Path.NORMAL)
domestic[2].add_path('Tenter', 100, Dir.S, Path.NORMAL)
domestic[2].add_path('T10', 100, Dir.N, Path.NORMAL)
domestic[3].add_path('T9', 100, Dir.S, Path.NORMAL)
domestic[3].add_path('T11', 100, Dir.N, Path.NORMAL)
domestic[4].add_path('T10', 100, Dir.S, Path.NORMAL)
domestic[4].add_path('T12', 100, Dir.N, Path.NORMAL)
domestic[5].add_path('T11', 100, Dir.S, Path.NORMAL)

route = find_path(domestic, 'Tenter', 'T12')
print(route)
# verify_graph(domestic)