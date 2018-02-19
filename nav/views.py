from django.http import HttpResponse
from . import airport_graph, testing

def default(request):
    return HttpResponse('')

def route_gate(request):
    gate = str(request)[29:][:-3]
    instructions = airport_graph.condense(airport_graph.translate(testing.domestic, airport_graph.find_path(testing.domestic, 'TNenter', gate.upper())))
    json = airport_graph.convert_to_json(instructions)
    return HttpResponse(json)
    # return HttpResponse('')

def route(request):
    flightno = str(request)[30:][:-3]
    if flightno == 'test':
        gate = 'TG2'
        instructions = airport_graph.condense(airport_graph.translate(testing.domestic, airport_graph.find_path(testing.domestic, 'DTXN1', gate)))
        json = airport_graph.convert_to_json(instructions)
        return HttpResponse(json)
    else:
        return HttpResponse('')
