from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipes

# Create your models here.

class Comments(models.Model):
    
    userID = models.ManyToManyField(User, related_name = 'user')
    recipeID = models.ManyToManyField(Recipes)
    body = models.TextField()
    voteUp= models.ManyToManyField(User, related_name = 'commentVoteUp')
    voteDown = models.ManyToManyField(User, related_name = 'commentVoteDown')
    username = models.CharField(max_length=20,null=True)
    
    def __str__(self):
	    return f"User: {self.id} | Body: {self.body}"