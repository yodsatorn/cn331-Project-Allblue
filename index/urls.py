from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "index"),
	path('about/', views.about, name = "about"),
<<<<<<< HEAD
	path('menu/', views.menu, name = "menu"),
=======
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
>>>>>>> 0d608291f289244f4f26b1c6455311bf44b8da32
]
