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
