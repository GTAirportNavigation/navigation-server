from .models import *
# from .airport_graph import *
domestic = []


def test_neighbors():
    Node.objects.get(id='TXN').neighbours.add(Node.objects.get(id='TN'))
    Node.objects.get(id='TN').neighbours.add(Node.objects.get(id='TXN'))
    Node.objects.get(id='TR24').neighbours.add(Node.objects.get(id='TN'))
    Node.objects.get(id='TN').neighbours.add(Node.objects.get(id='TR24'))
    Node.objects.get(id='TN').neighbours.add(Node.objects.get(id='TG9'))
    Node.objects.get(id='TG9').neighbours.add(Node.objects.get(id='TN'))
    Node.objects.get(id='TN').neighbours.add(Node.objects.get(id='TJ1'))
    Node.objects.get(id='TJ1').neighbours.add(Node.objects.get(id='TN'))
    Node.objects.get(id='TJ1').neighbours.add(Node.objects.get(id='TF12'))
    Node.objects.get(id='TF12').neighbours.add(Node.objects.get(id='TJ1'))
    Node.objects.get(id='TJ1').neighbours.add(Node.objects.get(id='TR16'))
    Node.objects.get(id='TR16').neighbours.add(Node.objects.get(id='TJ1'))
    Node.objects.get(id='TJ1').neighbours.add(Node.objects.get(id='TJ19'))
    Node.objects.get(id='TJ19').neighbours.add(Node.objects.get(id='TJ1'))
    Node.objects.get(id='TJ1').neighbours.add(Node.objects.get(id='TJ2'))
    Node.objects.get(id='TJ2').neighbours.add(Node.objects.get(id='TJ1'))

    #     # insert_path(domestic, 'TJ2', 'TR29', 0, EAST)
    #     # insert_path(domestic, 'TJ2', 'TJ3', 100, NORTH)
    #     # insert_path(domestic, 'TJ3', 'TG10', 0, EAST)
    #     # insert_path(domestic, 'TJ3', 'TJ4', 100, NORTH)
    #     # insert_path(domestic, 'TJ4', 'TCAA', 0, WEST)
    #     # insert_path(domestic, 'TJ4', 'TJ5', 100, NORTH)
    #     # insert_path(domestic, 'TJ5', 'TG11', 0, EAST)
    #     # insert_path(domestic, 'TJ5', 'TJ6', 100, NORTH)
    #     # insert_path(domestic, 'TJ6', 'TF6', 0, EAST)
    #     # insert_path(domestic, 'TJ6', 'TJ7', 100, NORTH)
    #     # insert_path(domestic, 'TJ7', 'TG12', 0, EAST)
    #     # insert_path(domestic, 'TJ7', 'TR26', 0, WEST)
    #     # insert_path(domestic, 'TJ7', 'TF11', 0, WEST)
    #     # insert_path(domestic, 'TJ7', 'TJ8', 100, NORTH)
    #     # insert_path(domestic, 'TJ8', 'TF8', 0, EAST)
    #     # insert_path(domestic, 'TJ8', 'TR17X1', 0, EAST)
    #     # insert_path(domestic, 'TJ8', 'TJ9', 100, NORTH)
    #     # insert_path(domestic, 'TJ9', 'TG13', 0, EAST)
    #     # insert_path(domestic, 'TJ9', 'TJ10', 100, NORTH)
    #     # insert_path(domestic, 'TJ10', 'TG14', 0, EAST)
    #     # insert_path(domestic, 'TJ10', 'TG15', 100, NORTH)

    #     # insert_path(domestic, 'TN', 'TM', 100, SOUTH)
    #     # insert_path(domestic, 'TM', 'TS', 100, SOUTH)
    #     # insert_path(domestic, 'TXS', 'TS', 100, EAST)
    #     # insert_path(domestic, 'TXS', 'TR25X1', 0, NORTH)
    #     # insert_path(domestic, 'TXS', 'TR28', 0, NORTH)
    #     # insert_path(domestic, 'TS', 'TJ11', 100, SOUTH)
    #     # insert_path(domestic, 'TJ11', 'TG8', 0, EAST)
    #     # insert_path(domestic, 'TJ11', 'TR21', 0, WEST)
    #     # insert_path(domestic, 'TJ11', 'TR22', 0, WEST)
    #     # insert_path(domestic, 'TJ11', 'TJ12', 100, SOUTH)
    #     # insert_path(domestic, 'TJ12', 'TF7', 0, WEST)
    #     # insert_path(domestic, 'TJ12', 'TJ13', 100, SOUTH)
    #     # insert_path(domestic, 'TJ13', 'TG7', 0, EAST)
    #     # insert_path(domestic, 'TJ13', 'TJ14', 100, SOUTH)
    #     # insert_path(domestic, 'TJ14', 'TF1', 0, WEST)
    #     # insert_path(domestic, 'TJ14', 'TCD', 0, EAST)
    #     # insert_path(domestic, 'TJ14', 'TJ15', 100, SOUTH)
    #     # insert_path(domestic, 'TJ15', 'TF5', 0, WEST)
    #     # insert_path(domestic, 'TJ15', 'TF3', 0, EAST)
    #     # insert_path(domestic, 'TJ15', 'TJ16', 100, SOUTH)
    #     # insert_path(domestic, 'TJ16', 'TG6', 0, EAST)
    #     # insert_path(domestic, 'TJ16', 'TJ17', 100, SOUTH)
    #     # insert_path(domestic, 'TJ17', 'TR23', 0, WEST)
    #     # insert_path(domestic, 'TJ17', 'TJ18', 100, SOUTH)
    #     # insert_path(domestic, 'TJ18', 'TR27', 0, WEST)
    #     # insert_path(domestic, 'TJ18', 'TG5', 0, EAST)
    #     # insert_path(domestic, 'TJ18', 'TJ19', 100, SOUTH)
    #     # insert_path(domestic, 'TJ19', 'TR17X2', 0, WEST)
    #     # insert_path(domestic, 'TJ19', 'TJ20', 100, SOUTH)
    #     # insert_path(domestic, 'TJ19', 'TR20', 0, WEST)
    #     # insert_path(domestic, 'TJ20', 'TJ21', 100, SOUTH)
    #     # insert_path(domestic, 'TJ21', 'TG4', 0, EAST)
    #     # insert_path(domestic, 'TJ21', 'TJ22', 100, SOUTH)
    #     # insert_path(domestic, 'TJ22', 'TF9', 0, WEST)
    #     # insert_path(domestic, 'TJ22', 'TJ23', 100, SOUTH)
    #     # insert_path(domestic, 'TJ22', 'TF10', 0, WEST)
    #     # insert_path(domestic, 'TJ23', 'TJ24', 100, SOUTH)
    #     # insert_path(domestic, 'TJ22', 'TF4', 0, WEST)
    #     # insert_path(domestic, 'TJ24', 'TJ25', 100, SOUTH)
    #     # insert_path(domestic, 'TJ25', 'TG3', 0, EAST)
    #     # insert_path(domestic, 'TJ25', 'TR18', 0, WEST)
    #     # insert_path(domestic, 'TJ25', 'TJ26', 100, SOUTH)
    #     # insert_path(domestic, 'TJ26', 'TR25X2', 0, WEST)
    #     # insert_path(domestic, 'TJ26', 'TJ27', 100, SOUTH)
    #     # insert_path(domestic, 'TJ27', 'TG2', 0, EAST)
    print("testing neighbor")

def insert_all_nodes():
    # T Concourse Missing Nodes: Elevators and Escalators !!
    Node(id='TXN', name='T Concourse', type=EnumField.JOINT, floor=0).save()
    Node(id='TN', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR24', name='News Express', type=EnumField.RETAIL, floor=0).save()
    Node(id='TG9', name='Gate T9', type=EnumField.GATE, floor=0).save()
    Node(id='TSN', name='T Concourse', type=EnumField.JOINT, floor=0).save()
    Node(id='TJ1', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF12', name='Burger King', type=EnumField.FOOD, floor=0).save()
    Node(id='TR16', name='Travel Size Essentials', type=EnumField.RETAIL, floor=0).save()
    Node(id='TR19', name='BestBuy Zoom', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ2', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR29', name='Z Market', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ3', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG10', name='Gate T10', type=EnumField.GATE, floor=0).save()
    Node(id='TJ4', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TCAA', name='American Airlines Club', type=EnumField.CLUB, floor=0).save()
    Node(id='TJ5', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG11', name='Gate T11', type=EnumField.GATE, floor=0).save()
    Node(id='TJ6', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF6', name='Goldberg\'s Bagels', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ7', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG12', name='Gate T12', type=EnumField.GATE, floor=0).save()
    Node(id='TR26', name='Southern Flavors', type=EnumField.RETAIL, floor=0).save()
    Node(id='TF11', name='Vending Machines', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ8', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF8', name='Saucy Blues', type=EnumField.FOOD, floor=0).save()
    Node(id='TR17X1', name='Atlanta News and Gifts', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ9', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG13', name='Gate T13', type=EnumField.GATE, floor=0).save()
    Node(id='TJ10', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG14', name='Gate T14', type=EnumField.GATE, floor=0).save()
    Node(id='TG15', name='Gate T15', type=EnumField.GATE, floor=0).save()
    Node(id='TM', name='T Concourse', type=EnumField.JOINT, floor=0).save()
    Node(id='TXS', name='T Concourse', type=EnumField.JOINT, floor=0).save()
    Node(id='TS', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR25X1', name='Shellis News', type=EnumField.RETAIL, floor=0).save()
    Node(id='TR28', name='Tech Showcase', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ11', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG8', name='Gate T8', type=EnumField.GATE, floor=0).save()
    Node(id='TR21', name='Headphone Hub', type=EnumField.RETAIL, floor=0).save()
    Node(id='TR22', name='Inmotion Entertainment', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ12', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF7', name='Sam Adams / Checkpoint Bistro', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ13', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG7', name='Gate T7', type=EnumField.GATE, floor=0).save()
    Node(id='TJ14', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF1', name='Bojangles', type=EnumField.FOOD, floor=0).save()
    Node(id='TCD', name='Delta Sky Club', type=EnumField.CLUB, floor=0).save()
    Node(id='TJ15', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF5', name='Famous Famiglia', type=EnumField.FOOD, floor=0).save()
    Node(id='TF3', name='The Coffee Bean and Tea Leaf', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ16', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG6', name='Gate T6', type=EnumField.GATE, floor=0).save()
    Node(id='TJ17', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR23', name='Lather', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ18', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR27', name='Talie', type=EnumField.RETAIL, floor=0).save()
    Node(id='TG5', name='Gate T5', type=EnumField.GATE, floor=0).save()
    Node(id='TJ19', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR17X2', name='Atlanta News and Gifts', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ20', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR20', name='Brookstone', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ21', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG4', name='Gate T4', type=EnumField.GATE, floor=0).save()
    Node(id='TJ22', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF9', name='TJI Friday\'s', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ23', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF10', name='Jamba Juice', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ24', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TF4', name='Corner Bakery Cafe', type=EnumField.FOOD, floor=0).save()
    Node(id='TJ25', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG3', name='Gate T3', type=EnumField.GATE, floor=0).save()
    Node(id='TR18', name='B Iconic', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ26', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TR25X2', name='Shellis News', type=EnumField.RETAIL, floor=0).save()
    Node(id='TJ27', name='', type=EnumField.JOINT, floor=0).save()
    Node(id='TG2', name='Gate T2', type=EnumField.GATE, floor=0).save()
    Node(id='TG1', name='Gate T1', type=EnumField.GATE, floor=0).save()

#     # insert_path(domestic, 'TXN', 'TN', 100, EAST)
#     # insert_path(domestic, 'TN', 'TR24', 0, SOUTH)
#     # insert_path(domestic, 'TN', 'TG9', 0, EAST)
#     # insert_path(domestic, 'TN', 'TJ1', 100, NORTH)
#     # insert_path(domestic, 'TJ1', 'TF12', 0, EAST)
#     # insert_path(domestic, 'TJ1', 'TR16', 0, WEST)
#     # insert_path(domestic, 'TJ1', 'TR19', 0, WEST)
#     # insert_path(domestic, 'TJ1', 'TJ2', 100, NORTH)
#     # insert_path(domestic, 'TJ2', 'TR29', 0, EAST)
#     # insert_path(domestic, 'TJ2', 'TJ3', 100, NORTH)
#     # insert_path(domestic, 'TJ3', 'TG10', 0, EAST)
#     # insert_path(domestic, 'TJ3', 'TJ4', 100, NORTH)
#     # insert_path(domestic, 'TJ4', 'TCAA', 0, WEST)
#     # insert_path(domestic, 'TJ4', 'TJ5', 100, NORTH)
#     # insert_path(domestic, 'TJ5', 'TG11', 0, EAST)
#     # insert_path(domestic, 'TJ5', 'TJ6', 100, NORTH)
#     # insert_path(domestic, 'TJ6', 'TF6', 0, EAST)
#     # insert_path(domestic, 'TJ6', 'TJ7', 100, NORTH)
#     # insert_path(domestic, 'TJ7', 'TG12', 0, EAST)
#     # insert_path(domestic, 'TJ7', 'TR26', 0, WEST)
#     # insert_path(domestic, 'TJ7', 'TF11', 0, WEST)
#     # insert_path(domestic, 'TJ7', 'TJ8', 100, NORTH)
#     # insert_path(domestic, 'TJ8', 'TF8', 0, EAST)
#     # insert_path(domestic, 'TJ8', 'TR17X1', 0, EAST)
#     # insert_path(domestic, 'TJ8', 'TJ9', 100, NORTH)
#     # insert_path(domestic, 'TJ9', 'TG13', 0, EAST)
#     # insert_path(domestic, 'TJ9', 'TJ10', 100, NORTH)
#     # insert_path(domestic, 'TJ10', 'TG14', 0, EAST)
#     # insert_path(domestic, 'TJ10', 'TG15', 100, NORTH)

#     # insert_path(domestic, 'TN', 'TM', 100, SOUTH)
#     # insert_path(domestic, 'TM', 'TS', 100, SOUTH)
#     # insert_path(domestic, 'TXS', 'TS', 100, EAST)
#     # insert_path(domestic, 'TXS', 'TR25X1', 0, NORTH)
#     # insert_path(domestic, 'TXS', 'TR28', 0, NORTH)
#     # insert_path(domestic, 'TS', 'TJ11', 100, SOUTH)
#     # insert_path(domestic, 'TJ11', 'TG8', 0, EAST)
#     # insert_path(domestic, 'TJ11', 'TR21', 0, WEST)
#     # insert_path(domestic, 'TJ11', 'TR22', 0, WEST)
#     # insert_path(domestic, 'TJ11', 'TJ12', 100, SOUTH)
#     # insert_path(domestic, 'TJ12', 'TF7', 0, WEST)
#     # insert_path(domestic, 'TJ12', 'TJ13', 100, SOUTH)
#     # insert_path(domestic, 'TJ13', 'TG7', 0, EAST)
#     # insert_path(domestic, 'TJ13', 'TJ14', 100, SOUTH)
#     # insert_path(domestic, 'TJ14', 'TF1', 0, WEST)
#     # insert_path(domestic, 'TJ14', 'TCD', 0, EAST)
#     # insert_path(domestic, 'TJ14', 'TJ15', 100, SOUTH)
#     # insert_path(domestic, 'TJ15', 'TF5', 0, WEST)
#     # insert_path(domestic, 'TJ15', 'TF3', 0, EAST)
#     # insert_path(domestic, 'TJ15', 'TJ16', 100, SOUTH)
#     # insert_path(domestic, 'TJ16', 'TG6', 0, EAST)
#     # insert_path(domestic, 'TJ16', 'TJ17', 100, SOUTH)
#     # insert_path(domestic, 'TJ17', 'TR23', 0, WEST)
#     # insert_path(domestic, 'TJ17', 'TJ18', 100, SOUTH)
#     # insert_path(domestic, 'TJ18', 'TR27', 0, WEST)
#     # insert_path(domestic, 'TJ18', 'TG5', 0, EAST)
#     # insert_path(domestic, 'TJ18', 'TJ19', 100, SOUTH)
#     # insert_path(domestic, 'TJ19', 'TR17X2', 0, WEST)
#     # insert_path(domestic, 'TJ19', 'TJ20', 100, SOUTH)
#     # insert_path(domestic, 'TJ19', 'TR20', 0, WEST)
#     # insert_path(domestic, 'TJ20', 'TJ21', 100, SOUTH)
#     # insert_path(domestic, 'TJ21', 'TG4', 0, EAST)
#     # insert_path(domestic, 'TJ21', 'TJ22', 100, SOUTH)
#     # insert_path(domestic, 'TJ22', 'TF9', 0, WEST)
#     # insert_path(domestic, 'TJ22', 'TJ23', 100, SOUTH)
#     # insert_path(domestic, 'TJ22', 'TF10', 0, WEST)
#     # insert_path(domestic, 'TJ23', 'TJ24', 100, SOUTH)
#     # insert_path(domestic, 'TJ22', 'TF4', 0, WEST)
#     # insert_path(domestic, 'TJ24', 'TJ25', 100, SOUTH)
#     # insert_path(domestic, 'TJ25', 'TG3', 0, EAST)
#     # insert_path(domestic, 'TJ25', 'TR18', 0, WEST)
#     # insert_path(domestic, 'TJ25', 'TJ26', 100, SOUTH)
#     # insert_path(domestic, 'TJ26', 'TR25X2', 0, WEST)
#     # insert_path(domestic, 'TJ26', 'TJ27', 100, SOUTH)
#     # insert_path(domestic, 'TJ27', 'TG2', 0, EAST)
#     # # South East 'ahead on your right'
#     # insert_path(domestic, 'TJ27', 'TG1', 0, SOUTHEAST)


#     Node(id='DTXN1', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXN2', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXN3', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXN4', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXN5', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXN6', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS1', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS2', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS3', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS4', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS5', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXS6', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXW1', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXW2', name='', type=EnumField.EXIT, floor=0).save()
#     # domestic terminal exit marta north
#     Node(id='DTXMN', name='', type=EnumField.EXIT, floor=0).save()
#     Node(id='DTXMS', name='', type=EnumField.EXIT, floor=0).save()
#     # connecting paths
#     Node(id='DTJ1', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ2', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ3', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ4', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ5', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ6', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ7', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ8', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ9', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ10', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ11', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ12', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ13', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ14', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ15', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ16', name='', type=EnumField.JOINT, floor=0).save()
#     Node(id='DTJ17', name='', type=EnumField.JOINT, floor=0).save()
#     # security checkpoints
#     Node(id='DTSN', name='North Security', type=EnumField.SECURITY, floor=0).save()
#     Node(id='DTSM', name='Main Security', type=EnumField.SECURITY, floor=0).save()
#     Node(id='DTSS', name='South Security', type=EnumField.SECURITY, floor=0).save()

#     # insert_path(domestic, 'DTXN6', 'DTSN', 100, SOUTHEAST)
#     # insert_path(domestic, 'DTXN5', 'DTJ1', 100, SOUTH)
#     # insert_path(domestic, 'DTXN4', 'DTJ3', 100, SOUTHEAST)
#     # insert_path(domestic, 'DTXN3', 'DTJ4', 100, SOUTHEAST)
#     # insert_path(domestic, 'DTXN2', 'DTJ5', 100, SOUTH)
#     # insert_path(domestic, 'DTXN1', 'DTJ5', 100, SOUTHEAST)
#     # insert_path(domestic, 'DTJ1', 'DTSN', 100, EAST)
#     # insert_path(domestic, 'DTJ2', 'DTJ1', 100, EAST)
#     # insert_path(domestic, 'DTJ3', 'DTJ2', 100, EAST)
#     # insert_path(domestic, 'DTJ4', 'DTJ3', 100, EAST)
#     # insert_path(domestic, 'DTJ5', 'DTJ4', 100, EAST)
#     # insert_path(domestic, 'DTJ6', 'DTJ5', 100, EAST)
#     # insert_path(domestic, 'DTXW1', 'DTJ6', 100, EAST)
#     # insert_path(domestic, 'DTJ6', 'DTXMN', 100, SOUTH)
#     # insert_path(domestic, 'DTJ7', 'DTSM', -1, WEST)
#     # insert_path(domestic, 'DTSM', 'DTJ8', 100, WEST)
#     # insert_path(domestic, 'DTJ8', 'DTJ9', 100, WEST)
#     # insert_path(domestic, 'DTJ9', 'DTJ10', 100, WEST)
#     # insert_path(domestic, 'DTJ10', 'DTJ11', 100, WEST)
#     # insert_path(domestic, 'DTJ2', 'DTJ8', 100, SOUTH)
#     # insert_path(domestic, 'DTJ3', 'DTJ9', 100, SOUTHEAST)
#     # insert_path(domestic, 'DTJ4', 'DTJ10', 100, SOUTH)
#     # insert_path(domestic, 'DTJ5', 'DTJ11', 100, SOUTH)
#     # insert_path(domestic, 'DTJ8', 'DTJ13', 100, SOUTH)
#     # insert_path(domestic, 'DTJ9', 'DTJ14', 100, SOUTHWEST)
#     # insert_path(domestic, 'DTJ10', 'DTJ15', 100, SOUTH)
#     # insert_path(domestic, 'DTJ11', 'DTJ16', 100, SOUTH)

#     # insert_path(domestic, 'DTJ12', 'DTSS', 100, EAST)
#     # insert_path(domestic, 'DTJ13', 'DTJ12', 100, EAST)
#     # insert_path(domestic, 'DTJ14', 'DTJ13', 100, EAST)
#     # insert_path(domestic, 'DTJ15', 'DTJ14', 100, EAST)
#     # insert_path(domestic, 'DTJ16', 'DTJ15', 100, EAST)
#     # insert_path(domestic, 'DTJ17', 'DTJ16', 100, EAST)
#     # insert_path(domestic, 'DTJ17', 'DTXMS', 100, NORTH)
#     # insert_path(domestic, 'DTXW2', 'DTJ17', 100, EAST)

#     # insert_path(domestic, 'DTXS1', 'DTJ12', 100, NORTH)
#     # insert_path(domestic, 'DTXS2', 'DTJ13', 100, NORTH)
#     # insert_path(domestic, 'DTXS3', 'DTJ14', 100, NORTH)
#     # insert_path(domestic, 'DTXS4', 'DTJ15', 100, NORTH)
#     # insert_path(domestic, 'DTXS5', 'DTJ15', 100, NORTHEAST)
#     # insert_path(domestic, 'DTXS6', 'DTJ16', 100, NORTHEAST)

#     # # connect domestic terminal to t concourse
#     # insert_path(domestic, 'DTSN', 'TXN', 0, EAST, Path.SECURITY)
#     # insert_path(domestic, 'DTSS', 'TXS', 0, EAST, Path.SECURITY)
