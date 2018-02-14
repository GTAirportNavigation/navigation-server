import enum

## Angle Shortcuts Definitions ##
NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

def get_direction(degree):
    if degree == 0:
        return 'North'
    elif degree == 45:
        return 'Northeast'
    elif degree == 90:
        return 'East'
    elif degree == 135:
        return 'Southeast'
    elif degree == 180:
        return 'South'
    elif degree == 225:
        return 'Southwest'
    elif degree == 270:
        return 'West'
    elif degree == 315:
        return 'Northwest'

def opposite_directions(a, b):
    if a >= 180:
        a -= 180
        if a == b:
            return True
    else:
        a += 180
        if a == b:
            return True
    print(a, b)
    return False

# Node Type
class Type(enum.Enum):
    # A Joint is a node
    # with no intrinsic value
    # but connects other nodes
    Joint = 0
    Gate = 2
    # Airline Counter
    Counter = 3
    Food = 4
    Retail = 5
    Club = 7

# Graph Node
class Node(object):
    def __init__(self, id='', name='', type=Type.Joint, floor=0):
        self.id = id
        self.name = name
        self.type = type
        self.floor = floor
        self.paths = []
    def __str__(self):
        return 'ID: {} Name: \'{}\' Type: {}\nPaths: {}'.format(self.id, self.name, self.type, self.paths)
    def add_path(self, id, distance, angle, path_type):
        self.paths.append((id, distance, angle, path_type))

# Path Type
class Path(enum.Enum):
    NORMAL = 0
    STAIRS = 1
    ESCALATOR = 2
    ELEVATOR = 3
    TRAIN = 4

# Get Index in Graph from ID
def get_node_index(graph, id):
    index = 0
    for node in graph:
        if node.id == id:
            return index
        index += 1

# Wrapper to Obtain Instructions
# graph - array of nodes to search in
# start - id of the starting node
# end - id of the ending node
# constraints - TODO used to find paths
# with specific constraints
def find_path(graph, start, end, constraints=[]):    
    open = [get_node_index(graph, start)]
    visited = []
    route = [[]]
    while len(open) > 0:
        temp = open.pop(0)
        tr = route.pop(0)
        if graph[temp].id == end:
            tr.append(temp)
            return tr
        else:
            visited.append(temp)
            for path in graph[temp].paths:
                index = get_node_index(graph, path[0])
                if index not in visited:
                    open.append(index)
                    route.append(tr + [temp])

# Translate Node List into Path List
def translate(graph, directions):
    instructions = []
    for x in range(len(directions) - 1):
        for p in graph[directions[x]].paths:
            if p[0] == graph[directions[x + 1]].id:
                # print(p)
                # temp = 'Travel ' + get_direction(p[2]) + ' for ' + str(p[1]) + ' meters to ' + graph[directions[x + 1]].name + '.'
                temp = (graph[directions[x + 1]].name, p[1], p[2], p[3].value)
                instructions.append(temp)
    return instructions

def condense(instructions):
    counter = 0
    while(counter != (len(instructions) - 1)):
        if instructions[counter][2] == instructions[counter + 1][2] and instructions[counter][3] == instructions[counter + 1][3]:
            t1 = instructions.pop(counter)
            t2 = instructions.pop(counter)
            instructions.insert(counter, (t2[0], t1[1] + t2[1], t2[2], t2[3]))
        else:
            counter += 1
    return list(instructions)

# angle is the angle from node1 to node2
def insert_path(graph, node1, node2, distance, angle, path_type=Path.NORMAL):
    index1 = get_node_index(graph, node1)
    index2 = get_node_index(graph, node2)
    graph[index1].add_path(node2, distance, angle, path_type)
    angle2 = 0
    if angle >= 180:
        angle2 = angle - 180
    else:
        angle2 = angle + 180
    graph[index2].add_path(node1, distance, angle2, path_type)

def convert_to_json(instructions):
    json = '['
    for i in instructions:
        test = '[\"' + i[0] + '\", ' + str(i[1]) + ', ' + str(i[2]) + ', ' + str(i[3]) + '],'
        json += test
    json =json[:-1] + ']'
    return json

# Only Used for Testing Purposes
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
            angle = path1[2]
            node2 = get_node_index(graph, eid)
            verified = False
            for path2 in graph[node2].paths:
                if sid == path2[0] and distance == path2[1] and opposite_directions(angle, path2[2]):
                    verified = True
            if not verified:
                print('Error:', sid, eid)
    print('----')
