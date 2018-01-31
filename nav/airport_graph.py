import enum

# Cardinal Direction
class Dir(enum.Enum):
    # N/A
    X = 0
    # North
    N = 1
    NE = 2
    # South
    E = 3
    SE = 4
    # East
    S = 5
    SW = 6
    # West
    W = 7
    NW = 8
   


# Graph Node
class Node(object):
    def __init__(self, id='', name='', dir=Dir.X, joint=False):
        self.id = id
        self.name = name
        # direction node is facing
        # useful in situations such as:
        # '500 feet on your LEFT'
        self.dir = dir
        # adjacent nodes of the current node
        self.neighbours = set()
        # joint = True for nodes which have no
        # significance themselves, just as
        # connecting points to other nodes
        self.joint = False
        self.paths = []
    def __str__(self):
        return 'ID: {} Name: \'{}\' Joint: {}\nPaths: {}'.format(self.id, self.name, self.joint, self.paths)
    def add_path(self, id, distance, dir, type):
        self.paths.append((id, distance, dir, type))
        # add adjacent node of the current location, the dir is relative to the current location
    def add_neighbour(self, neighbour, dir, distance, type):
        if neighbour not in self.neighbours:
            self.dir = dir
            self.neighbours.add(neighbour)


# Edge Type
class Type(enum.Enum):
    NORMAL = 0
    STAIRS = 1
    ESCALATOR = 2
    TRAIN = 3

def get_node(graph, id):
    index = 0
    for node in graph:
        if node.id == id:
            return index
        index += 1

# Wrapper to Obtain Instructions
def find_path(graph, start, end, parameters=[]):    
    open = [get_node(graph, start)]
    closed = []
    route = [[]]
    while len(open) > 0:
        temp = open.pop(0)
        tr = route.pop(0)
        if graph[temp].id == end:
            tr.append(temp)
            print(tr)
        else:
            closed.append(temp)
            for path in graph[temp].paths:
                index = get_node(graph, path[0])
                if index not in closed:
                    open.append(index)
                    route.append(tr + [temp])