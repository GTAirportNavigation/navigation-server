from django.http import HttpResponse
from . import graph, utils, testing

def default(request):
	return HttpResponse('GT Airport Navigation')

def refresh(request):
	# return HttpResponse(str(graph.nodes))
	return HttpResponse('Graph Refreshed')

def route(request):
	response = ''
	args = str(request)[20:-2].split('/')
	if len(args) == 3:
		src = args[1]
		dst = args[2]
		response = str(graph.path(src, dst))

	return HttpResponse(response)

def flight(request):
	response = ''
	args = str(request)[20:-2].split('/')
	if len(args) == 2:
		f = args[1]
		gate = utils.get_gate(f)
		response = '[\"' + (gate[0] + 'G' + gate[0][1:]) + '\", ' + str(gate[1]) + ']'

	return HttpResponse(response)

def shop(request):
	filt = ''
	response = ''
	shop_list = []
	args = str(request)[20:-2].split('/')
	if len(args) < 3:
		if len(args) == 2:
			filt = args[1]
		if args[0] == 'f':
			shop_list = graph.get_food(filt)
		elif args[0] == 'r':
			shop_list = graph.get_retail(filt)
		response = str(shop_list)

	return HttpResponse(response)

def detail(request):
	response = ''
	args = str(request)[20:-2].split('/')
	if len(args) == 2:
		loc = args[1]
		# response = utils.get_detail(loc)

	return HttpResponse(response)
