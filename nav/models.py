from django.db import models


# class Test(models.Model):
# 	name = models.CharField(max_length=50)
#
# 	class Meta:
# 		db_table = 'test'
#
# 	def get_name(self):
# 		return self.name

class EnumField(models.Field):
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        if not self.choices:
            raise AttributeError('EnumField requires `choices` attribute.')
    def db_type(self):
        return "enum(%s)" % ','.join("'%s'" % k for (k, _) in self.choices)

    NORMAL = 0
    STAIRS = 1
    ESCALATOR = 2
    ELEVATOR = 3
    TRAIN = 4

    PATH_CHOICES = (
        (NORMAL, 'Normal'),
        (STAIRS, 'Stair'),
        (ELEVATOR, 'Elevator'),
        (TRAIN, 'Train'),
    )

    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

    DIRECTIONS_CHOICES = (
        (NORTH, 'North'),
        (EAST, 'East'),
        (SOUTH, 'South'),
        (WEST, 'West'),
    )

    JOINT = 0
    GATE = 2
    COUNTER = 3
    FOOD = 4
    RETAIL = 5
    CLUB = 7

    TYPE_CHOICES = (
        (JOINT, 'Joint'),
        (GATE, 'Gate'),
        (COUNTER, 'Counter'),
        (FOOD, 'Food'),
        (RETAIL, 'Retail'),
        (CLUB, 'Club'),
    )



class Node(models.Model):

    name = models.CharField(max_length=50, blank=True)
    id = models.CharField(max_length=50, primary_key=True)
    # node_id = models.CharField(max_length=50, blank=True)
    type = models.IntegerField(EnumField.TYPE_CHOICES)
    # direction = models.IntegerField(EnumField.DIRECTIONS_CHOICES)
    # path = models.IntegerField(EnumField.PATH_CHOICES)
    neighbours = models.ManyToManyField("self", blank=True)
    floor = models.IntegerField(default=0)

    # def __str__(self):
    #     return 'ID: {} Name: \'{}\' Type: {}\nPaths: {}'.format(self.id, self.name, self.type, self.paths)


    # def add_path(self, id, distance, angle, path_type):
    #     self.paths.append((id, distance, angle, path_type))

    class Meta:
        db_table ='Node'

    def get_name(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super(Node, self).save(*args, **kwargs)
        except Exception as e:
            print('ERROR', e)


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

def get_node_index(graph, id):
    index = 0
    for node in graph:
        if node.id == id:
            return index
        index += 1


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

def insert_path(graph, node1, node2, distance, angle, path_type=EnumField.NORMAL):
    index1 = get_node_index(graph, node1)
    index2 = get_node_index(graph, node2)
    graph[index1].add_path(node2, distance, angle, path_type)
    angle2 = 0
    if angle >= 180:
        angle2 = angle - 180
    else:
        angle2 = angle + 180
    graph[index2].add_path(node1, distance, angle2, path_type)




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
