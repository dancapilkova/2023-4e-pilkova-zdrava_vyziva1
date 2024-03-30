from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class AddRecipe:
        model = Recipe
        fields = [
            "title",
            "ingredients",
            "instructions",
            "image",
            "day_time",
            "cuisine",
            "calories",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        labels = {
            "title": "Recipe Title",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "day_time": "Day Time",
            "cuisine": "Cuisine",
            "calories": "Calories",
        }