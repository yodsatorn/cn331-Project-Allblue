from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipes

# Create your models here.

class Comments(models.Model):
    
    userID = models.ManyToManyField(User)
    recipeID = models.OneToOneField(Recipes,on_delete=models.CASCADE)
    body = models.CharField(max_length = 4096)
    voteUp= models.ManyToManyField(User, related_name = 'commentVoteUp')
    voteDown = models.ManyToManyField(User, related_name = 'commentVoteDown')
    
    def __str__(self):
	    return f"User: {self.userID} | Body: {self.body}"