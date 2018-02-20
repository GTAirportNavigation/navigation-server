from django.http import HttpResponse
from . import airport_graph, testing

def default(request):
    return HttpResponse('')

def route(request):
    args = (str(request)[20:-2]).split('/')
    print(args)
    end = args[2].upper()
    start = ''
    if args[3] == '':
        start = 'DTJ10'
    else:
        start = args[3].upper()
    instructions = airport_graph.condense(airport_graph.translate(testing.domestic, airport_graph.find_path(testing.domestic, start, end)))
    json = airport_graph.convert_to_json(instructions)
    return HttpResponse(json)
