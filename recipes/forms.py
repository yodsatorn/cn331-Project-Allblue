from django import forms

class AddRecipe(forms.Form):
    recipeName = forms.CharField()
    solutions = forms.CharField()
    ingredient = forms.CharField()