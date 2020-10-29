from django.shortcuts import render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

#add recipe
def addRecipe(request,id):
    if request.method == "POST":
        name=request.POST["recipes Name : "]
        igd = request.POST["ingredient :"]
        sol = request.POST["solutions :"]
        r = Recipes(reName=name,ingredient=igd,solution=sol)
        r.save()
    return render( )