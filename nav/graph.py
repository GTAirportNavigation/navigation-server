from . import models

nodes = []
paths = []

def refresh():
	global nodes
	global paths

	# clear existing data
	nodes = []
	paths = []

	# import nodes
	all_nodes = models.Node.objects.all()
	for n in all_nodes:
		nodes.append(n)

	# import paths
	all_paths = models.Neighbor.objects.all()
	for p in all_paths:
		paths.append(p)

def get_neighbors(id):
	n = []
	for path in paths:
		if (path.to_node_id.lower() == id.lower()):
			n.append(path.from_node_id)
		elif (path.from_node_id.lower() == id.lower()):
			n.append(path.to_node_id)
	# print(n)
	return n

def get_neighbors_indices(id):
	neighbors = get_neighbors(id)

	for x in range(len(neighbors)):
		neighbors[x] = get_index_from_id(neighbors[x])

	return neighbors

def get_index_from_id(id):
	for i in range(len(nodes)):
		# print(nodes[i].id, ' ', id)
		if nodes[i].id.lower() == id.lower():
			# print('INDEX: ' + str(i))
			return i

def get_id_from_index(index):
	return nodes[index].id

def edge(aid, bid):
	for path in paths:
		if (path.to_node_id.lower() == aid.lower() and path.from_node_id.lower() == bid.lower()):
			return [path.from_node_id.lower(), path.distance, path.angle, path.type]
		elif (path.from_node_id.lower() == aid.lower() and path.to_node_id.lower() == bid.lower()):
			return [path.to_node_id.lower(), path.distance, path.angle, path.type]

# in this function we allow filtering to limit
# results by a given filter - in this case concourses
# therefore, just pass in to filter the desired concourse
# could be 'A' or 'T' for example, more complex filters could
# of course be added of these systems later
def get_type(type, filter):
	shops = []

	print('filter: ' + filter)
	hasfilter = not (filter == '')
	for node in nodes:
		if (node.type == type):
			if hasfilter:
				neighbors = get_neighbors(node.id)
				for n in neighbors:
					if (n[0].lower() == filter.lower()):
						shops.append([node.id, node.name])
						break
			else:
				shops.append([node.id, node.name])
	return shops

def get_food(filter):
	return get_type(models.EnumField.FOOD, filter)

def get_retail(filter):
	return get_type(models.EnumField.RETAIL, filter)

def trim(route):
	x = 0

	while x != (len(route) - 1):
		if (route[x][2] == route[x + 1][2] and route[x][3] == route[x + 1][3]):
			new_id = route[x + 1][0]
			new_dist = route[x][1] + route[x + 1][1]
			new_angle = route[x][2]
			new_type = route[x][3]
			route.pop(0)
			route.pop(0)
			route.insert(0, [new_id, new_dist, new_angle, new_type])
		else:
			x += 1

	return route

def path(sid, eid):
	node_list = find_path(sid, eid)

	node_ids = []
	for node in node_list:
		node_ids.append(get_id_from_index(node))

	route = []
	for x in range(len(node_ids) - 1):
		aid = node_ids[x]
		bid = node_ids[x + 1]
		route.append(edge(aid, bid))

	return trim(route)

def find_path(sid, eid, constraint=0):
	sindex = get_index_from_id(sid)
	frontier = []
	frontier.append(sindex)
	visited = []
	visited.append(sindex)
	route = [[]]

	while len(frontier) != 0:
		cindex = frontier.pop(0)
		croute = route.pop(0)
		cid = get_id_from_index(cindex)
		if cid.lower() == eid.lower():
			return (croute + [cindex])
		else:
			for nindex in get_neighbors(cid):
				if nindex not in visited:
					frontier.append(nindex)
					route.append(croute + [cindex])
					visited.append(nindex)
