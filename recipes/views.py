from django.http import request
from django.shortcuts import render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeForm

def addrecipe_view(request):
    if request.method == "POST" :
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            form = RecipeForm()
            return render(request, 'addrecipe.html', {'form' : form})
    else:
        form = RecipeForm(initial={'user': [request.user] })

    return render(request, 'addrecipe.html', {'form' : form})

def deleteRecipe(request ,recipe_id):
    if request.method == "POST":
        r = Recipes.objects.get(pk = recipe_id)
        r.delete()
        
    return render( )