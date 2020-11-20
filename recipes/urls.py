from recipes.views import add_comment
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('menu/', views.menu_view, name = "menu"),
	path('addrecipe/', views.addrecipe_view, name = 'addrecipe'),
	path('view/recipe/<int:id>/', views.recipe_view, name='recipe_view'),
	path('view/recipe/voteup/<int:recipe_id>', views.voteUp ,name='voteup'),
	path('view/recipe/votedown/<int:recipe_id>', views.voteDown ,name='votedown'),
	path('addcomment/<int:recipe_id>', views.add_comment, name="addcomment")
]
