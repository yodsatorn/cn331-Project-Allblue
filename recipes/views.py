from django.http import request
from django.shortcuts import render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import AddRecipe

def addrecipe_view(request):
    if request.method == "POST" :
        form = AddRecipe(request.POST)
        if form.is_valid():
                name = form.cleaned_data['recipeName']
                igd = form.cleaned_data['ingredient']
                sol = request.POST["solutions"]
                r = Recipes(reName=name,ingredient=igd,solution=sol)
                r.save()
                r.user.add(User.objects.get(id=request.user.id))
                return HttpResponseRedirect('')
    else :
        form = AddRecipe()

    return render(request, 'AddRecipe.html', {'form': form})

# add recipe
def addRecipe(request):
    if request.method == "POST":
        name= request.POST["recipes_Name"]
        igd = request.POST["ingredient"]
        sol = request.POST["solutions"]
        r = Recipes(reName=name,ingredient=igd,solution=sol)
        r.save()
        r.user.add(User.objects.get(id=request.user.id))
        
    return render( )

def deleteRecipe(request ,recipe_id):
    if request.method == "POST":
        r = Recipes.objects.get(pk = recipe_id)
        r.delete()
        
    return render( )