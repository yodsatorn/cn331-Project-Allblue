from django.http import request
from django.shortcuts import redirect, render
from recipes.models import Recipes, Tags
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeForm
from drive.main import uploadFile
from comments.models import Comments


# view_menu
def menu_view(request):
    tag = Tags.objects.all()
    if (request.method == 'GET'):
        result = Recipes.objects.all()
        return render(request, "menu.html", {
            'menu': result,
            'tags': tag
        })
    if (request.method == 'POST'):
        data = request.POST.get('q')
        option = request.POST.get('search_option')
        sort = request.POST.get('sort_option')
        
        if (sort == 'asc'):
            if (option == 'by_name'):
                result = Recipes.objects.filter(reName__icontains=data).order_by('id')
        elif (sort == 'des'):
            if (option == 'by_name'):
                result = Recipes.objects.filter(reName__icontains=data).order_by('id').reverse()

        return render(request, "menu.html", {
            'menu': result,
            'tags': tag
        })


# Add recipe fearture : this fucntion will add recipe that user create into data base.
def addrecipe_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            try:
                name = request.FILES['image'].name
                imageUrl = '.' + f.image.url
                imageID = uploadFile(name, imageUrl)
                f.image = imageID
                f.save()
            except KeyError:
                f.save()
            form = RecipeForm()
            return redirect('myrecipe', request.user.id)
    else:
        form = RecipeForm(initial={'user': [request.user]})
        return render(request, 'addrecipe.html', {'form': form})


sortRenameCount = 0
sortTimeCount = 0


# This fucntion will show detail of each recipe.
def recipe_view(request, id):
    return render(request, 'viewrecipe.html', {
        'result': Recipes.objects.get(id=id),
        'user': Recipes.objects.get(id=id).user.get(userRecipe=id),
        'tag': Recipes.objects.get(id=id).tag.all(),
        'solution': [x for x in Recipes.objects.get(id=id).solution.split("\n")],
        'ingredient': [x for x in Recipes.objects.get(id=id).ingredient.split("\n")],
        'comments': Comments.objects.filter(recipeID=id),
    })


# This fucntion will delete recipe in data base.
def deleteRecipe(request, recipe_id):
    if request.method == "GET":
        r = Recipes.objects.get(pk=recipe_id)
        r.delete()
    return redirect('myrecipe', request.user.id)


# voteUp feature
# If user press vote up button this fucntion will vote up recipes.
def voteUp_recipe(request, recipe_id):
    if request.user.is_authenticated :
        recipe = Recipes.objects.get(pk=recipe_id)
        user = User.objects.get(id=request.user.id)
        if recipe.voteUp.filter(id=request.user.id).count() == 0:
            if recipe.voteDown.filter(id=request.user.id).count() == 0:
                recipe.voteUp.add(user)
            else:
                recipe.voteDown.remove(user)
                recipe.voteUp.add(user)
        else:
            recipe.voteUp.remove(user)
        return redirect('recipe_view', recipe_id)
    else :
        return redirect('login')


# voteDown feature
# If user press vote down button this fucntion will vote down recipes.
def voteDown_recipe(request, recipe_id):
    if request.user.is_authenticated :
        recipe = Recipes.objects.get(pk=recipe_id)
        user = User.objects.get(id=request.user.id)
        if recipe.voteDown.filter(id=request.user.id).count() == 0:
            if recipe.voteUp.filter(id=request.user.id).count() == 0:
                recipe.voteDown.add(user)
            else:
                recipe.voteUp.remove(user)
                recipe.voteDown.add(user)
        else:
            recipe.voteDown.remove(user)
        return redirect('recipe_view', recipe_id)
    else:
        return redirect('login')

# This fucntion will add comment that writen by user.
def add_comment(request, recipe_id):
    if request.user.is_authenticated :
        if request.method == "GET":
            body = request.GET.get('body')
            recipe = Recipes.objects.get(id=recipe_id)
            user = User.objects.get(id=request.user.id)
            c = Comments.objects.create(body=body, username=request.user.username)
            c.userID.add(user)
            c.recipeID.add(recipe)
        return redirect('recipe_view', recipe_id)
    else :
        return redirect('login')


# This function will show recipe's user.
def view_my_recipes(request, user_id):
    return render(request, 'my_recipes.html', {
        'my_recipes': Recipes.objects.filter(user__id=user_id)
    })


# This fucntion will show recipe by tag's name
def tag_show_recipes(request,tag_id):
    if request.method == 'GET':
        tag = Tags.objects.all()
        recipe = Recipes.objects.filter(tag__id = tag_id)
        return render(request, 'menu.html', {
            'menu' : recipe,
            'tags' : tag
        })