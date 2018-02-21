from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.default, name=''),
    re_path('flight/.*', views.flight_track, name=''),
    path('demo.js', views.demo_js, name=''),
]