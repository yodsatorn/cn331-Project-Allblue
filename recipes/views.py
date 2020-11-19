from django.http import request
from django.shortcuts import redirect, render
from recipes.models import Recipes,Tags
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeForm

# view_menu
def menu_view(request):
	if (request.method == 'GET') :
		result = Recipes.objects.all()
		return  render(request, "menu.html", {
			'menu': result
		})
	else :
		data = request.POST.get('q')
		option = request.POST.get('search_option')

		if (option == 'by_name') :
			result = Recipes.objects.filter(reName__icontains = data)

		return render(request, "menu.html", {
			'menu': result
		})

# Add recipe fearture : this fucntion will add recipe that user create into data base.
def addrecipe_view(request):
    if request.method == "POST" :
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RecipeForm()
            return render(request, 'addrecipe.html', {'form' : form})
    else:
        form = RecipeForm(initial={'user': [request.user] })

    return render(request, 'addrecipe.html', {'form' : form})

sortRenameCount = 0
sortTimeCount = 0

# This fucntion will show detail of the recipe.
def recipe_view(request, id):
    return render(request, 'viewrecipe.html', {
        'result': Recipes.objects.get(id=id),
        'user': Recipes.objects.get(id=id).user.get(userRecipe = id),
        'solution': [x for x in Recipes.objects.get(id= id).solution.split("\n")],
        'ingredient': [x for x in Recipes.objects.get(id= id).ingredient.split("\n")]
        })

#This fucntion will delete recipe in data base.
def deleteRecipe(request ,recipe_id):
    if request.method == "POST":
        r = Recipes.objects.get(pk = recipe_id)
        r.delete()
    return render(request  )

# voteUp feature
# If user press vote up button this fucntion will vote up recipes.
def voteUp(request, recipe_id):
    recipe = Recipes.objects.get(pk = recipe_id)
    user = User.objects.get(id=request.user.id)
    if recipe.voteUp.filter(id=request.user.id).count() == 0:
        if recipe.voteDown.filter(id=request.user.id).count() == 0:
            recipe.voteUp.add(user)
        else :
            recipe.voteDown.remove(user)
            recipe.voteUp.add(user)
    else:
        recipe.voteUp.remove(user)
    return redirect('recipe_view', recipe_id)

# voteDown feature
# If user press vote down button this fucntion will vote down recipes.
def voteDown(request, recipe_id):
    recipe = Recipes.objects.get(pk = recipe_id)
    user = User.objects.get(id=request.user.id)
    if recipe.voteDown.filter(id=request.user.id).count() == 0:
        if recipe.voteUp.filter(id=request.user.id).count() == 0:
            recipe.voteDown.add(user)
        else :
            recipe.voteUp.remove(user)
            recipe.voteDown.add(user)
    else:
        recipe.voteDown.remove(user)
    return redirect('recipe_view', recipe_id) #I don't know what to do, it's up to you boi

#This fucntion will sorting recipes by Recipe's Name.
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

#This fucntion will sorting recipes  by time that recipe was created.
def sortByTime(request):
    if request.method == "POST":
        sortTimeCount += 1
        sortTimeCount %= 2
        #sort Recipes by Time desc
        if(sortTimeCount == 1):
            return  Recipes.objects.order_by('id') #you can add render more cause i don't know what to do.
        #sort Recipes by Time incr
        else:
            return Recipes.objects.order_by('id').reverse() #you can add render more cause i don't know what to do.

#This fucntion will list recipes.
def recipes_list(request):
    recipes = Recipes.objects.all()
    return render(request, 'AddRecipe.html', {
        'recipes': recipes
    })
