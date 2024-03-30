from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "ingredients",
            "instructions",
            "image",
            "meal_type",
            "cuisine_types",
            "calories",
        ]
        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        labels = {
            "title": "Recipe Title",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }
