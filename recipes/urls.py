from django.urls import path
from .views import NewRecipe, Recipes, Detail

urlpatterns = [
    path("new/", NewRecipe.as_view(), name="new_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", Detail.as_view(), name="detail"),
]
