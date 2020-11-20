from django import forms
from .models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            'user',
            'reName',
            'ingredient',
            'solution',
            'image',
            'tag'
        ]

        widgets = {
            'user': forms.MultipleHiddenInput(),
        }
