from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('word_add', views.process)
	]