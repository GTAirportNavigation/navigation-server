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

def opposite_directions(a, b):
    av = a.value
    bv = b.value
    if av == 0 or bv == 0:
        return False
    if av > 4:
        av -= 4
        if av == bv:
            return True
    else:
        av += 4
        if av == bv:
            return True
    return False

# Node Type
class Type(enum.Enum):
    # A Joint is a node
    # with no intrinsic value
    # but connects other nodes
    Joint = 0
    Gate = 1
    # Airline Counter
    Counter = 2
    Restaurant = 3
    Store = 4

# Graph Node
class Node(object):
    def __init__(self, id='', name='', dir=Dir.X, type=Type.Joint):
        self.id = id
        self.name = name
        # direction node is facing
        # useful in situations such as:
        # '500 feet on your LEFT'
        self.dir = dir
        self.type = type
        self.paths = []
    def __str__(self):
        return 'ID: {} Name: \'{}\' Type: {}\nPaths: {}'.format(self.id, self.name, self.type, self.paths)
    def add_path(self, id, distance, dir, path_type):
        self.paths.append((id, distance, dir, path_type))

# Path Type
class Path(enum.Enum):
    NORMAL = 0
    STAIRS = 1
    ESCALATOR_UP = 2
    # Escalator Down
    ESCALATOR_DW = 3
    ELEVATOR = 4
    TRAIN = 5

# Get Index in Graph from ID
def get_node_index(graph, id):
    index = 0
    for node in graph:
        if node.id == id:
            return index
        index += 1

# Wrapper to Obtain Instructions
def find_path(graph, start, end, parameters=[]):    
    open = [get_node_index(graph, start)]
    closed = []
    route = [[]]
    while len(open) > 0:
        temp = open.pop(0)
        tr = route.pop(0)
        if graph[temp].id == end:
            tr.append(temp)
            return tr
        else:
            closed.append(temp)
            for path in graph[temp].paths:
                index = get_node_index(graph, path[0])
                if index not in closed:
                    open.append(index)
                    route.append(tr + [temp])

# Ensure All Edges Are Reversed
# Also Checks Matching Distance Values
# As Well As Opposing Directions
def verify_graph(graph):
    print('Errors Deteced:')
    for node1 in graph:
        sid = node1.id
        for path1 in node1.paths:
            eid = path1[0]
            distance = path1[1]
            dir = path1[2]
            node2 = get_node_index(graph, eid)
            verified = False
            for path2 in graph[node2].paths:
                if path2[0] == sid and path2[1] == distance and opposite_directions(path2[2], dir):
                    verified = True
            if not verified:
                print('Error:', sid, eid)
    print('----')