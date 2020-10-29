from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "index"),
	path('about/', views.about, name = "about"),
<<<<<<< HEAD
	path('login/', views.login, name = "login"),
	path('register/', views.register, name = "register"),
=======
	path('menu/', views.menu, name = "menu"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
>>>>>>> 78045d4c8d7dbd287d6a57737f61d59cd29b3d03
]
