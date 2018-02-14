# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.test, name='views.test')
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='views.test')
]