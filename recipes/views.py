from django.shortcuts import render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

sortRenameCount = 0
sortTimeCount = 0
#add recipe
def addRecipe(request):
    if request.method == "POST":
        name= request.POST["recipes_Name"]
        igd = request.POST["ingredient"]
        sol = request.POST["solutions"]
        r = Recipes(reName=name,ingredient=igd,solution=sol)
        r.user.add(User.objects.get(id=request.user.id))
        
    return render(request, )

def deleteRecipe(request ,recipe_id):
    if request.method == "POST":
        r = Recipes.objects.get(pk = recipe_id)
        r.delete()
    return render(request  )

#voteUp feature
def voteUp(request,recipe_id):
    if request.method == "POST":
        recipe = Recipes.objects.get(pk = recipe_id)
        user = User.objects.get(user_id=request.user.id)
        if recipe.voteUp.filter(user_id=request.user.id).count()==0:
            if recipe.voteDown.filter(user_id=request.user.id).count()==0:
                recipe.voteUp.add(user)
            else :
                recipe.voteDown.remove(user)
                recipe.voteUp.add(user)
        else:
            recipe.voteUp.remove(user)
    return render() #I don't know what to do, it's up to you boi

#voteDown feature
def voteDown(request,recipe_id):
    if request.method == "POST":
        recipe = Recipes.objects.get(pk = recipe_id)
        user = User.objects.get(user_id=request.user.id)
        if recipe.voteDown.filter(user_id=request.user.id).count()==0:
            if recipe.voteUp.filter(user_id=request.user.id).count()==0:
                recipe.voteDown.add(user)
            else :
                recipe.voteUp.remove(user)
                recipe.voteDown.add(user)
        else:
            recipe.voteDown.remove(user)
    return render() #I don't know what to do, it's up to you boi

#sort by reName
def sortByReName(request):
    if request.method == "POST":
        sortRenameCount+=1
        sortRenameCount %= 2
        #sort Recipes by reName desc
        if(sortRenameCount == 1):
            return Recipes.objects.order_by('reName') #you can add render more cause i don't know what to do.
        #sort Recipes by reName incr
        else:
            return Recipes.objects.order_by('reName').reverse() #you can add render more cause i don't know what to do.

def sortByTime(request):
    if request.method == "POST":
        sortTimeCount +=1
        sortTimeCount %= 2
        #sort Recipes by Time desc
        if(sortTimeCount == 1):
            return  Recipes.objects.order_by('id') #you can add render more cause i don't know what to do.
        #sort Recipes by Time incr
        else:
            return Recipes.objects.order_by('id').reverse() #you can add render more cause i don't know what to do.