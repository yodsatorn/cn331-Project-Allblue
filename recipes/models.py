from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipes(models.Model):
<<<<<<< HEAD

=======
    
    user = models.ManyToManyField(User, related_name = 'userRecipe')
>>>>>>> 1555944364757fed41fb9c2134e74401c284bf71
    reName = models.CharField(max_length = 128)
    solution = models.CharField(max_length = 4096)
    ingredient = models.CharField(max_length = 4096)
    voteUp = models.ManyToManyField(User, related_name = 'recipeVoteUp')
    voteDown = models.ManyToManyField(User, related_name = 'recipeVoteDown')

    def __str__(self):
	    return f"ID: {self.pk} | Recipe: {self.reName} "

class Tags(models.Model):
    tagName = models.CharField(max_length = 64)
    tagID = models.ManyToManyField(Recipes)

    def __str__(self):
        return f"Tag = {self.tagName}"
