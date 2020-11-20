from django import forms
from .models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            'user',
            'reName',
            'tag',
            'ingredient',
            'solution',
            'image',
        ]

        widgets = {
            'user': forms.MultipleHiddenInput()
        }
