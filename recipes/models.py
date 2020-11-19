from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tags(models.Model):
    tagName = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"Tag = {self.tagName}"

    def is_valid_Tags(self):
        return (self.tagName != None)

class Recipes(models.Model):

    user = models.ManyToManyField(User, related_name = 'userRecipe')
    reName = models.CharField(max_length = 128)
    solution = models.TextField()
    ingredient = models.TextField()
    image = models.ImageField(upload_to="images/%Y/%m/%d/" , null=True, blank=True)
    voteUp = models.ManyToManyField(User, related_name = 'recipeVoteUp')
    voteDown = models.ManyToManyField(User, related_name = 'recipeVoteDown')
    tag = models.ManyToManyField(Tags)

    def __str__(self):
	    return f"ID: {self.pk} | Recipe: {self.reName} "

    def is_valid_Recipes(self):
        return (self.reName != None and self.solution != None and self.solution !=None)



