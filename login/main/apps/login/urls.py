from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('home', views.home),
		path('logout', views.logout)
	]