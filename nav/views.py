from django.http import HttpResponse
# from nav.models import Test
from nav.models import Node, EnumField

# def test(request):
#     tests = Test.objects.filter(name='bill')
#     for test in tests:
#         print(test.get_name())
#     return HttpResponse("")


from django.http import HttpResponse


def test(request):
    test_node = Node(name='test', id='33434', floor=1, type=EnumField.JOINT)
    test_node.save()
    print(1)
    print(test_node.name)
    # tests = Node.objects.all()
    # for test in tests:
    #     print(test.name)
    return HttpResponse("")

