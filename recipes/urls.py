from django.urls import path
from .views import NewRecipe

urlpatterns = [
    path("", NewRecipe.as_view(), name="add_recipe"),
]