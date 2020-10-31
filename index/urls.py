from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "index"),
	path('about/', views.about, name = "about"),
	path('menu2/', views.menu2, name = "menu2"),
	path('menu3/', views.menu3, name = "menu3"),
	path('login/', views.view_login, name="login"),
	path('register/', views.register, name="register"),
]
