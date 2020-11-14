from django.urls import path
from django.urls.base import reverse
from django.urls import include
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about/', views.about, name = "about"),
	path('menu/', views.menu, name = "menu"),
	path('login/', views.view_login, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.view_logout, name='logout'),
	path('profile/', views.profile, name='profile'),
	path('menu/search/', views.search, name='search'),
	path('profile/edit/', views.editProfile, name='editProfile'),
	path('recipes/',include('recipes.urls'))
]
