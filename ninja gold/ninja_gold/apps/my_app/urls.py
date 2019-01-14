from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('get_gold', views.get_gold),
        path('restart', views.restart_game)
	]