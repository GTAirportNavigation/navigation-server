from .models import *
from .testing import test_neighbors

def test():
    test_neighbors()
    # temp = Node('A', 'temp', EnumField.JOINT)
    # temp.save()
    print('Nodes Saved')
