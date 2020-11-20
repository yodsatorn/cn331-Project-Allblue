from django.urls import include
from django.urls import path
from . import views
urlpatterns = [
    path('recipes/',include('recipes.urls')),
    path('voteup/<int:recipe_id>/<int:id>', views.voteUp, name='voteup_comment'),
    path('votedown/<int:recipe_id>/<int:id>', views.voteDown, name='votedown_comment'),
    ]