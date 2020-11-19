from django.http import request
from django.shortcuts import render
from comments.models import Comments
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipes
from django.shortcuts import redirect
# Create your views here.

# This fucntion will add comment that writen by user. 
def addcomments(request, recipes_id):
    if request.method == "POST" :
        user = User.objects.get(id = request.user.id)
        recipe = Recipes.objects.get(pk = recipes_id)
        body = request.POST['body']
        comment = Comments.objects.create(body = body) 
        comment.userID.add(user)       
        comment.recipeID.add(recipe)
        return redirect('recipe_view',recipes_id)

#Vote up comment
def voteUp(request, recipes_id ):
    if request.method == "POST":
        comments = Comments.objects.get(recipeID = recipes_id )
        user = User.objects.get(user_id=request.user.id)
        if comments.voteUp.filter(user_id=request.user.id).count()==0:
            if comments.voteDown.filter(user_id=request.user.id).count()==0:
                comments.voteUp.add(user)
            else :
                comments.voteDown.remove(user)
                comments.voteUp.add(user)
        else:
            comments.voteUp.remove(user)
    return render()

# Vote down comment fucntion
def voteDown(request, recipes_id):
    if request.method == "POST":
        comments = Comments.objects.get( recipeID = recipes_id )
        user = User.objects.get(user_id=request.user.id)
        if comments.voteDown.filter(user_id=request.user.id).count()==0:
            if comments.voteUp.filter(user_id=request.user.id).count()==0:
                comments.voteDown.add(user)
            else :
                comments.voteUp.remove(user)
                comments.voteDown.add(user)
        else:
            comments.voteDown.remove(user)
    return render()

# This fucntion will show all of comments in the recipe.
def comment_list(request,recipe_ID):
    comment = Comments.objects.filter(recipeID = recipe_ID)
    return render(request, '.html', {
        'comment': comment
    }) # Nice said it's up to you ,you can return what u want