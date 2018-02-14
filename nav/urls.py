from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.default, name=''),
    re_path('route/.*/', views.route, name='')
]