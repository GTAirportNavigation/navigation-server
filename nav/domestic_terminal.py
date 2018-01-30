from enum import Enum

# Graph Node
class Node(object):
    def __init__(self, id='', name=''):
        self.id = id
        self.name = name
        self.paths = []
    def add_path(self, id, distance, dir, type):
        self.paths.append((id, distance, dir, type))

# Cardinal Direction
class Dir(Enum):
    N = 0
    S = 1
    E = 2
    W = 3

# For Time Calculation
class Type(Enum):
    NORMAL = 0
    STAIRS = 1
    ESCALATOR = 2
    TRAIN = 3