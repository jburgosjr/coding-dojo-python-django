from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('users', views.users),
        path('show/<id>', views.show),
        path('delete/<id>', views.delete),
        path('users/<id>/edit', views.edit),
        path('users/<id>', views.update),
        path('users/new/add', views.add),
        path('process', views.process)
	]