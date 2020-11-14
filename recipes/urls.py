from django.urls import path
from . import views

urlpatterns = [
	path('addrecipe/', views.addrecipe_view, name = 'addrecipe'),
	path('view/recipe/<int:id>/', views.recipe_view, name='recipe_view')
]