from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.default),
	path('refresh', views.refresh),
	re_path('route/.*', views.route),
	re_path('flight/.*', views.flight),
	re_path('r/.*', views.shop),
	re_path('e/.*', views.shop),
	re_path('detail/.*', views.detail),
]
