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
		response = str(graph.find_path(src, dst))

	return HttpResponse(response)

def flight(request):
	response = ''
	args = str(request)[20:-2].split('/')
	if len(args) == 2:
		f = args[1]
		gate = utils.get_gate(f)
		response = '[\'' + (gate[0] + 'G' + gate[1:]) + '\']'

	return HttpResponse(response)

def shop(request):
	response = ''
	shop_list = []
	args = str(request)[20:-2].split('/')
	if len(args) == 2:
		filt = args[1]
		if args[0] == 'r':
			pass
			# shop_list = utils.get_shops(filt, False)
		elif args[0] == 's':
			pass
			# shop_list = utils.get_shops(filt, True)
		response = str(shop_list)

	return HttpResponse(response)

def detail(request):
	response = ''
	args = str(request)[20:-2].split('/')
	if len(args) == 2:
		loc = args[1]
		# response = utils.get_detail(loc)

	return HttpResponse(response)
