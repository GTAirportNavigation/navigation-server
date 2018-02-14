from .airport_graph import *

domestic = []

# T Concourse Missing Nodes: Elevators and Escalators !!
domestic.append(Node('TNenter', 'T Concourse', Type.Joint))
domestic.append(Node('TN', 'T Concourse', Type.Joint))
domestic.append(Node('TR24', 'News Express', Type.Retail))
domestic.append(Node('TG9', 'Gate T9', Type.Gate))
domestic.append(Node('TSenter', 'T Concourse', Type.Joint))
domestic.append(Node('TJ1', '', Type.Joint))
domestic.append(Node('TF12', 'Burger King', Type.Food))
domestic.append(Node('TR16', 'Travel Size Essentials', Type.Retail))
domestic.append(Node('TR19', 'BestBuy Zoom', Type.Retail))
domestic.append(Node('TJ2', '', Type.Joint))
domestic.append(Node('TR29', 'Z Market', Type.Retail))
domestic.append(Node('TJ3', '', Type.Joint))
domestic.append(Node('TG10', 'Gate T10', Type.Gate))
domestic.append(Node('TJ4', '', Type.Joint))
domestic.append(Node('TCAA', 'American Airlines Club', Type.Club))
domestic.append(Node('TJ5', '', Type.Joint))
domestic.append(Node('TG11', 'Gate T11', Type.Gate))
domestic.append(Node('TJ6', '', Type.Joint))
domestic.append(Node('TF6', 'Goldberg\'s Bagels', Type.Food))
domestic.append(Node('TJ7', '', Type.Joint))
domestic.append(Node('TG12', 'Gate T12', Type.Gate))
domestic.append(Node('TR26', 'Southern Flavors', Type.Retail))
domestic.append(Node('TF11', 'Vending Machines', Type.Food))
domestic.append(Node('TJ8', '', Type.Joint))
domestic.append(Node('TF8', 'Saucy Blues', Type.Food))
domestic.append(Node('TR17X1', 'Atlanta News and Gifts', Type.Retail))
domestic.append(Node('TJ9', '', Type.Joint))
domestic.append(Node('TG13', 'Gate T13', Type.Gate))
domestic.append(Node('TJ10', '', Type.Joint))
domestic.append(Node('TG14', 'Gate T14', Type.Gate))
domestic.append(Node('TG15', 'Gate T15', Type.Gate))
domestic.append(Node('TM', 'T Concourse', Type.Joint))
domestic.append(Node('TSenter', 'T Concourse', Type.Joint))
domestic.append(Node('TS', 'T Concourse', Type.Joint))
domestic.append(Node('TR25X1', 'Shellis News', Type.Retail))
domestic.append(Node('TR28', 'Tech Showcase', Type.Retail))
domestic.append(Node('TJ11', '', Type.Joint))
domestic.append(Node('TG8', 'Gate T8', Type.Gate))
domestic.append(Node('TR21', 'Headphone Hub', Type.Retail))
domestic.append(Node('TR22', 'Inmotion Entertainment', Type.Retail))
domestic.append(Node('TJ12', '', Type.Joint))
domestic.append(Node('TF7', 'Sam Adams / Checkpoint Bistro', Type.Food))
domestic.append(Node('TJ13', '', Type.Joint))
domestic.append(Node('TG7', 'Gate T7', Type.Gate))
domestic.append(Node('TJ14', '', Type.Joint))
domestic.append(Node('TF1', 'Bojangles', Type.Food))
domestic.append(Node('TCD', 'Delta Sky Club', Type.Club))
domestic.append(Node('TJ15', '', Type.Joint))
domestic.append(Node('TF5', 'Famous Famiglia', Type.Food))
domestic.append(Node('TF3', 'The Coffee Bean and Tea Leaf', Type.Food))
domestic.append(Node('TJ16', '', Type.Joint))
domestic.append(Node('TG6', 'Gate T6', Type.Gate))
domestic.append(Node('TJ17', '', Type.Joint))
domestic.append(Node('TR23', 'Lather', Type.Retail))
domestic.append(Node('TJ18', '', Type.Joint))
domestic.append(Node('TR27', 'Talie', Type.Retail))
domestic.append(Node('TG5', 'Gate T5', Type.Gate))
domestic.append(Node('TJ19', '', Type.Joint))
domestic.append(Node('TR17X2', 'Atlanta News and Gifts', Type.Retail))
domestic.append(Node('TJ20', '', Type.Joint))
domestic.append(Node('TR20', 'Brookstone', Type.Retail))
domestic.append(Node('TJ21', '', Type.Joint))
domestic.append(Node('TG4', 'Gate T4', Type.Gate))
domestic.append(Node('TJ22', '', Type.Joint))
domestic.append(Node('TF9', 'TJI Friday\'s', Type.Food))
domestic.append(Node('TJ23', '', Type.Joint))
domestic.append(Node('TF10', 'Jamba Juice', Type.Food))
domestic.append(Node('TJ24', '', Type.Joint))
domestic.append(Node('TF4', 'Corner Bakery Cafe', Type.Food))
domestic.append(Node('TJ25', '', Type.Joint))
domestic.append(Node('TG3', 'Gate T3', Type.Gate))
domestic.append(Node('TR18', 'B Iconic', Type.Retail))
domestic.append(Node('TJ26', '', Type.Joint))
domestic.append(Node('TR25X2', 'Shellis News', Type.Retail))
domestic.append(Node('TJ27', '', Type.Joint))
domestic.append(Node('TG2', 'Gate T2', Type.Gate))
domestic.append(Node('TG1', 'Gate T1', Type.Gate))

insert_path(domestic, 'TNenter', 'TN', 100, EAST)
insert_path(domestic, 'TN', 'TR24', 0, SOUTH)
insert_path(domestic, 'TN', 'TG9', 0, EAST)
insert_path(domestic, 'TN', 'TJ1', 100, NORTH)
insert_path(domestic, 'TJ1', 'TF12', 0, EAST)
insert_path(domestic, 'TJ1', 'TR16', 0, WEST)
insert_path(domestic, 'TJ1', 'TR19', 0, WEST)
insert_path(domestic, 'TJ1', 'TJ2', 100, NORTH)
insert_path(domestic, 'TJ2', 'TR29', 0, EAST)
insert_path(domestic, 'TJ2', 'TJ3', 100, NORTH)
insert_path(domestic, 'TJ3', 'TG10', 0, EAST)
insert_path(domestic, 'TJ3', 'TJ4', 100, NORTH)
insert_path(domestic, 'TJ4', 'TCAA', 0, WEST)
insert_path(domestic, 'TJ4', 'TJ5', 100, NORTH)
insert_path(domestic, 'TJ5', 'TG11', 0, EAST)
insert_path(domestic, 'TJ5', 'TJ6', 100, NORTH)
insert_path(domestic, 'TJ6', 'TF6', 0, EAST)
insert_path(domestic, 'TJ6', 'TJ7', 100, NORTH)
insert_path(domestic, 'TJ7', 'TG12', 0, EAST)
insert_path(domestic, 'TJ7', 'TR26', 0, WEST)
insert_path(domestic, 'TJ7', 'TF11', 0, WEST)
insert_path(domestic, 'TJ7', 'TJ8', 100, NORTH)
insert_path(domestic, 'TJ8', 'TF8', 0, EAST)
insert_path(domestic, 'TJ8', 'TR17X1', 0, EAST)
insert_path(domestic, 'TJ8', 'TJ9', 100, NORTH)
insert_path(domestic, 'TJ9', 'TG13', 0, EAST)
insert_path(domestic, 'TJ9', 'TJ10', 100, NORTH)
insert_path(domestic, 'TJ10', 'TG14', 0, EAST)
insert_path(domestic, 'TJ10', 'TG15', 100, NORTH)

insert_path(domestic, 'TN', 'TM', 100, SOUTH)
insert_path(domestic, 'TM', 'TS', 100, SOUTH)
insert_path(domestic, 'TSenter', 'TS', 100, EAST)
insert_path(domestic, 'TSenter', 'TR25X1', 0, NORTH)
insert_path(domestic, 'TSenter', 'TR28', 0, NORTH)
insert_path(domestic, 'TS', 'TJ11', 100, SOUTH)
insert_path(domestic, 'TJ11', 'TG8', 0, EAST)
insert_path(domestic, 'TJ11', 'TR21', 0, WEST)
insert_path(domestic, 'TJ11', 'TR22', 0, WEST)
insert_path(domestic, 'TJ11', 'TJ12', 100, SOUTH)
insert_path(domestic, 'TJ12', 'TF7', 0, WEST)
insert_path(domestic, 'TJ12', 'TJ13', 100, SOUTH)
insert_path(domestic, 'TJ13', 'TG7', 0, EAST)
insert_path(domestic, 'TJ13', 'TJ14', 100, SOUTH)
insert_path(domestic, 'TJ14', 'TF1', 0, WEST)
insert_path(domestic, 'TJ14', 'TCD', 0, EAST)
insert_path(domestic, 'TJ14', 'TJ15', 100, SOUTH)
insert_path(domestic, 'TJ15', 'TF5', 0, WEST)
insert_path(domestic, 'TJ15', 'TF3', 0, EAST)
insert_path(domestic, 'TJ15', 'TJ16', 100, SOUTH)
insert_path(domestic, 'TJ16', 'TG6', 0, EAST)
insert_path(domestic, 'TJ16', 'TJ17', 100, SOUTH)
insert_path(domestic, 'TJ17', 'TR23', 0, WEST)
insert_path(domestic, 'TJ17', 'TJ18', 100, SOUTH)
insert_path(domestic, 'TJ18', 'TR27', 0, WEST)
insert_path(domestic, 'TJ18', 'TG5', 0, EAST)
insert_path(domestic, 'TJ18', 'TJ19', 100, SOUTH)
insert_path(domestic, 'TJ19', 'TR17X2', 0, WEST)
insert_path(domestic, 'TJ19', 'TJ20', 100, SOUTH)
insert_path(domestic, 'TJ19', 'TR20', 0, WEST)
insert_path(domestic, 'TJ20', 'TJ21', 100, SOUTH)
insert_path(domestic, 'TJ21', 'TG4', 0, EAST)
insert_path(domestic, 'TJ21', 'TJ22', 100, SOUTH)
insert_path(domestic, 'TJ22', 'TF9', 0, WEST)
insert_path(domestic, 'TJ22', 'TJ23', 100, SOUTH)
insert_path(domestic, 'TJ22', 'TF10', 0, WEST)
insert_path(domestic, 'TJ23', 'TJ24', 100, SOUTH)
insert_path(domestic, 'TJ22', 'TF4', 0, WEST)
insert_path(domestic, 'TJ24', 'TJ25', 100, SOUTH)
insert_path(domestic, 'TJ25', 'TG3', 0, EAST)
insert_path(domestic, 'TJ25', 'TR18', 0, WEST)
insert_path(domestic, 'TJ25', 'TJ26', 100, SOUTH)
insert_path(domestic, 'TJ26', 'TR25X2', 0, WEST)
insert_path(domestic, 'TJ26', 'TJ27', 100, SOUTH)
insert_path(domestic, 'TJ27', 'TG2', 0, EAST)
# North East 'ahead on your right'
insert_path(domestic, 'TJ27', 'TG1', 0, 135)

# route = find_path(domestic, 'TNenter', 'TG2')
# print(route)
# instructions = translate(domestic, route)
# condense(instructions)
# print(instructions)
# verify_graph(domestic)
