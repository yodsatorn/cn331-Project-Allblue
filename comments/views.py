from django.http import request
from django.shortcuts import render
from comments.models import Comments
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipes
# Create your views here.

sortRenameCount = 0
sortTimeCount = 0

def addcomments_view(request, recipes_id):
    if request.method == "POST" :
        r = Recipes.objects.get(pk = recipes_id)
        comments = Comments.objects.get(recipeID = r )
        c = request.POST["comment"]
        comment = Comments(body=c)
        comment.save()

        return render(request, '.html', {'comment' : comment})

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

def comment_list(request):
    comment = Comment.objects.all()
    return render(request, '.html', {
        'comment': comment
    })