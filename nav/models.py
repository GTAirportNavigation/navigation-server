from django.db import models

class EnumField(models.Field):
	def __init__(self, *args, **kwargs):
		super(EnumField, self).__init__(*args, **kwargs)
		if not self.choices:
			raise AttributeError('EnumField requires *choices* attribute.')
	def db_type(self):
		return "enum(%s)" % ','.join("'%s'" % k for (k, _) in self.choices)

	NORMAL = 0
	STAIRS = 1
	ESCALATOR = 2
	ELEVATOR = 3
	TRAIN = 4
	SECURITY = 9

	PATH_CHOICES = (
		(NORMAL, 'Normal'),
		(STAIRS, 'Stair'),
		(ELEVATOR, 'Elevator'),
		(TRAIN, 'Train'),
		(SECURITY, 'Security')
	)

	NORTH = 0
	NORTHEAST = 45
	EAST = 90
	SOUTHEAST = 135
	SOUTH = 180
	SOUTHWEST = 225
	WEST = 270
	NORTHWEST = 315

	DIRECTIONS_CHOICES = (
		(NORTH, 'North'),
		(NORTHEAST, 'Northeast'),
		(EAST, 'East'),
		(SOUTHEAST, 'Southeast'),
		(SOUTH, 'South'),
		(SOUTHWEST, 'Southwest'),
		(WEST, 'West'),
		(NORTHWEST, 'Northwest'),
	)

	JOINT = 0
	SECURITY = 1
	GATE = 2
	COUNTER = 3
	FOOD = 4
	RETAIL = 5
	CLUB = 7
	EXIT = 9

	TYPE_CHOICES = (
		(JOINT, 'Joint'),
		(SECURITY, 'Security'),
		(GATE, 'Gate'),
		(COUNTER, 'Counter'),
		(FOOD, 'Food'),
		(RETAIL, 'Retail'),
		(CLUB, 'Club'),
		(EXIT, 'Exit'),
	)

class Node(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	name = models.CharField(max_length=50, blank=True)
	type = models.IntegerField(EnumField.TYPE_CHOICES)
	floor = models.IntegerField(default=0)

	class Meta:
		db_table ='Node'

class Neighbor(models.Model):
	from_node = models.ForeignKey(Node, related_name='from_node', on_delete=models.CASCADE)
	to_node = models.ForeignKey(Node, related_name='to_node', on_delete=models.CASCADE)
	distance = models.IntegerField(default=0)
	angle = models.IntegerField(default=0)
	type = models.IntegerField(EnumField.PATH_CHOICES)

	class Meta:
		db_table='Neighbor'
