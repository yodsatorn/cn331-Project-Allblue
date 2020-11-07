from django.urls import path
from . import views

urlpatterns = [
	path('addrecipe/', views.addrecipe_view, name = 'addrecipe'),
]