from django.shortcuts import render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

#add recipe
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