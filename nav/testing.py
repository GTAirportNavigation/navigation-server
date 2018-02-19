# from nav.airport_graph import *
from models import *

domestic = []

<<<<<<< HEAD
# T Concourse Missing Nodes: Elevators and Escalators !!
domestic.append(Node('TNenter', 'T EnumField'
                                '.NORTH', EnumField.JOINT))
domestic.append(Node('TN', 'T EnumField'
                           '.NORTH'
                           , EnumField.JOINT))
domestic.append(Node('TR24', 'News Express', EnumField.Retail))
domestic.append(Node('TG9', 'Gate T9', EnumField
                     .Gate))
domestic.append(Node('TSenter', 'Concourse T', EnumField
                     .JOINT))
domestic.append(Node('TJ1', '', EnumField
                     .JOINT))
domestic.append(Node('TF12', 'Burger King', EnumField
                     .Food))
domestic.append(Node('TR16', 'Travel Size Essentials', EnumField
                     .Retail))
domestic.append(Node('TR19', 'BestBuy Zoom', EnumField
                     .Retail))
domestic.append(Node('TJ2', '', EnumField
                     .JOINT))
domestic.append(Node('TR29', 'Z Market', EnumField
                     .Retail))
domestic.append(Node('TJ3', '', EnumField
                     .JOINT))
domestic.append(Node('TG10', 'Gate T10', EnumField
                     .Gate))
domestic.append(Node('TJ4', '', EnumField
                     .JOINT))
domestic.append(Node('TCAA', 'American Airlines Club', EnumField
                     .Club))
domestic.append(Node('TJ5', '', EnumField
                     .JOINT))
domestic.append(Node('TG11', 'Gate T11', EnumField
                     .Gate))
domestic.append(Node('TJ6', '', EnumField
                     .JOINT))
domestic.append(Node('TF6', 'Goldberg\'s Bagels', EnumField
                     .Food))
domestic.append(Node('TJ7', '', EnumField
                     .JOINT))
domestic.append(Node('TG12', 'Gate T12', EnumField
                     .Gate))
domestic.append(Node('TR26', 'EnumField'
                             '.SOUTHern Flavors', EnumField
                     .Retail))
domestic.append(Node('TF11', 'Vending Machines', EnumField
                     .Food))
domestic.append(Node('TJ8', '', EnumField
                     .JOINT))
domestic.append(Node('TF8', 'Saucy Blues', EnumField
                     .Food))
domestic.append(Node('TR17', 'Atlanta News and Gifts', EnumField
                     .Retail))
domestic.append(Node('TJ9', '', EnumField
                     .JOINT))
domestic.append(Node('TG13', 'Gate T13', EnumField
                     .Gate))
domestic.append(Node('TJ10', '', EnumField
                     .JOINT))
domestic.append(Node('TG14', 'Gate T14', EnumField
                     .Gate))
domestic.append(Node('TG15', 'Gate T15', EnumField
                     .Gate))
domestic.append(Node('TM', 'T Middle', EnumField
                     .JOINT))
domestic.append(Node('TSenter', 'T EnumField'
                                '.SOUTH', EnumField
                     .JOINT))
domestic.append(Node('TS', 'T EnumField'
                           '.SOUTH', EnumField
                     .JOINT))
domestic.append(Node('TR25', 'Shellis News', EnumField
                     .Retail))
domestic.append(Node('TR28', 'Tech Showcase', EnumField
                     .Retail))
domestic.append(Node('TJ11', '', EnumField
                     .JOINT))
domestic.append(Node('TG8', 'Gate T8', EnumField
                     .Gate))
domestic.append(Node('TR21', 'Headphone Hub', EnumField
                     .Retail))
domestic.append(Node('TR22', 'Inmotion Entertainment', EnumField
                     .Retail))
domestic.append(Node('TJ12', '', EnumField
                     .JOINT))
domestic.append(Node('TF7', 'Sam Adams / Checkpoint Bistro', EnumField
                     .Food))
domestic.append(Node('TJ13', '', EnumField
                     .JOINT))
domestic.append(Node('TG7', 'Gate T7', EnumField
                     .Gate))
domestic.append(Node('TJ14', '', EnumField
                     .JOINT))
domestic.append(Node('TF1', 'Bojangles', EnumField
                     .Food))
domestic.append(Node('TCD', 'Delta Sky Club', EnumField
                     .Club))
domestic.append(Node('TJ15', '', EnumField
                     .JOINT))
domestic.append(Node('TF5', 'Famous Famiglia', EnumField
                     .Food))
domestic.append(Node('TF3', 'The Coffee Bean and Tea Leaf', EnumField
                     .Food))
domestic.append(Node('TJ16', '', EnumField
                     .JOINT))
domestic.append(Node('TG6', 'Gate T6', EnumField
                     .Gate))
domestic.append(Node('TJ17', '', EnumField
                     .JOINT))
domestic.append(Node('TR23', 'Lather', EnumField
                     .Retail))
domestic.append(Node('TJ18', '', EnumField
                     .JOINT))
domestic.append(Node('TR27', 'Talie', EnumField
                     .Retail))
domestic.append(Node('TG5', 'Gate T5', EnumField
                     .Gate))
domestic.append(Node('TJ19', '', EnumField
                     .JOINT))
domestic.append(Node('TR17', 'Atlanta News and Gifts', EnumField
                     .Retail))
domestic.append(Node('TJ20', '', EnumField
                     .JOINT))
domestic.append(Node('TR20', 'Brookstone', EnumField
                     .Retail))
domestic.append(Node('TJ21', '', EnumField
                     .JOINT))
domestic.append(Node('TG4', 'Gate T4', EnumField
                     .Gate))
domestic.append(Node('TJ22', '', EnumField
                     .JOINT))
domestic.append(Node('TF9', 'TJI Friday\'s', EnumField
                     .Food))
domestic.append(Node('TJ23', '', EnumField
                     .JOINT))
domestic.append(Node('TF10', 'Jamba Juice', EnumField
                     .Food))
domestic.append(Node('TJ24', '', EnumField
                     .JOINT))
domestic.append(Node('TF4', 'Corner Bakery Cafe', EnumField
                     .Food))
domestic.append(Node('TJ25', '', EnumField
                     .JOINT))
domestic.append(Node('TG3', 'Gate T3', EnumField
                     .Gate))
domestic.append(Node('TR18', 'B Iconic', EnumField
                     .Retail))
domestic.append(Node('TJ26', '', EnumField
                     .JOINT))
domestic.append(Node('TR25', 'Shellis News', EnumField
                     .Retail))
domestic.append(Node('TJ27', '', EnumField
                     .JOINT))
domestic.append(Node('TG2', 'Gate T2', EnumField
                     .Gate))
domestic.append(Node('TG1', 'Gate T1', EnumField
                     .Gate))

insert_path(domestic, 'TNenter', 'TN', 100, EnumField
            .EAST)
insert_path(domestic, 'TN', 'TR24', 0, EnumField
            .SOUTH)
insert_path(domestic, 'TN', 'TG9', 0, EnumField
            .EAST)
insert_path(domestic, 'TN', 'TJ1', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ1', 'TF12', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ1', 'TR16', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ1', 'TR19', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ1', 'TJ2', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ2', 'TR29', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ2', 'TJ3', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ3', 'TG10', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ3', 'TJ4', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ4', 'TCAA', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ4', 'TJ5', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ5', 'TG11', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ5', 'TJ6', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ6', 'TF6', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ6', 'TJ7', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ7', 'TG12', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ7', 'TR26', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ7', 'TF11', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ7', 'TJ8', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ8', 'TF8', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ8', 'TR17', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ8', 'TJ9', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ9', 'TG13', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ9', 'TJ10', 100, EnumField
            .NORTH
        )
insert_path(domestic, 'TJ10', 'TG14', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ10', 'TG15', 100, EnumField
            .NORTH
        )
=======
graph.append(Node('Tenter', 'Concourse T', Dir.E))
graph.append(Node('T8', 'Gate T8', Dir.E))
graph.append(Node('T9', 'Gate T9', Dir.E))
graph.append(Node('T10', 'Gate T10', Dir.NE))
# These Distance Values are Not Accurate
graph[0].add_path('T8', 100, Dir.S, Type.NORMAL)
node = Node('T9', 'Gate T9', Dir.N)
graph[0].add_neighbour(node, Dir.S, 10, Type.NORMAL)
graph[0].add_neighbour(node, Dir.N, 10, Type.NORMAL)
print(graph[0])


graph[0].add_path('T9', 100, Dir.N, Type.NORMAL)
graph[2].add_path('T10', 100, Dir.NE, Type.NORMAL)
>>>>>>> fd71339c96ff10fc32f120bc13756a2520def0a8

insert_path(domestic, 'TN', 'TM', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TM', 'TS', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TSenter', 'TS', 100, EnumField
            .EAST)
insert_path(domestic, 'TSenter', 'TR25', 0, EnumField
            .NORTH
        )
insert_path(domestic, 'TSenter', 'TR28', 0, EnumField
            .NORTH
        )
insert_path(domestic, 'TS', 'TJ11', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ11', 'TG8', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ11', 'TR21', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ11', 'TR22', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ11', 'TJ12', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ12', 'TF7', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ12', 'TJ13', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ13', 'TG7', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ13', 'TJ14', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ14', 'TF1', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ14', 'TCD', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ14', 'TJ15', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ15', 'TF5', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ15', 'TF3', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ15', 'TJ16', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ16', 'TG6', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ16', 'TJ17', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ17', 'TR23', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ17', 'TJ18', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ18', 'TR27', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ18', 'TG5', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ18', 'TJ19', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ19', 'TR17', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ19', 'TJ20', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ19', 'TR20', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ20', 'TJ21', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ21', 'TG4', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ21', 'TJ22', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ22', 'TF9', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ22', 'TJ23', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ22', 'TF10', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ23', 'TJ24', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ22', 'TF4', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ24', 'TJ25', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ25', 'TG3', 0, EnumField
            .EAST)
insert_path(domestic, 'TJ25', 'TR18', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ25', 'TJ26', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ26', 'TR25', 0, EnumField
            .WEST)
insert_path(domestic, 'TJ26', 'TJ27', 100, EnumField
            .SOUTH)
insert_path(domestic, 'TJ27', 'TG2', 0, EnumField
            .EAST)
# EnumField
# .NORTH
# EnumField
# .EAS 'ahead on your right'
insert_path(domestic, 'TJ27', 'TG1', 0, 135)

route = find_path(domestic, 'TNenter', 'TG2')
print(route)
verify_graph(domestic)