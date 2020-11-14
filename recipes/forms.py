from django import forms
from .models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            'user',
            'reName',
            'solution',
            'ingredient',
            'image'
        ]

        widgets = {
            'user': forms.MultipleHiddenInput(),
        }
