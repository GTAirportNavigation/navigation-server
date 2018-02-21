from django.shortcuts import loader
from django.http import HttpResponse
from nav import airport_graph, testing

# Create your views here.
def default(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def flight_track(request):
    args = (str(request)[20:-2]).split('/')
    print(args[2])
    directions = []
    if (args[2] == 'DL1'):
        directions = airport_graph.condense(airport_graph.translate(testing.domestic, airport_graph.find_path(testing.domestic, 'DTXN1', 'TG12')))
    elif (args[2] == 'DL2'):
        directions = airport_graph.condense(airport_graph.translate(testing.domestic, airport_graph.find_path(testing.domestic, 'DTXN1', 'TG3')))
    c = {'directions': directions}
    template = loader.get_template('directions.html')
    print('got template')
    return HttpResponse(template.render(c))

def demo_js(request):
    file = open('static/demo.js')
    js = file.read()
    file.close()
    return HttpResponse(js)
