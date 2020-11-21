from django.http import request
from django.shortcuts import render
from comments.models import Comments
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipes
from django.shortcuts import redirect
# Create your views here.



# Vote up comment
def voteUp(request, recipe_id, id):
    comments = Comments.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    if comments.voteUp.filter(id=request.user.id).count() == 0:
        if comments.voteDown.filter(id=request.user.id).count() == 0:
            comments.voteUp.add(user)
        else:
            comments.voteDown.remove(user)
            comments.voteUp.add(user)
    else:
        comments.voteUp.remove(user)
    return redirect('recipe_view', recipe_id)


# Vote down comment
def voteDown(request, recipe_id, id):
    comments = Comments.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    if comments.voteDown.filter(id=request.user.id).count() == 0:
        if comments.voteUp.filter(id=request.user.id).count() == 0:
            comments.voteDown.add(user)
        else:
            comments.voteUp.remove(user)
            comments.voteDown.add(user)
    else:
        comments.voteDown.remove(user)
    return redirect('recipe_view', recipe_id)
