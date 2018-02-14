import enum

# Cardinal Direction
class Dir(enum.Enum):
    # N/A
    X = 0
    # North
    N = 1
    # South
    S = 2
    # East
    E = 3
    # West
    W = 4

# Graph Node
class Node(object):
    def __init__(self, id='', name='', dir=Dir.X, joint=False):
        self.id = id
        self.name = name
        # direction node is facing
        # useful in situations such as:
        # '500 feet on your LEFT'
        self.dir = dir
        # joint = True for nodes which have no
        # significance themselves, just as
        # connecting points to other nodes
        self.joint = False
        self.paths = []
    def __str__(self):
        return 'ID: {} Name: \'{}\' Joint: {}\nPaths: {}'.format(self.id, self.name, self.joint, self.paths)
    def add_path(self, id, distance, dir, type):
        self.paths.append((id, distance, dir, type))

# Edge Type
class Type(enum.Enum):
    NORMAL = 0
    STAIRS = 1
    ESCALATOR = 2
    TRAIN = 3