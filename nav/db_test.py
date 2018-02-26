from .models import *
from .testing import test_neighbors, insert_all_nodes

def test():
    insert_all_nodes()
    test_neighbors()
    # temp = Node('A', 'temp', EnumField.JOINT)
    # temp.save()
    print('Nodes Saved')
